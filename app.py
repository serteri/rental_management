from flask import Flask , jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow.validate import Length

app = Flask(__name__)
ma = Marshmallow(app)

#set the database URI via SQLAclhemy
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql+psycopg2://serter:Altay2205@localhost:5432/rental_management"

#to avaoid  the deprecation warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False

#create the database object
db = SQLAlchemy(app)




@app.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@app.cli.command("seed")
def seed_db():
    from datetime import date
    
    #create the first user object
    
    admin_user = User(
        #set the attributes, not the id

        user_name = "Mehmet",
        user_email = "mehmet@gmail.com",
        user_dob = date(1979,5,22),
        password = "12345698",
        admin = True
    )
    # Add the object as a new row to the tableadd . 
    db.session.add(admin_user)
    
    user1 = User(
        #set the attributes, not the id

        user_name = "John",
        user_email = "john@gmail.com",
        user_dob = date(1978,6,15),
        password = "12345678"
    )
    # Add the object as a new row to the table
    db.session.add(user1)
    
    property1 = Property(
        #set the attributes, not the id

        property_address = "67 Mclennan street",
        property_postcode = "4010",
        property_suburb = "Albion",
        property_state= "QLD"
    )
    # Add the object as a new row to the table
    db.session.add(property1)
    
    
    #commit the changes
    db.session.commit()
    print("Table seeded")

@app.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")

class User(db.Model):
    #define the table name for the db
    
    __tablename__ = "USERS"
    
    #Set the primary key
    
    user_id = db.Column(db.Integer,primary_key=True)
    
    #Add rest of the attributes
    
    user_name = db.Column(db.String(),unique= True,nullable = False)
    user_email = db.Column(db.String(),unique= True,nullable = False)
    user_dob = db.Column(db.Date(),nullable = False)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
class Property(db.Model):
    #define the table name for the db
    
    __tablename__ = "PROPERTIES"
    
    #Set the primary key
    
    property_id = db.Column(db.Integer,primary_key=True)
    
    #Add rest of the attributes
    
    property_address = db.Column(db.String(),nullable = False)
    property_postcode = db.Column(db.String(),nullable = False)
    property_suburb = db.Column(db.String(),nullable = False)
    property_state = db.Column(db.String(),nullable = False)   
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #fields to expose
        model= User
        
        #set the password's length to a minumum of 8 characters
        password = ma.String(validate=Length(min=8))
class PropertySchema(ma.Schema):
    class Meta:
        #fields to expose
        fields = ("property_id","property_address","property_postcode","property_suburb","property_state")        

user_schema = UserSchema()
users_schema = UserSchema(many=True)        
 
property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)

     
@app.route("/")
def hello():
  return "Hello World!"

@app.route("/users", methods = ["GET"])
def get_users():
    # get all the users from the database table
    users_list = User.query.all()
    
    #convert the users from the database into a JSON format and store them in result
    result = users_schema.dump(users_list)
    
    #return the data in JSON format
    
    return jsonify(result)
@app.route("/properties", methods = ["GET"])
def get_properties():
    # get all the users from the database table
    property_list = Property.query.all()
    
    #convert the users from the database into a JSON format and store them in result
    result = properties_schema.dump(property_list)
    
    #return the data in JSON format
    
    return jsonify(result)
