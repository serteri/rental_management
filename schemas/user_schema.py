from main import ma

from marshmallow import fields
from marshmallow.validate import Length


#create the User Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("user_id","user_name","user_email","user_dob","user_password","admin","property")
        # load_only = ['user_password', 'admin']
        # user_id = fields.Int(dump_only =True)
        # user_name = fields.Str()
        # user_email = fields.Str(required= True)
        # user_dob = fields.Date()
        # user_password = fields.Str(required= True)
        # admin = fields.Boolean()
        #set the password's length to a minimum of 6 characters
    user_password = ma.String(validate=Length(min=6))
    property = fields.List(fields.Nested("PropertySchema"))

#single card schema, when one card needs to be retrieved
user_schema = UserSchema()
#multiple card schema, when many cards need to be retrieved
users_schema = UserSchema(many=True)