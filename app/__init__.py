from asyncio import constants # ?
import os  # Import operating system tools
from flask import Flask, render_template, request, url_for  # Import flask library and associated tools
from dotenv import load_dotenv # ?

# NOTE: url_for is linked to the functions below and returns the corresponding index; preferred over hardcoding links

"""
TODO:
- merge Hobbies page into Home page
- create three main pages to navigate to: MLH Fellowship, About Me, Contact
"""

load_dotenv() # Loads .env file
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", img="Talike.jpg", url=os.getenv("URL"))

@app.route("/about-me/")
def about_me():
    return render_template("about_me.html", img="Talike.jpg", url=os.getenv("URL"))

@app.route("/contact/")
def contact():
    return render_template("contact.html", img="Talike.jpg", url=os.getenv("URL"))

if __name__ == "__main__":
    app.run(debug=True)