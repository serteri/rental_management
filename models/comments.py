from main import db

class Comment(db.Model):
    __tablename__ = "comments"
    
    comment_id = db.Column(db.Integer,primary_key =True)
    
    comment = db.Column(db.String(),nullable = False)
    
    #two foreign keys
    
    us_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable =False)
    pro_id = db.Column(db.Integer,db.ForeignKey("properties.property_id"),nullable= False)
                            
                            