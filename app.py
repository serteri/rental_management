from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#set the database URI via SQLAclhemy
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql+psycopg2://serter:Altay2205@localhost5432/rental_management"

@app.route("/")
def hello():
  return "Hello World!"