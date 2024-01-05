
# Notes App

This API is built using Django Rest Framework and Postgres DB

## Features

- Signup, Login and logout
- user can add / update / delete / fetch all notes using endpoints
- Request limit





## API Reference

- If you are using _POSTMAN_ add **Authorization** header in **Headers** section for each request except `signup` and `login`
```jso
  KEY : "Authorization",
  Value : "Token <TOKEN STRING>"
```
- If you are using `curl`
```json
curl -X GET http://127.0.0.1:8000/api/notes/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```

### For Registration
- Endpoints

 >   POST /api/auth/signup/

- Body
```json
{
  "username": "USERNAME",
  "password": "PASSWORD"
}
```
### For Signin
- Endpoints
 
> POST /api/auth/signin/

- Body
```json
{
  "username": "USERNAME",
  "password": "PASSWORD"
}
```
### For Log-out

- for this feature you have to provide the token header in the request

>  GET /api/auth/logout/

```json
  curl -X GET http://127.0.0.1:8000/api/auth/logout -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```


#### 1. Get all notes


> GET /api/notes

#### 2. Add a notes

> POST /api/notes



#### 3. Endpoints to work on a particular note
- _to fetch a note_

 > GET /api/items/${id}
- _to update a note_
 >  PUT /api/items/${id}

- _to delete a note_

 > DELETE /api/items/${id}


| Parameter | Type     | Description                       |
| :-------- | :------- |:----------------------------------|
| `id`      | `string` | **Required**. Id of note to fetch |





## Requirement
 - Python
 - PostgreSQL
 - Postman



## How to run Locally

1. Select a directory
2. make an virtual environment
3. Clone the project

```bash
  git clone https://github.com/AbhiMisRaw/notes-app-drf.git
```
4. Enable virtual environment
5. Go to the cloned project directory

```bash
  cd notes-app-drf
```
6. Install dependencies

```bash
  pip install -r requirements.txt
```
7. Setup Postgres Database database
8. Replace database configuration in manage.py file according to this
```bash
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<NAME OF YOU DATABASE>',
        'USER': '<USER NAME>',
        'PASSWORD': '<PASSWORD>',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

9. Run migrations
```bash
  python manage.py makemigrations
  python manage.py migrate
```

10. Start the server

```bash
  python manage.py runserver
```
CONGRATS