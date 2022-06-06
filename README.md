# MLH Fellowship Orientation Hackathon - Portfolio Website
**Track:** Production Engineering
**Team:** Pog Squad  
**Members:** Victor Bustillos, Talike Bennett

## Description
For this project, we were tasked with creating a portfolio website using the Flask framework and Jinja templates. We were provided a foundation for the project -- consisting of `__init__.py`, `index.html`, and `main.css` -- and added our unique features from there. A custom page was made for each of the team members. For each page, we listed a few aspects of our lives with sections such as About Me, Work Experience, and Education. We linked our Hobbies section to another page that displays images associated with our hobbies. We even made use of Google Maps to embed a map that highlisghts places that we have traveled to.

The Jinja template engine came in handy because it reduced the amount of repeated code we needed to write. The CSS stylesheet also helped with adding visually appealing features to the website pages.

## Setup
1. Before running the website, make sure to install `virtualenv` using PIP. 
```
pip install virtualenv
```
2. Move to the `app` directory and create a virtual environment.
```
cd app
virtualenv env
```
3. Activate the virtual environment. (NOTE: Activation commands may vary.)
```
[WINDOWS]      env\Scripts\activate.bat
[LINUX, MACOS] source env/bin/activate
```
4. While inside of the virtual environment, install `flask` and `python-dotenv` using PIP.
```
pip install flask
pip install python-dotenv
```
5. Run the Python script `__init__.py`.
```
python __init__.py
```

## Tools Used
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![html](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![css](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
