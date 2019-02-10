from firebase import firebase
from app import app
from flask import render_template, request, session, redirect, url_for
from utility import get_preview_url
from question import *
from helpers import get_score, clear_score
from bs4 import BeautifulSoup
import requests
from score import *

@app.route('/answer/')
def answer():
    genre = request.args['genre']
    if 'song_guess' in request.args:
        # use request.args to access hidden elements from question.html
        user_option = request.args['song_guess']
        answer_title = request.args['correct_title']
        answer_artist = request.args['correct_artist']
        answer_song = request.args['correct_song']
        # use if-else to increment score appropriately
        if user_option == answer_song:
            session['num_correct'] += 1
            session['num_total'] += 1
        else:
            session['num_correct'] = session['num_correct']
            session['num_total'] += 1
    else:
        return redirect(url_for("question", genre=genre))

    #updating database with current score
    db_cursor = firebase.FirebaseApplication('https://krayziest-quiz.firebaseio.com', None)
    players_dictionary = db_cursor.get('/players', None)
    # only adds score to leaderboard if higher than previous high score
    username = session['username']
    if username in players_dictionary:
        if session['num_correct'] > players_dictionary[session['username']]:
			db_cursor.put('/players', session['username'], session['num_correct'])
    elif 'num_correct' and 'num_total' in session:
		db_cursor.put('/players', session['username'], session['num_correct'])

	#WebScraping: Used BeautifulSoup to scrape href from <a> tags to create a url
	#that corresponded to the correct answer.
    # source = https://github.com/munchycool/forthelulz/tree/master/youtube_example
    scrape_url="https://www.youtube.com"
    search_url="/results?search_query="
    video_title = answer_title
    new_video_title = video_title.replace(" ", "+")
    sb_url = scrape_url + search_url + new_video_title
    sb_get = requests.get(sb_url)
    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
    yt_links = soupeddata.find_all("a")
    yt_final = ""
    for x in yt_links:
        yt_href = x.get("href")
        if yt_href.startswith("/watch"):
            yt_final = yt_href[9:]
            break

    data = {
        "song_choice" : user_option,
        "title" : answer_title,
        "artist" : answer_artist,
        "right_answer" : answer_song,
        "same_genre" : genre,
        "score" : session['num_correct'],
        "total" : session['num_total'],
        "username" : session['username'],
        "link" : yt_final
    }

    return render_template("answer.html", **data)
