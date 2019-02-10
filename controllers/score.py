from app import app
from flask import render_template, request, session
from helpers import get_score, clear_score

@app.route('/score/')
def score():

    data = {
        "score" : session['num_correct'],
        "total" : session['num_total'],
        "username" : session['username']
    }

    return render_template("score.html", **data)
