# -*- coding: utf-8 -*-
"""
@author: jonboy1987
"""
import networkx as nx
import pandas as pd
from Tkinter import Tk
from tkFileDialog import askopenfilename

""" Now as the GiantBomb API can't get user information like location and who follows who,
    Scraping the website manually will have to do
    Getting people <username> is following:
        https://www.giantbomb.com/profile/<username>/following/?filter=users
    Getting followers of <username>:
        https://www.giantbomb.com/profile/<username>/follower/
    Also to make this easier I will only use a subset of the followers,following for each user
    (scraping only the first page of results)
        """
def make_dataset_and_social_network_graph(reviewers):
    G = nx.DiGraph() # empty directed graph
    for r in reviewers: # initlalize graph nodes only
        G.add_node(r)
        
    for user in reviewers:
        following_url = 'https://www.giantbomb.com/profile/' + user + '/following/?filter=users'
        # about me url parsing
        following_df = pd.read_html(following_url, attrs = {"class": "table"})
        following_df[0].columns = ['user', 'type'] # column name change
        following_membership = following_df[0]['user'].isin(reviewers) # check who is following who 
        print following_df[0]['user'][following_membership]
        
        followers_url = 'https://www.giantbomb.com/profile/' + user + '/follower'
        followers_df = pd.read_html(followers_url, attrs = {"class": "table"})
        
        followers_df[0].columns = ['user', 'type']
        followers_membership = followers_df[0]['user'].isin(reviewers)
        print followers_df[0]['user'][followers_membership]
       
       
       # manually put in following edges for Asura's Wrath users
       
        
if __name__ == "__main__":
    print "Getting user information and friends/followers and creating the network graph"
    Tk().withdraw()
    filename = askopenfilename()
    users = pd.read_csv(filename, header = None)
    make_dataset_and_social_network_graph(users[1])
    
    # manually adding the edges for Asura's Wrath: