#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:43:58 2019

@author: Jonathan Hernandez
"""

import kaggle
import re

# competition[0] get the desired competition name which we can use
# kaggle.api.competition_download_file() to get the training and test data

def download_train_data(kaggle_download_url):
    # training dataset
    # competition name lookup (use regex to find the name of the competition)
    competition_name = re.search(r'(?<=\/c\/)(.*)(?=\/download)',
                                 kaggle_download_url)
    train_titanic = kaggle.api.competition_download_file(competition_name[0],
                                                         file_name='train.csv')
    return train_titanic

def download_test_data(kaggle_download_url):    
    # test dataset
    # competition name lookup (use regex to find the name of the competition)
    competition_name = re.search(r'(?<=\/c\/)(.*)(?=\/download)',
                                 kaggle_download_url)
    test_titanic = kaggle.api.competition_download_file(competition_name[0],
                                                        file_name='test.csv')
    return test_titanic

if __name__ == "__main__":
    # authenticate using the kaggle.json file containing username/API token
    kaggle.api.authenticate()

    # get url's of training and test data of kaggle's titanic competition
    kaggle_url = 'https://www.kaggle.com/c/titanic/download'
    titanic_train = download_train_data(kaggle_url)
    titanic_test = download_test_data(kaggle_url)