from flask import Blueprint, jsonify, request,abort
from main import db
from models.property import Property
from models.users import User
from schemas.properties_schema import properties_schema,property_schema
from main import bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date ,timedelta

properties = Blueprint('properties', __name__)


@properties.route("/properties", methods = ["GET"])
def get_properties():
            # get all the users from the database table
            property_list = Property.query.all()
            
            #convert the users from the database into a JSON format and store them in result
            result = properties_schema.dump(property_list)
            
            #return the data in JSON format
            
            return jsonify(result)
# The POST route endpoint


@properties.route("/property/<int:id>/", methods= ["GET"])
def get_property(id):
     property = Property.query.filter_by(property_id=id).first()
     
     #return an error if the property does not exist
     
     if not property:
          return abort(400,description = "Property does not exist.")
    
     #Convert the propertties from the database into a JSON format and store them in result
     result = property_schema.dump(property)
     
     #return  the data in JSON format
     return jsonify(result)

@properties.route("/properties/new", methods=["POST"])
@jwt_required()
def create_property():
     #Create a new user
    property_fields = property_schema.load(request.json)
   
    new_property =Property.query.filter_by(property_address=property_fields["property_address"]).first()

    if new_property:
        # return an abort message to inform the user. That will end the request
        return abort(400, description="Property already registered")
   
    id = get_jwt_identity()
    new_property =Property()
    new_property.property_address = property_fields["property_address"]
                                     
     #Add the email attribute
    new_property.property_postcode = property_fields["property_postcode"]
    
    new_property.property_suburb = property_fields["property_suburb"]
    new_property.property_state = property_fields["property_state"]
    new_property.id = id
    #add to the database and commit
    db.session.add(new_property)
    db.session.commit()
    
    
   
    
    # return the user email
    return jsonify({"new_property":new_property.property_address , "id":new_property.id})       







# Finally, we round out our CRUD resource with a DELETE method
@properties.route("/properties/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_card(id):
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
    # find the card
    property = Property.query.filter_by(id=property.property_id).first()
    #return an error if the card doesn't exist
    if not property:
        return abort(400, description= "Card does not exist")
    #Delete the card from the database and commit
    db.session.delete(property)
    db.session.commit()
    #return the card in the response
    return jsonify(property_schema.dump(property))