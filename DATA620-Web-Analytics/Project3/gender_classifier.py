# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:23:27 2018

@author: jonboy1987
"""

import pandas as pd
import nltk
from nltk.corpus import names
from nltk.metrics.scores import (precision, recall)
import random
#nltk.download('names') # first time only

# female names usually end in a,i,e and male names are k,o,r,s,t
#return the last letter in a word  
names = ([(name.lower(), 'male') for name in names.words('male.txt')] + 
        [(name.lower(), 'female') for name in names.words('female.txt')])
        
random.shuffle(names)

# use suffixes more than prefixes
def gender_feature_custom(name):
    return {'suffix2': name[-2:],
            'suffix3': name[-3:],
            'prefix2': name[0:2],
            'prefix3': name[0:3],
            'length': len(name)}
            
featuresets = [(gender_feature_custom(n), g) for (n,g) in names]
test_set, dev_test_set, train_set = featuresets[:500], featuresets[500:1000], featuresets[1000:]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print "Labels: ", classifier.labels()
print "Most Informative features: "
for feature, value in classifier.most_informative_features():
    print feature, value
print "Accuracy: ", nltk.classify.accuracy(classifier, test_set)

errors = []
for (name, tag) in names:
    guess = classifier.classify(gender_feature_custom(name))
    if guess != tag:
        errors.append((tag, guess, name))
        
for (tag, guess, name) in sorted(errors):
    print 'correct', tag, 'guess', guess, 'name', name