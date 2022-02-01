from flask import render_template
from app import app

# view
@app.route('/')
def index():

    title = "Welcome to My Flask App"
    return render_template('index.html')