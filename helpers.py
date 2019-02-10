# Add more import statements as you need them!
from utility import get_four_choices
from flask import session
import billboard

"""
Our dictionary to hold which genres we are giving to our users. Play around with
this dictionary to see how the starter code changes on index.html. The keys
represent the names as they appear on the website, and the values represent the
chart IDs for Billboard to use.

TODO: Add at least two more genres to this dictionary. Information on how to find
      more Billboard chart IDs is on the Billboard library documentation, as
      linked on the core page of the spec. Make sure you only choose charts that
      contain SONGS (not artists, albums, etc.).
"""
GENRES_LIST = {
    "Current Pop Hits": "hot-100",
    "Dance Club Hits": "dance-club-play-songs",
    "Country Classics": "greatest-country-songs",
    "Holiday Hits": "holiday-streaming-songs",
    "Top K-POP ": "billboard-korea-k-pop-100"
}

"""
REQUIRES: a valid chart name that corresponds to a chart name on Billboard
MODIFIES: nothing
EFFECTS: chooses four random songs from the valid Billboard chart and returns
         result in a list. Uses get_four_choices() and the Billboard library.
         Remember: if you want to use a library in Python, what must we put at
         the top of the file to access its member functions?
"""
def get_four_songs(chart_name):
    my_list1 = billboard.ChartData(chart_name)
    choice = get_four_choices(my_list1)
    my_list2 = [my_list1[choice[0]], my_list1[choice[1]], my_list1[choice[2]], my_list1[choice[3]]]
    return my_list2

"""
REQUIRES: nothing
MODIFIES: nothing
EFFECTS: returns a string with the score to print
"""
def get_score():
    return session['num_correct']

"""
REQUIRES: nothing
MODIFIES: num_correct, num_total in session
EFFECTS: sets the num_correct and num_total to 0
"""
def clear_score():
    session['num_correct'] = 0
    session['num_total'] = 0
