from main import ma
from marshmallow import fields

class CommentSchema(ma.Schema):
    class Meta:
     ordered = True
        # Fields to expose
     fields = ("comment_id","comment","users")
    users= fields.Nested("UserSchema",only=("user_email","user_name",))
     
comment_schema = CommentSchema()

comments_schema = CommentSchema(many=True)    