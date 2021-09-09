# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:43:11 2018

@author: jonboy1987
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
import nltk
from nltk.tokenize import word_tokenize

# load the data
spambase = pd.read_csv("spambase/spambase.data")

# load attribute names into the spambase dataset
spambase_names = open("spambase/spambase.names", 'r')
attributes = spambase_names.readlines()[33:91]

# extract only the text before the ':' to get each attribute
names = [a[:a.index(':')] for a in attributes]
names.append('spam')

# add the column names
spambase.columns = names

## re-map the 0's and 1's as non-spam and spam respectively
spambase.spam = ['spam' if a == 1 else 'non-spam' for a in spambase.spam]

# Data Visualization
spam_counts = pd.Series(spambase.spam).value_counts()
spam_counts.plot.bar()

# split data into a training/dev-test set
X_train, X_test, y_train, y_test = train_test_split(spambase.iloc[:,0:57],
                                                    spambase['spam'],
                                                    test_size = 0.33,
                                                    random_state=4)

# apply logistic regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test) # predict the y values given the test trainind data
print('Accuracy of logistic regression classifier on test set: ', round(logreg.score(X_test, y_test),3))
## Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test,y_pred))
# Misclassification summary
y_test = np.asarray(y_test)
for i in range(len(y_pred)):
    if (y_pred[i] != y_test[i]):
        print('Email# %-8s Predicted label %-12s true label: %-8s') % (i, y_pred[i], y_test[i])
print

# Apply Naive Bayes Classification
X_train, X_test, y_train, y_test = train_test_split(spambase.iloc[:,0:57],
                                                    spambase['spam'],
                                                    test_size = 0.33,
                                                    random_state=4)
# Naive bayes multi-nominal
NB_model = MultinomialNB()
NB_model.fit(X_train, y_train) 
y_pred = NB_model.predict(X_test)
print('Accuracy of Naive bayes regression classifier on test set: ', round(NB_model.score(X_test, y_test),3))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
# Misclassification summary
y_test = np.asarray(y_test)
for i in range(len(y_pred)):
    if (y_pred[i] != y_test[i]):
        print('Email# %-8s Predicted label %-12s true label: %-8s') % (i, y_pred[i], y_test[i])
        
"""Write functions to return word frequency, char frequency and run-length of capital letter and 
use that data to predict and classify if spam or not for given email text
"""

def get_word_char_capitalletter_frequencies_for_dataset(email_text):
    # Get the words to search for to compute the statistics to predict for spam/no spam
    data = {}
    words_search_for = [s.replace('word_freq_', '') for s in spambase.columns]
    # get the characters to search for
    words_search_for = [s.replace('char_freq_', '') for s in words_search_for]
    del words_search_for[54:]
    words = word_tokenize(email_text) # split into words
    words_lower = [w.lower() for w in words]
    fdist = nltk.FreqDist(words_lower) # frequency distribution
    n_words = len(words_lower)
    frequency_summary = [(freq, round(fdist[freq]/float(n_words), 2)) for freq in fdist]
    for w in words_search_for:
        if w in [x[0] for x in frequency_summary]:
            # retrieve the frequency of the found word
            f = [x[0] for x in frequency_summary].index(w)
            if len(w) == 1:
                data['char_freq_' + w] = [frequency_summary[f][1]] # append to the data
            else:
                data['word_freq_' + w] = [frequency_summary[f][1]]
        else: # if not found set data[w] = 0
            if len(w) == 1:
                data['char_freq_' + w] = [0]
            else:
                data['word_freq_' + w] = [0]
    
    # Get total capital letters in email_text
    data['capital_run_length_total'] = sum(1 for s in email_text if s.isupper())
    
    # now get consecutive capital letters; compute the average and longest run
    ctr = 0
    l = []
    for c in email_text:
        if c.isupper():
            ctr = ctr +1
        else:
            l.append(ctr)
            ctr = 0
    
    data['capital_run_length_longest'] = max(l)
    data['capital_run_length_average'] = np.mean(l)
    
    return pd.DataFrame.from_dict(data)
    
print get_word_char_capitalletter_frequencies_for_dataset("It has come to our attention [ [ that you may be entitled to an undisclosed amount of unclaimed funds funds funds FUNDS.")
    