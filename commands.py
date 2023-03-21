from main import db
from flask import Blueprint
from main import bcrypt
from models.users import User
from models.property import Property
from datetime import date

db_commands = Blueprint("db", __name__)

# create app's cli command named create, then run it in the terminal as "flask db create", 
# it will invoke create_db function
@db_commands .cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands .cli.command("seed")
def seed_db():

    admin_user = User(
        user_name ="adassdad",
        
        user_email = "admiwn@email.com",
        user_dob = "1987-04-22",
        user_password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        admin = True
    )
    db.session.add(admin_user)

    user1 = User(
        user_name = "asdas2qqq",
        user_email = "use3r1@email.com",
        user_dob = "1976-02-12",
        user_password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    db.session.add(user1)
    db.session.commit()
    
    property1 = Property(
        property_address = "67 Mclennasn street",
        property_postcode = "4010",
        property_suburb = "Albion",
        property_state = "QLD",
        id = user1.user_id
        
    )
    db.session.add(property1)
    
    property2 = Property(
        property_address = "68 Mclennasn street",
        property_postcode = "4010",
        property_suburb = "Albion",
        property_state = "QLD",
        user = admin_user
        
    )
    db.session.add(property2)
    # commit the changes
    db.session.commit()
    print("Table seeded") 

@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 