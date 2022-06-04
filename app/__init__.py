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
    v_titles = ["PE Fellow", "Software Engineer", "Intern"]
    v_dates = ["May 2022 - Present", "January 2017 - December 2018", "May 2016 - August 2016"]
    v_locations = ["MLH", "Blue People", "Google"]
    return render_template('victor.html', title="Victor B.", url=os.getenv("URL"),
        titles=v_titles, dates=v_dates, locations=v_locations)

@app.route('/Talike')
def talike_page():
    # NOTE: Using dictionary for first two lists did not work
    t_titles = ["PE Fellow", "Intern", "Seasonal Aide"]
    t_dates = ["May 2022 - Present", "January 2022", "June 2021 - August 2021"]
    t_locations = ["MLH", "UNICC", "NYC Parks"]
    return render_template('talike.html', title="Talike B.", url=os.getenv("URL"),
        titles=t_titles, dates=t_dates, locations=t_locations)

# Branch to run site
if __name__ == "__main__":
    app.run(debug=True)
