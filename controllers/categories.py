# You might need to add more of these import statements as you implement your controllers.
from app import app
from flask import render_template, session, request
from helpers import GENRES_LIST, clear_score

@app.route('/categories')
def categories():
    #code to prevent route error with username from home vs other pages
    sample_username = request.args.get('username')
    if sample_username != None:
        session['username'] = request.args.get('username')

    data = {
        "username" : session['username'],
        "genres": GENRES_LIST,
        "score" : session['num_correct'],
        "total" : session['num_total'],
        "username" : session['username']
    }

    return render_template("categories.html", **data)
