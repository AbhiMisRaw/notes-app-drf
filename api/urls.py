from django.urls import path

from . import views

urlpatterns = [
    path('notes/',views.NotesList.as_view()),
    path('notes/<int:pk>', views.NoteRetriveUpdateDestroy.as_view()),
    path('auth/signup/', views.signup),
    path('auth/login/', views.login),
    path('auth/logout/', views.Logout.as_view()),
]