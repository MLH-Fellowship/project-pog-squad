from asyncio import constants
import os  # Import operating system tools
from flask import Flask, render_template, request, url_for  # Import flask library and associated tools
from dotenv import load_dotenv

# NOTE: url_for is linked to the functions below and returns the corresponding index; preferred over hardcoding links

load_dotenv()  # Loads .env file
app = Flask(__name__)


@app.route("/victor")
@app.route("/victor/")
def victor():
    return render_template("/victor/home.html", img="victor.jpeg",title="Victor", url=os.getenv("URL"))

@app.route("/victor/hobbies")
@app.route("/victor/hobbies/")
def victor_hobbies():
    return render_template("/victor/hobbies.html", img="victor.jpeg",title="Victor", url=os.getenv("URL"))


@app.route("/talike")
@app.route("/talike/")
def talike():
    return render_template("/talike/home.html", img="talike.jpg",title="Talike", url=os.getenv("URL"))

@app.route("/talike/hobbies")
@app.route("/talike/hobbies/")
def talike_hobbies():
    return render_template("/talike/hobbies.html", img="talike.jpg", title="Talike", url=os.getenv("URL"))

if __name__ == "__main__":
    app.run(debug=True)