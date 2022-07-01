from asyncio import constants
from datetime import datetime
import os
from unicodedata import name  # Import operating system tools
from flask import Flask, render_template, request, url_for  # Import flask library and associated tools
from dotenv import load_dotenv
from peewee import *
# NOTE: url_for is linked to the functions below and returns the corresponding index; preferred over hardcoding links

from playhouse.shortcuts import model_to_dict

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os. getenv( "MYSQL _USER" ), password=os. getenv ( "MYSQL_PASSWORD" ) , host=os.getenv( "MYSQL_HOST" ), port=3306)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.now())
    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

load_dotenv("../.env")  # Loads .env file
app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("/home.html", img="Victor.jpeg",title="Victor", url=os.getenv("URL"))

@app.route("/hobbies")
def hobbies():
    return render_template("/hobbies.html", img="Victor.jpeg",title="Victor", url=os.getenv("URL"))

@app.route("/timeline")
def timelines():
    return render_template("/timeline.html", img="Victor.jpeg",title="Victor", url=os.getenv("URL"))


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    name = request.form["name"]
    email = request.form["email"]
    content = request.form["content"]
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)    

@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in 
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
