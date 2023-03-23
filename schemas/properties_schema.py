from main import ma
from marshmallow import fields

class PropertySchema(ma.Schema):
    class Meta:
     ordered = True
        # Fields to expose
     fields = ("property_id", "property_address", "property_postcode", "property_suburb","property_state","users","comments","ranks")
    users=fields.Nested("UserSchema",only=("user_name","user_email","user_id",))
    comments= fields.List(fields.Nested("CommentSchema"))
    ranks= fields.List(fields.Nested("RankSchema"))
#single card schema, when one card needs to be retrieved
property_schema = PropertySchema()
#multiple card schema, when many cards need to be retrieved
properties_schema =PropertySchema(many=True)

