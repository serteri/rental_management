from main import db

class Rank(db.Model):
    __tablename__ = "ranks"
    
    rank_id = db.Column(db.Integer,primary_key =True)
    
    rank = db.Column(db.Integer,nullable = False)
    
    #two foreign keys
    
    u_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable =False)
    prop_id = db.Column(db.Integer,db.ForeignKey("properties.property_id"),nullable= False)
                            