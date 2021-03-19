# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Django==3.1
- djangorestframework==3.12.2
- djangorestframework-simplejwt==4.3.0

## Installation
```
	pip install django
	pip install djangorestframework
	pip install django-rest-auth
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `crud`, so we will use the following URLS - `/api/crud/` and `/api/crud/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`crud` | GET | READ | Get all user details
`crud/:id` | GET | READ | Get a single user details
`crud`| POST | CREATE | Create a new user details
`crud/:id` | PUT | UPDATE | Update a user details
`crud/:id` | DELETE | DELETE | Delete a user details

First, we have to start up Django's development server.
```
	python manage.py runserver
```
Any users can use the API services, for that reason if we try this:
```
	http://localhost:8000/api/crud/
```
we get:
```
 [{"id":2,"name":"shreya","email":"shreya123@gmail.com","password":"shreya"},{"id":4,"name":"harry","email":"hdfj@gnail.com","password":"jkwhslkhx"},{"id":5,"name":"Nitesh","email":"ns98738698@gmail.com","password":"Nitesh"}]
```
Instead, if we try to access with credentials:
```
	http http://127.0.0.1:8000/api/v1/movies/3 "Authorization: Token 7530ec9186a31a5b3dd8d03d84e34f80941391e3"
```
we get the movie with id = 3
```
{  "title":  "Avengers",  "genre":  "Superheroes",  "year":  2012,  "creator":  "admin"  }
```

## Login and Tokens

To get a token first we have to login
```
	http http://127.0.0.1:8000/rest-auth/login/ username="admin" password="root1234"
```
after that, we get the token
```
{
    "key": "2d500db1e51153318e300860064e52c061e72016"
}
```
**ALL request must be authenticated with a valid token, otherwise they will be invalid**

We can create new users. (password1 and password2 must be equal)
```
http POST http://127.0.0.1:8000/rest-auth/registration/ username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```
And we can logout, the token must be your actual token
```
http POST http://127.0.0.1:8000/rest-auth/logout/ "Authorization: Token <YOUR_TOKEN>" 
```

The API has some restrictions:
-   The movies are always associated with a creator (user who created it).
-   Only authenticated users may create and see movies.
-   Only the creator of a movie may update or delete it.
-   Unauthenticated requests shouldn't have access.

### Commands
```
http http://127.0.0.1:8000/api/v1/movies/ "Authorization: Token <YOUR_TOKEN>"
http GET http://127.0.0.1:8000/api/v1/movies/3 "Authorization: Token <YOUR_TOKEN>"
http POST http://127.0.0.1:8000/api/v1/movies/ "Authorization: Token <YOUR_TOKEN>" title="Ant Man and The Wasp" genre="Action" year=2018
http PUT http://127.0.0.1:8000/api/v1/movies/3 "Authorization: Token <YOUR_TOKEN>" title="AntMan and The Wasp" genre="Action" year=2018
http DELETE http://127.0.0.1:8000/api/v1/movies/3 "Authorization: Token <YOUR_TOKEN>"
```

### Pagination
The API supports pagination, by default responses have a page_size=10 but if you want change that you can pass through params page=size=X
```
http http://127.0.0.1:8000/api/v1/movies/?page=1 "Authorization: Token <YOUR_TOKEN>"
http http://127.0.0.1:8000/api/v1/movies/?page=3 "Authorization: Token <YOUR_TOKEN>"
http http://127.0.0.1:8000/api/v1/movies/?page=3&page_size=15 "Authorization: Token <YOUR_TOKEN>"
```

Finally, I provide a DB to make these tests.

