from app import app
from flask import render_template, session, request
from helpers import clear_score

@app.route('/')
def home():
    # always starts game with a blank score
    clear_score()

    # always starts game with no initial username
    if 'username' in session:
        del session['username']

    data = {
    }

    return render_template("home.html", **data)
