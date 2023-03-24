# Rental Management API Idea

## R1

This API for the rental property comment and rating.People can look at this API before going to inspection for a rental property to see all comments (bad or good) for the property and get an idea about the property before inspecting it. People needs to be register before commenting the property. Users need to enter properties address,suburb,postcode etc...They can rate the property.

## R2

Finding a rental property is a challenging process. You need to go and inspect the properties in your shortlist. But when you start to live this property, you might experience something bad things for example you can encounter bad neighbouring or some rooms experince the humid badly. It is good to read comments for the property before inspecting the property.

People need to register to comment and rank for a property. People need to enter their user name, email address,date of birth and a password (at least 6 character). Rental property details are rental address, rental property postcode, rental property suburb,rental property state.

## R3

I used Structured Query Language (SQL). It is a powerful and widely used programming language for relatioanl database management systems.It is a programming language used to manage and manipulate relational databases. SQL is the standard language used to interact with relational databases and is used to perform tasks such as creating and modifying database schema, inserting, updating, and deleting data, and querying and retrieving data from a database. SQL Advantages are:

1. Data retrieval: SQL is designed for efficient retrieval of data from large and complex databases. It provides a simple and flexible way to access, filter, and sort data, making it easy to retrieve the information you need quickly and efficiently.

2. Data manipulation: SQL supports a wide range of data manipulation operations, including inserting, updating, and deleting data. This makes it easy to manage the data in your database and keep it up to date.

3. Data integrity: SQL enforces data integrity through its support of constraints, which ensure that the data in the database meets certain requirements, such as uniqueness or referential integrity. This helps to maintain the accuracy and consistency of the data in the database.

4. Data security: SQL provides built-in security features, such as authentication and authorization mechanisms, to ensure that only authorized users can access and modify the data in the database. It also supports encryption of sensitive data to protect it from unauthorized access.

I choose PostgreSQL database system.PostgreSQL supports SQL and offers many advanced features, including support for advanced data types like arrays and JSON, transactions with ACID properties, and powerful indexing and query optimization capabilities. It is also highly extensible and allows developers to create custom data types, functions, and extensions.SQL is used in many different types of applications, from web and mobile applications to business intelligence and data warehousing. It is supported by most modern relational database management systems, including MySQL, Oracle, Microsoft SQL Server, and PostgreSQL, among others.

PostgreSQL is known for its stability, reliability, and high performance, and it is used by many large organizations and government agencies around the world. It is available for free and runs on a variety of platforms, including Linux, Windows, and macOS. Additionally, there is a large and active community of developers and users who contribute to the ongoing development and support of PostgreSQL.
PostgreSQL is a popular open-source relational database management system that has been widely used for many years. While PostgreSQL has many advantages, including high performance, reliability, and advanced features, there are also some potential drawbacks compared to other databases. Here are some of the main drawbacks of PostgreSQL:

1. Complexity: PostgreSQL can be more complex to set up and manage compared to other databases, especially for those who are new to database management. Its advanced features and capabilities can require more knowledge and experience to fully utilize.

2. Limited compatibility: While PostgreSQL supports many programming languages, it may not be as compatible with certain programming languages as other databases.

3. Limited scalability: While PostgreSQL can handle large amounts of data, it may not be as scalable as some other databases, particularly for very large or complex applications.

4. Resource-intensive: PostgreSQL can be more resource-intensive compared to other databases, which can impact performance and require more powerful hardware.

## R4

An ORM (Object-Relational Mapping) is a programming technique that allows developers to interact with relational databases using an object-oriented programming paradigm. ORM systems typically provide a set of libraries and tools that map database tables to classes and objects in the programming language, providing a more natural and intuitive way to interact with the data stored in the database. Here are some of the key functionalities and benefits of an ORM:

1. Simplified database access: With an ORM, developers can interact with the database using familiar programming language constructs such as classes, objects, and methods, rather than writing SQL queries directly. This simplifies database access and makes it more intuitive for developers, reducing the amount of boilerplate code required to access and manipulate the data in the database.

2. Improved code quality and maintainability: ORM systems provide a high level of abstraction, allowing developers to focus on the logic of their applications rather than the details of the underlying database. This can lead to cleaner, more modular code that is easier to maintain and extend over time.

3. Object-oriented modeling of data: ORM systems allow developers to model their data using object-oriented principles, providing a more natural and intuitive way to think about and interact with the data. This can lead to more flexible and maintainable code, as well as better alignment between the data model and the business logic of the application.

4. Cross-database compatibility: ORM systems typically support multiple database management systems, allowing developers to write database-independent code that can be used across a variety of platforms and environments.

5. Performance optimization: ORM systems often provide advanced caching and query optimization features that can help to improve the performance of database access. This can help to reduce the number of queries executed against the database, and improve the overall speed and responsiveness of the application.

# R5

I do have two controllers. One of them is user contoller and the other one is properties controller.

In the user controller-

1. To see all users,there is an end point "/users", methods = ["GET"]
2. To create a user- "/register", methods=["POST"]- Post method have been used
3. To login - there is a method for that. "/login", methods=["POST"] - this method uses to login to the API.
4. To delete an user. There is a method and end point is "/<int:id>/", methods=["DELETE"]).
   we use user_id to find the user and perform deletion. Only admin can delete the user.
5. To see an individual user ,there is an enpoint for that. "/users/<int:id>", methods= ["GET"]
6. To update an user,there is an endpoint for that . "/users/<int:id>", methods= ["PUT"]

In the property controller -

1. To see all properties,it is the and point "/properties", methods = ["GET"]
2. To see a property,I used "/property/<int:id>/", methods= ["GET"] this end point.
3. To add a property - "/properties/new", methods=["POST"]
4. To update a property -"/<int:id>", methods=["PUT"] Only admin can update the property.
5. To delete a property - "/properties/<int:id>/", methods=["DELETE"] Only admin can delete the property.
6. To search a property based on an attribute : "/search", methods=["GET"]

For comments in the property controller

1. To post a comment: "/property/<int:id>/comments",methods=["POST"]
2. To delete a comment : "/property/<int:id>/comments",methods=["DELETE"]
3. To update a comment : "/property/<int:id>/comments",methods=["PUT"]

For ranks in the property controller

1. To post a rank : "/property/<int:id>/ranks",methods=["POST"]
2. To delete a rank : "/property/<int:id>/ranks",methods=["DELETE"]
3. To update a rank : "/property/<int:id>/ranks",methods=["PUT"]

# R6

My ERD is showing below.

![Rental Management ERD](./ERD/rental_management%20ERD.png)

In the ERD ,there are two main tables which are Users and Resitential property. In the User table, primary key user id is a foreign key in the residential property table.

There are two other tables which are comments and rating tables.

Both tables have user id and property id as a foreign key.

# R7

I used third parry servives and here is the list of all of them.

1. **python-dotenv** : Python-dotenv is a library which enables loading of environment variables from a .env file. These can be used in software development as a way to store sensitive info, like API access codes, database passwords and configuration data. The library makes management of variables far simpler, since they are stored inside a .env located in the root directory; this is not tracked by version control systems such as Git, so is ideal for keeping config secure.
2. **Flask-SQLAlchemy** : This Flask extension supplies a convenient interface for operating with relational databases within Flask projects. It is designed to leverage the robust SQLAlchemy toolkit and Object-Relational Mapping (ORM) library for Python.

Flask-SQLAlchemy simplifies the process of creating database models with Python classes, and establishing relationships between them. It offers an abstraction layer that lets you take advantage of different backends such as SQLite, PostgreSQL and MySQL, without altering your code. You can interact with the database using an intuitive Python syntax.

3. **Flask-Bcrypt** : Flask-Bcrypt allows you to quickly and securely hash passwords in your application. It offers an easy-to-use API for taking passwords and comparing them against the stored hashes. It utilizes the bcrypt algorithm, an industry standard that is known for being computationally expensive while also highly secure.

4. **Flask-JWT-Extended**: Flask-JWT-Extended provides a secure means of authenticating and authorizing users in web applications, utilizing the popular JSON Web Tokens. Flask-JWT-Extended simplifies the process of adding authentication and authorization to a Flask application. It creates JWTs for authenticated users, and validates these tokens on secured endpoints in order to give access according to the contents of the tokens.
5. **PyJWT**: PyJWT is a Python library which simplifies working with JSON Web Tokens. JWTs are a popular and secure way of authenticating and authorizing users in web applications. PyJWT makes it easy to use JWTs with its easy-to-use API, providing methods for creating, encoding, decoding and verifying signatures. PyJWT offers an uncomplicated and easy to utilize API for using JWTs within Python applications.

6. **sqlalchemy.exc** : The sqlalchemy.exc module of the SQLAlchemy Python library includes a set of exceptions that are raised when mistakes take place while using SQLAlchemy to communicate with databases. These exceptions provide in-depth information about what led to the mistake, including the database error type, the query which caused it, and any related messages or stack traces. The sqlalchemy.exc module contains several exceptions, including DatabaseError, IntegrityError, OperationalError, and InvalidRequestError. These occur in cases of a connection failure or syntax error in a query, when a database constraint is violated, an operational issue arises, or an invalid request is sent. If an IntegrityError exception is raised, we catch it, rollback the transaction, and print the error message for further insight. SQLAlchemy's sqlalchemy.exc module provides a range of options for managing errors and exceptions when dealing with databases using Python and SQLAlchemy.
7. **Marshmallow** : Marshmallow is a Python library that enables the transformation of complex data types like JSON and database records into Python objects and vice versa. It is commonly used in web applications to facilitate the interchange of information between clients and servers. Additionally, this library offers a wide range of possibilities for specifying custom schemas that determine the shape and format of the data during serialization or deserialization processes. With Marshmallow, users can work with different data types including strings, numbers, dates, lists, nested objects, and more.

# R8

In my model folder there are four files.
Two main files and two other files.

In the user file : There are 6 main rows which are user_id,user_name,user_email,user_dob, user_password and admin.

user_name,user_email and user_password are string.
properties row is linked to property table. Backref is users.

There is a comments row which is linked to comments table, and backref is user.
The last one is ranks row which linked to ranks table and backref is user.

The second main table is property table.It has 5 main rows which are property_id ,property_address, property_postcode, property_suburb, property_state.

It has one foreign key which is u_id ,relation with user table. Same as the user table there are two relation with other tables. one is comments and the other one is ranking.

In the comment table, there are two main rows which are comment_id and comment.
It has two foreign keys, which are us_id from user table and pro_id from property table.

In the ranks table,there are two main rows which are ranking_id and rank. It has two foreign keys which are u_id from user table(user_id) and prop_id from property table(property_id)

# R9

In the user_schema file:

```python
 class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id","user_name","user_email","user_dob","user_password","admin","properties")
        load_only = ('user_password', 'admin')
        #set the password's length to a minimum of 6 characters
    user_password = ma.String(validate=Length(min=6))
    properties = fields.List(fields.Nested("PropertySchema",exclude=("users",)))
```

I added properties field which is nested PropertySchema. In the property_schema file ,in the fields section there is a users field or rows. I exclude in the UserSchema properties field. There will be a lot of information which is unneccsarry.

In the properties_schema file:

```python
class PropertySchema(ma.Schema):
    class Meta:
     ordered = True
        # Fields to expose
     fields = ("property_id", "property_address", "property_postcode", "property_suburb","property_state","users","comments","ranks")
    users=fields.Nested("UserSchema",only=("user_name","user_email","user_id",))
    comments= fields.List(fields.Nested("CommentSchema"))
    ranks= fields.List(fields.Nested("RankSchema"))


```

In the field section, there are three more fields which are users, comments and ranks..

users nested UserSchema and only shows user_name,user_email,user_id. It gets information from user table but only gets these three information mention above line.
