# Rental Management API Idea

## R1

This API for the rental property comment and rating.People can look at this API before going to inspection for a rental property to see all comments (bad or good) for the property and get an idea about the property before inspecting it. People needs to be register before commenting the property. Users need to enter properties address,suburb,postcode etc...They can rate the property. It will ease the finding a rental property process for a rental to help to decide the rental properties by reading comments about the property.

## R2

Finding a rental property is a challenging process. You need to go and inspect the properties in your shortlist. But when you start to live this property, you might experience something bad things for example you can encounter bad neighbouring or some rooms experince the humid badly. It is good to read comments for the property before inspecting the property.

People need to register to comment and rank for a property. People need to enter their user name, email address,date of birth and a password (at least 6 character). Rental property details are rental address, rental property postcode, rental property suburb,rental property state.

## R3

I used Structured Query Language (SQL). SQL is a powerful language for managing relational databases. It is used to create and modify database schemas, insert, update, and delete data, and query and retrieve data from a database. Benefits of SQL include its ease of use and high degree of flexibility. It is the industry standard for interacting with relational databases and can be used in almost any situation.:

1. SQL is created to enable expeditious retrieval of data from immense and intricate databases. It offers a straightforward and adaptable approach to gain access, filter and order data, allowing you to quickly and effectively get the details you need.

2. SQL allows a variety of data manipulation tasks such as inserting, updating, and deleting. These operations make it simple to manage and maintain your database.

3. SQL provides support for constraints to ensure data follows certain requirements like uniqueness and referential integrity, thereby keeping data in the database accurate and consistent.

4. SQL offers built-in protection features, such as authentication and authorization, to ensure that only authorized individuals have access to and can alter the data in a database. Encryption of sensitive information is also enabled by SQL to provide extra security.

I choose PostgreSQL database system.PostgreSQL boasts support for SQL and a wealth of advanced features such as arrays and JSON data types, ACID-compliant transactions, impressive indexing and query optimization acumen. It is highly extensible to the point of allowing developers to produce tailored data types, functions and extensions.SQL is employed in all sorts of projects, ranging from web and mobile applications to data warehousing and business intelligence systems. The language is endorsed by most modern relational database management systems, such as MySQL, Oracle, Microsoft SQL Server and PostgreSQL.

PostgreSQL is renowned for its stability, reliability and outstanding performance, regularly being employed by significant organisations and government agencies globally. It has a free-to-use policy, plus is compatible with Linux, Windows and macOS systems. Furthermore, the PostgreSQL community of developers and users is flourishing and continually evolving as they continue to invest in and support the program.

PostgreSQL is one of the oldest and most widely used open-source relational database management systems. Despite its advantages like robustness, reliability, and a range of features, certain drawbacks may make it less attractive than other databases. Here are some negatives to consider:

1. Setting up and managing PostgreSQL can be more involved than with other databases, particularly for those unfamiliar with database management. To take advantage of its powerful features and capabilities, one needs to have a greater level of knowledge or experience.

2. PostgreSQL is compatible with many programming languages, but not all. It may not offer the same level of compatibility as some other databases.

3. PostgreSQL is capable of dealing with vast quantities of data, however its scalability may be limited compared to certain other databases; especially when faced with very intricate or considerable applications.

4. PostgreSQL is known to be more demanding in terms of resources than other databases, meaning users may need more advanced hardware for optimal performance.

## R4

An Object-Relational Mapping (ORM) is a programming technique that enables developers to access and manipulate relational databases in an object-oriented manner. This approach provides a much more intuitive way to interact with the data stored in the database, as opposed to more traditional database operations. Libraries and tools of ORM systems map database tables to classes and objects in the programming language, providing key functionalities and benefits:

1. ORMs provide developers with an accessible way to interact with databases, allowing them to use their existing knowledge of programming language structures such as classes, objects and methods. This replaces the need for manually writing SQL queries, which significantly reduces the amount of time spent creating boilerplate code for data access and manipulation.

2. ORM systems allow for improved code quality and maintainability, granting developers the ability to focus on the application logic, instead of getting lost in database details. This leads to neater, more modular code which can be easily modified and expanded across time.

3. ORM systems enable developers to employ object-oriented approaches when modelling data, which can facilitate the construction of more flexible and maintainable code, while also enabling a closer relationship between the data model and the application's underlying logic.

4. ORM systems facilitate cross-database compatibility, enabling developers to construct code that functions in a variety of platforms and settings, free from database restrictions.

5. ORM systems often include caching and query optimization capabilities that can boost the performance of database access. This helps to minimize the number of queries sent to the database, leading to an improved speed and responsiveness of the application.

# R5

I do have two controllers. One of them is user contoller and the other one is properties controller.

In the user controller-

1. To see all users,there is an end point "/users", methods = ["GET"]

```python
def get_users():

    return User.query.all()

```

2. To create a user- "/register", methods=["POST"]- Post method have been used

```python
@users.route("/register", methods=["POST"])
@users.arguments(UserSchema)
@users.response(201,UserSchema)
def create_user(user_data):
     #Create a new user
    user_fields =user_schema.load(request.json)


    new_user = User.query.filter_by(user_email=user_fields["user_email"]).first()

    if new_user:
        # return an abort message to inform the user. That will end the request
        return abort(400, description="Email already registered")

    new_user = User()
    new_user.user_name = user_fields["user_name"]

     #Add the new user attributes
    new_user.user_email = user_fields["user_email"]

    new_user.user_dob = user_fields["user_dob"]
    new_user.user_password = bcrypt.generate_password_hash(user_fields["user_password"]).decode("utf-8")
    new_user.admin = user_data["admin"]
    #add to the database and commit
    db.session.add(new_user)
    db.session.commit()

    #create a variable that sets an expiry date

    expiry = timedelta(days=1)

    #create the access token
    access_token = create_access_token(identity=str(new_user.user_id), expires_delta=expiry)


    # return the user email and the access token
    return jsonify({"new_user":new_user.user_name, "token": access_token })

```

3. To login - there is a method for that. "/login", methods=["POST"] - this method uses to login to the API.

```python
def user_login():
    # get the user data from the request
    user_fields = user_schema.load(request.json)
    #find the user in the database by email
    user = User.query.filter_by(user_email=user_fields["user_email"]).first()
    # there is not a user with that email or if the password is no correct send an error
    if not user or not bcrypt.check_password_hash(user.user_password, user_fields["user_password"]):
        return abort(401, description="Incorrect username and password")

    #create a variable that sets an expiry date
    expiry = timedelta(days=1)
    #create the access token
    access_token = create_access_token(identity=str(user.user_id), expires_delta=expiry)
    # return the user email and the access token
    return jsonify({"user":user.user_email, "token": access_token })
```

4. To delete an user. There is a method and end point is "/<int:id>/", methods=["DELETE"]).
   we use user_id to find the user and perform deletion. Only admin can delete the user.

   ```python
    user = User.query.filter_by(user_id=id).first()
    # #return an error if the user doesn't exist
    if not user:

         return abort(400, description= "User doesn't exist")
    if not user.admin:
        return abort(401, description="Unauthorised user")
    # #Delete the user from the database and commit
    db.session.delete(user)
    db.session.commit()
    # #return the user in the response
    return jsonify(user_schema.dump(user))
   ```

5. To see an individual user ,there is an enpoint for that. "/users/<int:id>", methods= ["GET"]

```python
 def get_user(id):
       user = User.query.filter_by(user_id=id).first()
       #return an error if the user does not exist
       if not user:
           return abort(400,description ="User does not exist")

       #Convert the users from the database into a JSON format and store them in result

       result = user_schema.dump(user)

       #return the data in JSON format

       return jsonify(result)
```

6. To update an user,there is an endpoint for that . "/users/<int:id>", methods= ["PUT"]

```python
def update_user(id):
    # get the user data from the request
       user_fields = user_schema.load(request.json)
       #find the user
       user = User.query.filter_by(user_id=id).first()
       #return an error if the user does not exist
       if not user:
           return abort(400,description ="User does not exist")

       #fill the attributes

       user.user_name = user_fields["user_name"]
       user.user_email = user_fields["user_email"]
       user.user_dob = user_fields["user_dob"]

       #add to the database and commit
       db.session.commit()

       #return the data in JSON format

       return jsonify(user_schema.dump(user))
```

In the property controller -

1. To see all properties,it is the and point "/properties", methods = ["GET"]

```python
def get_properties():
            # get all the users from the database table
            property_list = Property.query.all()

            #convert the users from the database into a JSON format and store them in result
            result = properties_schema.dump(property_list)

            #return the data in JSON format


            return jsonify(result)
```

2. To see a property,I used "/property/<int:id>/", methods= ["GET"] this end point.

```python
def get_property(id):

    #find the property
     property = Property.query.filter_by(property_id=id).first()

     #return an error if the property does not exist

     if not property:
          return abort(400,description = "Property does not exist.")

     #Convert the propertties from the database into a JSON format and store them in result
     result = property_schema.dump(property)

     #return  the data in JSON format
     return jsonify(result)
```

3. To add a property - "/properties/new", methods=["POST"]

```python
def create_property():
     #Create a new user
    property_fields = property_schema.load(request.json)

     #find the property in the database
    new_property =Property.query.filter_by(property_address=property_fields["property_address"]).first()
    #property in the database,return an error
    if new_property:
        # return an abort message to inform the user. That will end the request
        return abort(400, description="Property already registered")

     #get the user id
    u_id = get_jwt_identity()

    #new property
    new_property =Property()
    new_property.property_address = property_fields["property_address"]

     #Add property  attributes
    new_property.property_postcode = property_fields["property_postcode"]

    new_property.property_suburb = property_fields["property_suburb"]
    new_property.property_state = property_fields["property_state"]
    new_property.u_id = u_id
    #add to the database and commit
    db.session.add(new_property)
    db.session.commit()

    # return the property address and user id
    return jsonify({"new_property":new_property.property_address , "id":new_property.u_id})
```

4. To update a property -"/<int:id>", methods=["PUT"] Only admin can update the property.

```python
def update_property(id):
     property_fields = property_schema.load(request.json)
     #get user from jwt
     u_id = get_jwt_identity()
    #Find it in the db
     user = User.query.get(u_id)

     #Make sure it is in the database
     if not user:
          return abort(401,description="Invalid user")

     #Stop the request if the user is not admin
     if not user.admin:
          return abort(401, description = "Unauthorised user")

     #find the property
     property = Property.query.filter_by(u_id=id).first()
     #return an error if the property deos not exist
     if not property:
          return abort(400,description= "Property does not exist")

     #update the property  details with the given values

     property.property_address = property_fields["property_address"]
     property.property_postcode = property_fields["property_postcode"]
     property.property_suburb = property_fields["property_suburb"]
     property.property_state = property_fields["property_state"]
     db.session.commit()

     #return the property in the response

     return jsonify(property_schema.dump(property))
```

5. To delete a property - "/properties/<int:id>/", methods=["DELETE"] Only admin can delete the property.

```python
def delete_property(id):
    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
    # find the property
    property = Property.query.filter_by(property_id=id).first()
    #return an error if the property doesn't exist
    if not property:
        return abort(400, description= "Property does not exist")
    #Delete the property from the database and commit
    db.session.delete(property)
    db.session.commit()
    #return the propertu in the response
    return jsonify(property_schema.dump(property))
```

6. To search a property based on an attribute : "/search", methods=["GET"]

```python
def search_properties():

     property_list = Property.query.filter_by(property_postcode = request.args.get('property_postcode'))

     result = properties_schema.dump(property_list)
     #return the data in JSON format
     return jsonify(result)
```

For comments in the property controller

1. To post a comment: "/property/<int:id>/comments",methods=["POST"]

```python
def post_comment(id):
     #create a new comment
     comment_fields = comment_schema.load(request.json)
     #get the user id invoking get_jwr_identiy
     user_id = get_jwt_identity()
     #find it in the db
     user =User.query.get(user_id)

     #Make sure it is in the database
     if not user:
          return abort(401,description="Invalid user")

     #find the property
     property = Property.query.filter_by(property_id=id).first()
     #return an error if the property does not exist
     if not property:
          return abort(401,description="Property does not exist")

     #create a  comment with the given values

     new_comment= Comment()

     new_comment.comment= comment_fields["comment"]

     #Use the property gotten by the id of the route

     new_comment.pro_id =property.property_id

     #use that id to set the qwnership of the property

     new_comment.us_id = user_id

     #add to the database and commit

     db.session.add(new_comment)
     db.session.commit()

     #return the card in the response
     return jsonify(property_schema.dump(property))
```

2. To delete a comment : "/property/<int:id>/comments",methods=["DELETE"]

```python
def delete_comment(id):
    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
    # find the property
    property = Property.query.filter_by(property_id=id).first()
    #return an error if the property doesn't exist
    if not property:
        return abort(400, description= "Property does not exist")


     #find the commit
    comment= Comment.query.filter_by(pro_id=id).first()
    #return an error if not commit
    if not comment:
          return abort(400, description= "Comment does not exist")
    db.session.delete(comment)
    db.session.commit()

     #return the property in the response
    return jsonify(property_schema.dump(comment))
```

3. To update a comment : "/property/<int:id>/comments",methods=["PUT"]

```python
def update_comment(id):

      #create a new comment
    comment_fields = comment_schema.load(request.json)

    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
#     # find the property
    property = Property.query.filter_by(property_id=id).first()
    #return an error if the property doesn't exist
    if not property:
        return abort(400, description= "Property does not exist")


     #find the comment
    comment= Comment.query.filter_by(pro_id=id).first()
    #comment not in the database,return an error
    if not comment:
          return abort(400, description= "Comment does not exist")

    comment.comment= comment_fields["comment"]
    db.session.commit()

     #return the property in the response
    return jsonify(property_schema.dump(comment))
```

For ranks in the property controller

1. To post a rank : "/property/<int:id>/ranks",methods=["POST"]

```python
def post_rank(id):
     #create a new comment
     rank_fields = rank_schema.load(request.json)
     #get the user id invoking get_jwr_identiy
     user_id = get_jwt_identity()
     #find it in the db
     user =User.query.get(user_id)

     #Make sure it is in the database
     if not user:
          return abort(401,description="Invalid user")

     #find the property
     property = Property.query.filter_by(property_id=id).first()
     #return an error if the property does not exist
     if not property:
          return abort(401,description="Property does not exist")

     #create a  rank with the given values

     new_rank= Rank()

     new_rank.rank= rank_fields["rank"]

     #Use the property gotten by the id of the route

     new_rank.prop_id =property.property_id

     #use that id to set the ownership of the rank

     new_rank.u_id = user_id

     #add to the database and commit

     db.session.add(new_rank)
     db.session.commit()

     #return the property in the response
     return jsonify(property_schema.dump(property))
```

2. To delete a rank : "/property/<int:id>/ranks",methods=["DELETE"]

```python
def delete_rank(id):
    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
    # find the property
    property = Property.query.filter_by(property_id=id).first()
    #return an error if the property doesn't exist
    if not property:
        return abort(400, description= "Property does not exist")


     #find the rank
    rank= Rank.query.filter_by(prop_id=id).first()
    #return an error if there is no rank
    if not rank:
          return abort(400, description= "Rank does not exist")
      #delete and commit it
    db.session.delete(rank)
    db.session.commit()

     #return the rank in the response
    return jsonify(property_schema.dump(rank))
```

3. To update a rank : "/property/<int:id>/ranks",methods=["PUT"]

```python
def update_rank(id):

      #create a new rank
    rank_fields = rank_schema.load(request.json)

    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
#     # find the property
    property = Property.query.filter_by(property_id=id).first()
    #return an error if the property doesn't exist
    if not property:
        return abort(400, description= "Property does not exist")


     #find the rank
    rank= Rank.query.filter_by(prop_id=id).first()
    #return an error if there is no rank
    if not rank:
          return abort(400, description= "Rank does not exist")

    rank.rank= rank_fields["rank"]
    db.session.commit()

     #return the rank in the response
    return jsonify(property_schema.dump(rank))
```

# R6

My ERD is showing below.

![Rental Management ERD](./ERD/rental_management%20ERD.png)

In the ERD ,there are two main tables which are Users and Resitential property. In the User table, primary key user id is a foreign key in the residential property table.

There are two other tables which are comments and rating tables.

Both tables have user id and property id as a foreign key.

# R7

I used third party servives and here is the list of all of them.

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

In the ERD, users and rental property are the two main tables. I used user id as a foreign key in the property table because it is one to many relation ship. One user can have many properties but a property has one user.

There are two more tables which are comments and ranks. Both tables have two foreign keys user id and property id. Because it is many to many relationship and it need a new table.

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

In the field section, there are three main fields which are users, comments and ranks.In the ERM, properties table has user_id as a foreign key.

users nested UserSchema and only shows user_name,user_email,user_id. It gets information from user table but only gets these three information mention above line.

comments nested CommentSchema and getting information from this table. Comments table in the databese has comment_id, comment ,user_id and property_id as foreign keys.

ranks nested RankSchema and getting information from this table. Ranks table in the databese has rank_id, rank ,user_id and property_id as foreign keys.

ERM shows that comments and ranks table have user id and property id as foreign keys.

In the comments_schema file:

```python
class CommentSchema(ma.Schema):
    class Meta:
     ordered = True
        # Fields to expose
     fields = ("comment_id","comment","users")
    users= fields.Nested("UserSchema",only=("user_email","user_name",))
```

In the field section, there are two main fields which are comment id, comment. It has one more field which is users.

users nested UserSchema and only shows user_name,user_email. It gets information from user table but only gets these two information mention above line.

ERM shows that comments table have user id and property id as foreign keys.

In the ranks_schema file:

```python
class RankSchema(ma.Schema):
    class Meta:
     ordered = True
        # Fields to expose
     fields = ("rank_id","rank","users")
    users= fields.Nested("UserSchema",only=("user_email","user_name",))

```

In the field section, there are two main fields which are rank id and rank. It has one more field which is users.

users nested UserSchema and only shows user_name,user_email. It gets information from user table but only gets these two information mention above line.

ERM diagram shows that ranks table have user id and property id as foreign keys.

One to many relationship between user and property. I used user id as a foreign key in the property table.
Many to many relationship. Ranks and comments are the example of many to many relationship which needs a new table. In these tables user id and property id used as a foreign key.
