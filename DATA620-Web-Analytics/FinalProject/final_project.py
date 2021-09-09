# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:58:29 2018

@author: jonboy1987
dataset from https://www.kaggle.com/stackoverflow/rquestions
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import nltk
import re
import enchant

# read in the csv files

r_answers = pd.read_csv("rquestions/Answers.csv")
r_questions = pd.read_csv("rquestions/Questions.csv")

""" I want to ask the question for this analysis:

"""
# questions with answers
r_stackoverflow = pd.merge(r_questions, r_answers, left_on="Id", right_on="ParentId",how="inner")
r_stackoverflow = r_stackoverflow.drop("Id_x", axis=1) # Id no longer needed
print r_stackoverflow.shape
print r_stackoverflow.columns
#let's clean up the column names as some of them got suffixed from using
# pd.merge() and also distinguish between the answers and questions

r_stackoverflow.columns = ['Q_OwnerUserId', 'Q_CreationDate', 'Q_Score', 'Title',
                           'Q_Body', 'A_Id', 'A_OwnerUserId', 'A_CreationDate', 'ParentId', 'A_Score',
                           'IsAcceptedAnswer', 'A_Body']

#r_stackoverflow.A_Body = r_stackoverflow.A_Body.replace(r'[^A-Za-z]+', ' ', regex=True)
#
#""" Exploratory Data Analysis """
#
#answers_accepted = pd.Series(r_stackoverflow.IsAcceptedAnswer).value_counts()
#answers_accepted.plot.bar(title = "Tag = R Stackoverflow answers accepted by the SO community")
#
#print answers_accepted
#
## Let's now look at the words in the dataset of answers accepted.
## split dataset into two one with accepted answers and the other not accepted
#answers = r_stackoverflow[["IsAcceptedAnswer", "A_Body"]]
#accepted = answers.loc[answers["IsAcceptedAnswer"] == True]
#notaccepted = answers.loc[answers["IsAcceptedAnswer"] == False]
#
#corpus_accepted = " ".join(accepted.A_Body)
#corpus_accepted = corpus_accepted.decode('utf-8')
#accepted_tokens = nltk.word_tokenize(corpus_accepted) # tokenize the string
#
#corpus_notaccepted = " ".join(notaccepted.A_Body)
#corpus_notaccepted = corpus_notaccepted.decode('utf-8')
#notaccepted_tokens = nltk.word_tokenize(corpus_notaccepted)
#
## normalize the words and sort them
#accepted_words = [w.lower() for w in accepted_tokens]
#notaccepted_words = [w.lower() for w in notaccepted_tokens]
#
#print "Number of words in the accepted group: %d " % (len(accepted_words))
#print
#print "Number of words in the not accepted group: %d " % (len(notaccepted_words))
r_stackoverflow['ParentId'] = r_stackoverflow['ParentId'].apply(str)
r_stackoverflow['A_Id'] = r_stackoverflow['A_Id'].apply(str)

DG = nx.from_pandas_edgelist(r_stackoverflow, 'A_Id', 'ParentId', ['A_Score', 'IsAcceptedAnswer'], create_using = nx.DiGraph())

print DG.has_edge('79709', '79741')
print DG.get_edge_data('79741', '79709')

DG.in_degree('79741')
pd.unique()
d = {}
