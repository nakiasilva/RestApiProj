# RestApiProj
 Django Rest API Project

 # Rest API Application

> This project highlights the usage of <a href="https://www.djangoproject.com/" target="_blank">**Django framework**</a> to create RESTful APIs leveraging the Django ORM to faciliate database migrations.

> Sqlite3, a self contained, serverless SQL database engine is used to store, retrieve and alter data hence   eliminating the need of manual creation and handling of database.

> TDD was employed while writing the test cases for each functionalities.


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


The 

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

