import os  # Import operating system tools
from flask import Flask, render_template, request  # Import flask library and associated tools
from dotenv import load_dotenv

load_dotenv()  # Loads .env file
app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

# Branch to run site
if __name__ == "__main__":
    app.run(debug=True)
