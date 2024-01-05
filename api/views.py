
from rest_framework.response import Response

from .serializers import NoteSerializer
from notes.models import Note

from rest_framework import generics, permissions
from rest_framework.views import APIView

# For authentication

from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

# for throttle control
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.decorators import throttle_classes , api_view

@csrf_exempt
@throttle_classes([AnonRateThrottle])
def signup(request):
    throttle_instance = AnonRateThrottle()

    if not throttle_instance.allow_request(request=request, view=None):
        return Response({"error" : "Request limits exceeds"})
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'])
            user.save()

            token = Token.objects.create(user=user)
            return JsonResponse({
                "token": str(token),
                "message": "Account is created"
            }, status=201)
        except IntegrityError:
            return JsonResponse({
                "error": 'username taken, choose another username'
            }, status=401)


@csrf_exempt
@throttle_classes([AnonRateThrottle])
@api_view(['POST'])
def login(request):
    throttle_instance = AnonRateThrottle()

    if not throttle_instance.allow_request(request=request, view=None):
        return Response({"error" : "Request limits exceeds"})
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data["username"],
            password=data["password"]
        )
        if user is None:
            return JsonResponse({
                "error": "unable to login, check credentials"
            }, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({
                "token": str(token),
                "message": "Logged in successful"
            }, status=201)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=200)


# Create your views here.


class NotesList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        s = Note.objects.filter(author=user)
        return s

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
