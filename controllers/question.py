from app import app
from flask import render_template, request, session
from helpers import get_four_songs
from utility import get_preview_url
import random

@app.route('/question/')
def question():
    user_option = request.args['genre']
    songs = get_four_songs(user_option)
    # use indexing to choose random song from song list to be answer
    index = random.randint(0, 3)
    audio = get_preview_url(songs[index].title, songs[index].artist)
    # use while loop to make sure audio is available
    while "error" in audio:
        index = random.randint(0, 3)
        audio = get_preview_url(songs[index].title, songs[index].artist)
    answer_url = audio.get("url")
    answer_title = audio.get("title")
    answer_artist = audio.get("artist")

    data = {
        "chart_name" : user_option,
        "song_choices" : songs,
        "audio_track" : answer_url,
        "title_answer" : answer_title,
        "artist_answer" : answer_artist,
        "song_answer" : songs[index],
        "score" : session['num_correct'],
        "total" : session['num_total'],
        "username" : session['username']
    }

    return render_template("question.html", **data)
