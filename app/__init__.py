from asyncio import constants
import os  # Import operating system tools
from flask import Flask, render_template, request, url_for  # Import flask library and associated tools
from dotenv import load_dotenv # ?

# NOTE: url_for is linked to the functions below and returns the corresponding index; preferred over hardcoding links

load_dotenv()  # Loads .env file
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", img="Talike.jpg", title="Talike", url=os.getenv("URL"))

@app.route("/hobbies/")
def hobbies():
    return render_template("hobbies.html", img="Talike.jpg", title="Talike", url=os.getenv("URL"))

if __name__ == "__main__":
    app.run(debug=True)