from main import db

class Comment(db.Model):
    __tablename__ = "COMMENTS"
    
    comment_id = db.Column(db.Integer,primary_key =True)
    
    comment = db.Column(db.String(),nullable = False)
    
    
    
    