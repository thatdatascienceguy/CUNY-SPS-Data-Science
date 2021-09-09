#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:07:32 2019

@author: Jonathan Hernandez

Reads in the test.csv dataset of the titanic data and uses the Random Forest
Model pickle file to make predictions on the test.csv and writes to a csv file
showing which passenger (by ID) survived or not.
"""

# With our random forest model as a .pkl extension, let's test it out on the 
# test titanic dataset from kaggle.

import pickle
import pandas as pd
from train_model import gender_mapping
from train_model import embarked_status_mapping
from train_model import impute_missing_age

# load the dataset
test_titanic = pd.read_csv('test.csv')

# load the pickle (.pkl) file containing our RandomForestModel
pickle_file = open('DATA622_titanic_random_forest_model.pkl', 'rb')
rfc_model = pickle.load(pickle_file)
pickle_file.close()

# Just as we had to do some data cleaning and imputation in the training model
# the same applies for the test_titanic dataset

cols_drop = ['Name', 'Ticket', 'PassengerId', 'Cabin']
test_titanic = test_titanic.drop(cols_drop, axis=1)

# use the gender mapping and embarked mapping in helping in making predictions
test_titanic = gender_mapping(test_titanic)
# replace Embarked strings with 0, 1, 2, ...
test_titanic = embarked_status_mapping(test_titanic)

# impute the ages as well like we did for the training data
test_titanic = impute_missing_age(test_titanic, test_titanic['Age'])
test_titanic['Fare'].fillna(test_titanic['Fare'].median(), inplace = True)

# Should return no empty values at this point
print(test_titanic.isnull().sum())
# also a missing value in the Fare column, replace the missing value with the
# median of the Fare values
results = pd.DataFrame({
        'PassengerID': list(range(892,1310)),
        'Survived': rfc_model.predict(test_titanic)})

# write the predictions to a csv file
results.to_csv('titanic_results.csv')


