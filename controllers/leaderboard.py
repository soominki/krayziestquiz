from firebase import firebase
from app import app
from flask import render_template, request, session
import urllib2
from bs4 import BeautifulSoup
from score import *
from home import *


@app.route('/leaderboard/')
def leaderboard():
	# imported firebase database where all the scores and usernames are stored
	db_cursor = firebase.FirebaseApplication('https://krayziest-quiz.firebaseio.com', None)
	players_dictionary = db_cursor.get('/players', None)
	# created a sorted list of player usernames and a sorted list of corresponding scores
	player_names = players_dictionary.keys()
	sorted_players = sorted(player_names, key=lambda x:players_dictionary[x], reverse=True)
	list_scores = []
	for player in sorted_players:
		list_scores.append(players_dictionary[player])

	data = {
		"players_dictionary" : players_dictionary
	}

	# adds sorted names to data dictionary
	for x in range(0, len(sorted_players)):
		data["name{0}".format(x)] = sorted_players[x]
	# adds sorted scores to data dictionary
	for x in range(0, len(sorted_players)):
		data["score{0}".format(x)] = players_dictionary[sorted_players[x]]

	return render_template("leaderboard.html", **data)

# leaderboard_page = 'http://localhost:5000/leaderboard/'
# page = urllib2.urlopen(leaderboard_page)
# soup = BeautifulSoup(page, 'html.parser')
# name_player = soup.find('h5', attrs={'class':'names'})
# names = name.player.text.strip()
# print names

# for key, value in players_dictionary.iteritems():
# 	list = [key, value]
# 	name = key
# 	score = value
# 	list.append(name)
# 	list.append(score)
# 	list_names.append(list)
# print(list_names[0])
