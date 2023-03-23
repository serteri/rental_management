from main import ma
from marshmallow import fields

class RankSchema(ma.Schema):
    class Meta:
     ordered = True
        # Fields to expose
     fields = ("rank_id","rank","users")
    users= fields.Nested("UserSchema",only=("user_email","user_name",))
     
rank_schema = RankSchema()

ranks_schema = RankSchema(many=True) 