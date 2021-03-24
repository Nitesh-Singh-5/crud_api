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

First, we have to start up Django's development server:
```
python manage.py runserver
```
Any users can use the API services, for that reason if we try this:
```
http://localhost:8000/api/crud/
```
we get:
```
 [{"id":2,"name":"shreya","email":"shreya123@gmail.com","password":"shreya"},{"id":4,"name":"harry","email":"hdfj@gnail.com","password":"jkwhslkhx"},{"id":5,"name":"Nitesh","email":"ns98738698@gmail.com","password":"Nitesh"},{"id":6,"name":"shivam","email":"shivam123@gmail.com","password":"shivam123"}]
```
we get the movie with id = 5:
```
{"id":5,"name":"Nitesh","email":"ns98738698@gmail.com","password":"Nitesh"}
```





