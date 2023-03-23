from main import db

class User(db.Model):
    #define the table name for the db
    
    __tablename__ = "users"
    
    #Set the primary key
    
    user_id = db.Column(db.Integer,primary_key=True)
    
    #Add rest of the attributes
    
    user_name = db.Column(db.String(),unique= True,nullable = False)
    user_email = db.Column(db.String(),unique= True,nullable = False)
    user_dob = db.Column(db.Date(),nullable = False)
    user_password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    
    
    properties = db.relationship("Property",backref="users",cascade="all,delete")
    
    comments = db.relationship(
        "Comment",
        backref="user",
        cascade="all, delete"
    )
    ranks = db.relationship(
        "Rank",
        backref= "user",
        cascade= "all ,delete"
        
    )