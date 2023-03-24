from flask import jsonify, request
from main import db
from models.users import User
from schemas.user_schema import user_schema, users_schema
from datetime import date ,timedelta
from main import bcrypt
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity
from schemas.user_schema import UserSchema
from sqlalchemy.exc  import SQLAlchemyError
from flask_smorest import Blueprint , abort

users = Blueprint('users', __name__)

# The GET routes endpoint
@users.route("/users", methods = ["GET"])
@users.response(200,UserSchema(many=True))
def get_users():
    
    return User.query.all()
        
# The POST route endpoint
@users.route("/register", methods=["POST"])
@users.arguments(UserSchema)
@users.response(201,UserSchema)   
def create_user(user_data):
     #Create a new user
    user_fields =user_schema.load(request.json)
    
    #find the new_user in the database by using user_fields['user_email']
    new_user = User.query.filter_by(user_email=user_fields["user_email"]).first()

    if new_user:
        # return an abort message to inform the user. That will end the request
        return abort(400, description="Email already registered")
    
    #create a new user
    new_user = User()
    
      #Add the new user attributes
    new_user.user_name = user_fields["user_name"]
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
    
@users.route("/login", methods=["POST"])
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

# Finally, we round out our CRUD resource with a DELETE method
@users.route("/<int:id>/", methods=["DELETE"])
def delete_user(id):
    # #get the user id invoking get_jwt_identity
    #user_id = get_jwt_identity()
    # #Find it in the db
    #user = User.query.get(user_id)
    # #Make sure it is in the database
    #if not user:
    #    return abort(401, description="Invalid user")
    # # Stop the request if the user is not an admin
  
    # # find the user
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

@users.route("/users/<int:id>", methods= ["GET"])
def get_user(id):
       user = User.query.filter_by(user_id=id).first()
       #return an error if the user does not exist
       if not user:
           return abort(400,description ="User does not exist")
       
       #Convert the users from the database into a JSON format and store them in result
       
       result = user_schema.dump(user)
       
       #return the data in JSON format
       
       return jsonify(result)
   
@users.route("/users/<int:id>", methods= ["PUT"])
@jwt_required()
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