from flask import Flask , jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow.validate import Length
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager



ma = Marshmallow()
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    
    app = Flask(__name__)


# configuring our app:
    app.config.from_object("config.app_config")


    app.config["JWT_SECRET_KEY"] = "Backend best end"    
    # creating our database object! This allows us to use our ORM
    db.init_app(app)
    
    # creating our marshmallow object! This allows us to use schemas
    ma.init_app(app)
    
     #creating the jwt and bcrypt objects! this allows us to use authentication
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    # import the controllers and activate the blueprints
    from controller import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)
        
    from commands import db_commands
    app.register_blueprint(db_commands) 
    
    @app.route("/")
    def hello():
            return "Hello World!"
    return app