from flask import Blueprint, jsonify, request,abort
from main import db
from models.property import Property
from models.users import User
from models.comments import Comment
from models.ranks import Rank
from schemas.properties_schema import properties_schema,property_schema
from schemas.comments_schema import comments_schema, comment_schema
from schemas.ranks_schema import ranks_schema,rank_schema
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
   
    u_id = get_jwt_identity()
    new_property =Property()
    new_property.property_address = property_fields["property_address"]
                                     
     #Add tpost code attribute
    new_property.property_postcode = property_fields["property_postcode"]
    
    new_property.property_suburb = property_fields["property_suburb"]
    new_property.property_state = property_fields["property_state"]
    new_property.u_id = u_id
    #add to the database and commit
    db.session.add(new_property)
    db.session.commit()
    
    # return the user email
    return jsonify({"new_property":new_property.property_address , "id":new_property.u_id})       


  #The Put route endpoint
@properties.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_property(id):
     property_fields = property_schema.load(request.json)
     
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
     #return an errot if the property deos not exist
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
    property = Property.query.filter_by(property_id=id).first()
    #return an error if the card doesn't exist
    if not property:
        return abort(400, description= "Property does not exist")
    #Delete the card from the database and commit
    db.session.delete(property)
    db.session.commit()
    #return the card in the response
    return jsonify(property_schema.dump(property))



@properties.route("/search", methods=["GET"])
def search_properties():
     
     property_list = Property.query.filter_by(property_postcode = request.args.get('property_postcode'))
     
     result = properties_schema.dump(property_list)
     #return the data in JSON format
     return jsonify(result)

@properties.route("/property/<int:id>/comments",methods=["POST"])
#logged in user required
@jwt_required()
# Property id required to assign the comment of a property
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
     

@properties.route("/property/<int:id>/comments",methods=["DELETE"])
#logged in user required
@jwt_required()
# Property id required to assign the comment of a property
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

     
     
    comment= Comment.query.filter_by(pro_id=id).first()
    if not comment:
          return abort(400, description= "Comment does not exist") 
    db.session.delete(comment)
    db.session.commit()
     
     #return the property in the response
    return jsonify(property_schema.dump(comment))
     
@properties.route("/property/<int:id>/comments",methods=["PUT"])
#logged in user required
@jwt_required()
# Property id required to assign the comment of a property
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
     
@properties.route("/property/<int:id>/ranks",methods=["POST"])
#logged in user required
@jwt_required()
# Property id required to assign the comment of a property
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
     
     #use that id to set the qwnership of the property
     
     new_rank.u_id = user_id
     
     #add to the database and commit
     
     db.session.add(new_rank)
     db.session.commit()
     
     #return the card in the response
     return jsonify(property_schema.dump(property))



@properties.route("/property/<int:id>/ranks",methods=["DELETE"])
#logged in user required
@jwt_required()
# Property id required to assign the comment of a property
def delete_rank(id):
    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
#     if not user.admin:
#         return abort(401, description="Unauthorised user")
    # find the card
    property = Property.query.filter_by(property_id=id).first()
    #return an error if the card doesn't exist
    if not property:
        return abort(400, description= "Property does not exist")

     
     
    rank= Rank.query.filter_by(prop_id=id).first()
    if not rank:
          return abort(400, description= "Rank does not exist") 
    db.session.delete(rank)
    db.session.commit()
     
     #return the card in the response
    return jsonify(property_schema.dump(rank))

@properties.route("/property/<int:id>/ranks",methods=["PUT"])
#logged in user required
@jwt_required()
# Property id required to assign the comment of a property
def update_rank(id):
     
      #create a new comment
    rank_fields = rank_schema.load(request.json)
    
    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
#     if not user.admin:
#         return abort(401, description="Unauthorised user")
#     # find the card
    property = Property.query.filter_by(property_id=id).first()
    #return an error if the card doesn't exist
    if not property:
        return abort(400, description= "Property does not exist")

     
     
    rank= Rank.query.filter_by(prop_id=id).first()
    if not rank:
          return abort(400, description= "Rank does not exist")

    rank.rank= rank_fields["rank"]
    db.session.commit()
     
     #return the card in the response
    return jsonify(property_schema.dump(rank))