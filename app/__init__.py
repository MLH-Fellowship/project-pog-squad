import os  # Import operating system tools
from flask import Flask, render_template, request  # Import flask library and associated tools
from dotenv import load_dotenv

load_dotenv()  # Loads .env file
app = Flask(__name__)

@app.route('/')
def home():
    return "Fix later."

@app.route('/Victor')
def victor_page():
    return render_template('victor.html', title="Victor B.", url=os.getenv("URL"))

@app.route('/Talike')
def talike_page():
    return render_template('talike.html', title="Talike B.", url=os.getenv("URL"))


# Branch to run site
if __name__ == "__main__":
    app.run(debug=True)
