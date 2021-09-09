# -*- coding: utf-8 -*-

"""
@author: jonboy1987
"""

import json
import re
import urllib
from bs4 import BeautifulSoup
import networkx as nx
import pandas as pd

def get_GiantBomb_video_game(videogame_name, api_key):
    # query video game unique ID (exact match on the video game)
    url = "https://www.giantbomb.com/api/games/?api_key=" + api_key + "&format=json&filter=name:" + videogame_name + "&field_list=site_detail_url"    
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data
    
def get_video_game_id(videogame_json_data):
    # with the json data scrape through and acquire the unique game id and use
    # now extract unique id from game; this is needed to get the user_reviews
    url_id = videogame_json_data['results'][0]['site_detail_url']
    
    # use regular expressions to get the id of the game
    game_id = re.search('/[0-9]*-[0-9]*/', url_id)
    return game_id.group(0) # extract the first result
    
def get_video_game_releases_ids(game_id, api_key):
    # with giantbomb I discovered; you have to get the game's releases (console's released)
    # then you can access the reviews as not even the reviews are in the json
    # returned by get_GiantBomb_video_game
    # special thanks to the following link:
    # https://www.giantbomb.com/forums/api-developers-3017/q-how-to-query-user-reviews-via-the-api-for-a-game-1454356/
    
    game_releases_url = 'https://giantbomb.com/api/game' + game_id + '?api_key=' + api_key + '&field_list=releases&format=json'
    releases_response = urllib.urlopen(game_releases_url)
    data = json.loads(releases_response.read())
        
    # extract the id for each api_detail_url
    review_id = []
    
    for url in data['results']['releases']:
        review_id.append(re.search('/[0-9]*-[0-9]*/', url['api_detail_url']).group(0))
    
    # strip off '/'
    review_id = map(lambda x: re.sub('/', "", x), review_id)
    return review_id # review_ids will be used to get reviews across systems that this game was released on 

def get_videogame_user_review_users(releaseIDs, api_key):
    # get the users from the user_review from the game releaseID's
    reviewers = []
    for ID in releaseIDs:
        url = 'https://www.giantbomb.com/api/user_reviews/?api_key=' + api_key + '&filter=object:' + ID + '&format=json'
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        if data['results'] == []: # if release had not game reviews skip
            continue
        else:
            for review in data['results']:
                reviewers.append(review['reviewer'])
            
    return reviewers

if __name__ == "__main__":
    print "Please register for a free Giant Bomb account at giantbomb.com"
    print "and register for a free api key for this program to work"
    
    api_key = raw_input('Enter your giantbomb.com api key: ')
    videogame_name = raw_input('Enter exact name of video game: ')
    game_json = get_GiantBomb_video_game(videogame_name, api_key)
    
    # now extract unique id from game; this is needed to
    gameID = get_video_game_id(game_json)
    
    # with game ID, extract the releases id's to get the user_reviews
    reviewID = get_video_game_releases_ids(gameID, api_key)
    
    # show the url of the user_reviews
    reviewers = get_videogame_user_review_users(reviewID, api_key)
    reviewers = pd.Series(reviewers, name="giantbomb_user")
    # filename to use
    outputname = videogame_name + '.csv'
    reviewers.to_csv(path=outputname) # output to csv file; save so it is not needed
    # to query the same game over again