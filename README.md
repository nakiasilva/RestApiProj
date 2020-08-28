# Rest API Application

## Table of Contents

- [Introduction](#introduction)
- [APIs](#APIs)
- [Responses](#response)
- [Installations](#installations)
- [Execution](#execution)
- [Example](#example)



## Introduction

> This project highlights the usage of <a href="https://www.djangoproject.com/" target="_blank">**Django framework**</a> to create <a href="https://www.django-rest-framework.org/" target="_blank">**RESTful APIs**</a> leveraging the Django ORM to faciliate database migrations.

> Database: <a href="https://www.sqlite.org/index.html" target="_blank">**Sqlite3**</a> , a self contained, serverless SQL database engine is used to store, retrieve and alter data hence   eliminating the need of manual creation and handling of database.

> Testing: TDD was employed while writing the test cases for each functionalities.



## APIs
**The following endpoints were created in this application:**

1. `GET /products` - gets all products in the database.
2. `GET /products?name={name}` - finds all products matching the specified name in the database.
3. `GET /products/{id}` - gets the project that matches the specified ID - ID is a UUID in the database.
4. `POST /products` - creates a new product in the database.
5. `PUT /products/{id}` - updates a product in the database.
6. `DELETE /products/{id}` - deletes a product and its options from the database.
7. `GET /products/{id}/options` - finds all options for a specified product in the database.
8. `GET /products/{id}/options/{optionId}` - finds the specified product option for the specified product in the database.
9. `POST /products/{id}/options` - adds a new product option to the specified product in the database.
10. `PUT /products/{id}/options/{optionId}` - updates the specified product option in the database.
11. `DELETE /products/{id}/options/{optionId}` - deletes the specified product option in the database.




## Responses

**Product:**
```
{
  "Id": "01234567-89ab-cdef-0123-456789abcdef",
  "Name": "Product Name",
  "Description": "Product Description",
  "Price": 123.00,
  "DeliveryPrice": 12.00
}
```

**Products:**
```
{
  "Items": [
    {
      // product
    },
    {
      // product
    }
  ]
}
```

**Product Option:**
```
{
  "Id": "01234567-89ab-cdef-0123-456789abcdef",
  "Name": "Product Name",
  "Description": "Product Description"
}
```

**Product Options:**
```
{
  "Items": [
    {
      // product option
    },
    {
      // product option
    }
  ]
}
```



## Installations 

> Install the following depencies


- Install Python >= **3.7.0** </br></br>

- Install pip >= **3.7** 

    `python get-pip.py` </br></br>

- Install Django >= **3.0.8** 

    `pip install Django`</br></br>

- Install **Django REST framework** 

    `pip install djangorestframework`</br></br>

- Install django-cors-headers >= **3.4.0** 

    `pip install django-cors-headers`



## Execution

> To start the server follow the instructions below :

- Open terminal inside the folder `RestApiProj` 

- Run the below command through CLI </br>
    `python manage.py runserver`

- Test endpoints in postman 

## Example

> GET

![Alt text](https://github.com/nakiasilva/RestApiProj/Images/get.png?raw=true "GET")