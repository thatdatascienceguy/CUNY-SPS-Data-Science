#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:25:33 2019

@author: Jonathan Hernandez
File that reads in the training titanic data and does the following in order:
    1. Reads in the data
    2. drops columns not needed in this case 
        'Survived', 'Name', 'Ticket', 'PassengerId', 'Cabin'
        Besides Survived the dependent variable, the other 4 I felt were not 
        needed to determine or classify if a person survived the titanic crash
        or not.
    3. Maps gender values from M/F to 0's and 1's so we can train and fit a 
    random forest classifier that will classify if a passenger died (0) or
    survived (0)
    4. Replaces missing Embarked values with the most common Embarked status and
    maps Embarked values from 0,1,2 and so on.
    5. Replaces missing ages by the median of the ages in the training set.
    6. Splits the training data into a training/test set to test and fit our
    model.
    7. Trains a random forest classifier model and then outputs a plot showing
    which features are most important and makes predictions on the test set.
    8. Writes the accuracy of the model to a text file and saves the 
    Random Forest model in a .pkl where it will be used to make predictions on 
    the test.csv dataset.
"""

import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics

"""Read in the dataset in question"""
def read_data(training_dataset):
    data = pd.read_csv(training_dataset)
    return data

"""Split the training set into a 70/30 rule
That is, 70 percent of the data is used to train a Random Forest model and 
30% is used to test it out
"""
def titanic_train_data_split(X, y, split_percentage=0.7):
    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size = split_percentage, random_state=200)
    return X_train, X_test, y_train, y_test # return the split data
    

"""Function to drop specified columns and returns
the dataset excluding the dropped columns"""
def drop_columns(dataset, list_of_cols_drop):
    if list_of_cols_drop == []:
        return dataset # nothing to do; simply return it
    else:
        data_X = dataset.drop(columns=list_of_cols_drop, axis=1)
        # new dataset that omits if any columns to drop
        return data_X

"""Transform the gender values from Female/Male to 0 and 1"""
def gender_mapping(dataset):
    # convert male and female to 0 and 1 respectively for using a 
    # random forest classifier
    gender_encoder = LabelEncoder()
    dataset['Sex'] = gender_encoder.fit_transform(dataset['Sex'])
    return dataset

"""Replace missing Embarked values and map them to integers"""
def embarked_status_mapping(dataset):
    # looking at the Embarked column there are 2 missing values, let's first
    # replace them with the most common Embarked status
    dataset['Embarked'] = dataset['Embarked'].fillna(
            dataset['Embarked'].mode()[0])
    
    # convert each value of Embarked as numbers 0, 1, and 2 for using
    # the random forest model
    dataset['Embarked'] = pd.factorize(dataset['Embarked'])[0]
    return dataset

"""Replace missing ages with the median of ages"""    
def impute_missing_age(dataset, ages):
    ages.fillna(ages.median(), inplace = True)
    #print(sum(ages.isnull()))
    dataset['Age'] = ages
    return dataset

"""Plot Feature importance"""
def plot_feature_imp(xlabel, ylabel, title, data, model):
    feature_imp = pd.Series(model.feature_importances_,index=data.columns)
    feature_imp = feature_imp.sort_values(ascending=False)
    sns.barplot(x=feature_imp, y=feature_imp.index)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()
    
if "__main__" == __name__:
    train_titanic = pd.read_csv('train.csv') # read in the training data
    train_survived = train_titanic['Survived'] # dependent variable
    
    # let's see how many missing values are in each column
    train_titanic.isnull().sum()
    
    # Drop the columns belowa as these factors we will not use
    # in our randomforest model
    cols_drop = ['Survived', 'Name', 'Ticket', 'PassengerId', 'Cabin']
    train_titanic = drop_columns(train_titanic, cols_drop)
    
    # Age and Embarked will have to be imputed    
    # creatie mapped gender values from strings
    train_titanic = gender_mapping(train_titanic)
    
    # replace Embarked strings with 0, 1, 2, ...
    train_titanic = embarked_status_mapping(train_titanic)
    # replace missing Age values with their median
    train_titanic = impute_missing_age(train_titanic, train_titanic['Age'])
    
    # split the training and test data
    train_X, test_X, train_y, test_y = titanic_train_data_split(train_titanic,
                                                                train_survived)
    
    rfc = RandomForestClassifier(n_estimators=100)
    # fit a Random forest classifier on the training portion of the training
    # dataset
    rfc.fit(train_X, train_y)    
    
    # feature plot
    plot_feature_imp('Feature Importance Score',
                     'Features',
                     'Visualizing Important Features',
                     train_X, rfc)
    
    # make predictions on the test_X dataset and see how accurate our model is
    pred_y = rfc.predict(test_X)
    accuracy_file = open("RandomForestClassifier.txt", "w")
    accuracy_file.write("Accuracy: %s" % (metrics.accuracy_score(test_y, pred_y)))
    accuracy_file.close()
    
    # save into a pickle (pkl file)
    random_forest_model_filename = 'DATA622_titanic_random_forest_model.pkl'
    random_forest_model_pkl = open(random_forest_model_filename, 'wb')
    pickle.dump(rfc, random_forest_model_pkl)
    random_forest_model_pkl.close()
    # save into a pickle (pkl file)