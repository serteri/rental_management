from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#set the database URI via SQLAclhemy
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql+psycopg2://serter:Altay2205@localhost:5432/rental_management"

#to avaoid  the deprecation warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False

#create the database object
db = SQLAlchemy(app)

class User(db.Model):
    #define the table name for the db
    
    __tablename__ = "USERS"
    
    #Set the primary key
    
    user_id = db.Column(db.Integer,primary_key=True)
    
    #Add rest of the attributes
    
    user_name = db.column(db.String())
    user_email = db.Column(db.String())
    user_dob = db.Column(db.Date())

@app.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@app.cli.command("seed")
def seed_db():
    from datetime import date
    
    #create the first user object
    
    user1 = User(
        #set the attributes, not the id

        user_name = "Mehmet",
        user_email = "mehmet@gmail.com",
        user_dob = date(1979,5,22)
    )
    # Add the object as a new row to the table
    db.session.add(user1)
    
    user2 = User(
        #set the attributes, not the id

        user_name = "John",
        user_email = "john@gmail.com",
        user_dob = date(1978,6,15)
    )
    # Add the object as a new row to the table
    db.session.add(user2)
    
    #commit the changes
    db.session.commit()
    print("Table seeded")

@app.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tabled dropped")
    
@app.route("/")
def hello():
  return "Hello World!"