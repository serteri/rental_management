from main import db

class Property(db.Model):
    #define the table name for the db
    
    __tablename__ = "properties"
    
    #Set the primary key
    
    property_id = db.Column(db.Integer,primary_key=True)
    
    #Add rest of the attributes
    
    property_address = db.Column(db.String(),nullable = False)
    property_postcode = db.Column(db.String(),nullable = False)
    property_suburb = db.Column(db.String(),nullable = False)
    property_state = db.Column(db.String(),nullable = False)   
    
    id = db.Column(db.Integer,db.ForeignKey("users.user_id"),nullable =False)
   