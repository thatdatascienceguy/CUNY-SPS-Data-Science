# -*- coding: utf-8 -*-
"""
@author: jonboy1987
"""

import pandas as pd
from Tkinter import Tk
from tkFileDialog import askopenfilename
import os
import re
import warnings

def getEPA_HTTP_data():
    """Reads in the image, uses a file dialog to point to the file"""
    Tk().withdraw()
    filename = askopenfilename()
    
    # Read in the dataset
    EPA_HTTP_data = pd.read_csv(filename, sep='delimeter', header=None)
    return EPA_HTTP_data

def clean_and_tidy_data(dataset):
    """This function will clean up the dataset by combining columns,
    deleting un-needed columns from using sep='delimeter', concatenating data,
    """
    
    # hostname/IP address can be found by extracting the beginning of the line
    # until a " " is reached    
    hostname = dataset[0].str.extract('^([^\s]+)')
    
    # the date/time can be extracted by getting all characters in the []
    time = dataset[0].str.extract('\[(.*?)\]')
    
    # request can be obtained by getting everything within outer " "
    request = dataset[0].str.extract(r'"(.*?)"')
    
    # HTTP code
    HTTP_reply_code = dataset[0].map(lambda x: re.search('\"\s[0-9]{3}', x).
    group(0).replace('" ', ""))
    
    # bytes can be extracted by getting everything after the last " "
    bytes_in_reply = dataset[0].map(lambda x: re.search("([0-9]+$)|(-$)", x).group(0))
    
    # Form the newly clean/tidy dataset
    EPA_HTTP = pd.DataFrame({'hostname': hostname, 'time': time,
                             'request': request, 'HTTP_reply_code': HTTP_reply_code,
                             'bytes': bytes_in_reply})
                                                  
    # lets reorder the columns so it appears as it was in the original dataset
    # instead of having them alphabetically
    cols = ['hostname', 'time', 'request', 'HTTP_reply_code', 'bytes']
    return EPA_HTTP[cols]
    
def get_hostname_with_most_req(dataset):
    """ Returns the hostname or IP address that had the most requests in a day
    """
    return dataset.hostname.value_counts().head(1)

def get_hostname_most_bytes_rec(dataset):
    """ Returns the hostname or IP address that received the most bytes"""
    # remove rows where no http reply was done (a 0 or -)
    tmp = dataset[(dataset.bytes != '0') & (dataset.bytes != '-')]
    # convert to int (the bytes)
    tmp.bytes = tmp.bytes.astype(int)
    # return the hostname/ip with the most bytes received
    return tmp.groupby('hostname')['bytes'].sum().sort_values(ascending = False).head(1)
    
def most_gif_image_downloaded(dataset):
    """ Get the name of the .gif image that was downloaded the most from dataset
    """
    # filter out the requests with only .GET in them (get requests)
    has_GET = EPA_HTTP_dataset.request.str.contains("GET")
    
    #  GET_req contains the requests that were GET (download)
    GET_req = EPA_HTTP_dataset.request[has_GET]
    
    # Now get the GET requests where .gif images were being download
    has_GET_gif = GET_req.str.contains(".gif")
    
    # GET_req_gif contains all requests that downloaded .gif files
    GET_req_gif = GET_req[has_GET_gif]
    
    # remove the "GET " and " HTTP/1.0"
    GET_req_gif = GET_req_gif.str.replace("GET ", "")
    GET_req_gif = GET_req_gif.str.replace(" HTTP/1.0", "")
    # use os.path.basename to get the name of the .gif file
    GET_req_gif = GET_req_gif.map(lambda x: os.path.basename(x))
    
    # finally show the gif image that has been requestd the most
    return EPA_HTTP_dataset.request.groupby(GET_req_gif).count().sort_values(ascending = False).head(1)   

def HTTP_reply_codes_not_200(dataset):
    """ Get the list of HTTP reply codes not 200 """
    non_200_HTTP_code = EPA_HTTP_dataset[EPA_HTTP_dataset.HTTP_reply_code != "200"].HTTP_reply_code
    return list(non_200_HTTP_code.unique())

def busiest_hour_requests(dataset):
    """ Gets the hour the server received the most requests"""
    # the dataset is split into two days so make two variables for each day
    day1 = EPA_HTTP_dataset.time.str.contains("29:[0-9]{2}:[0-9]{2}:[0-9]{2}")
    day2 = EPA_HTTP_dataset.time.str.contains("30:[0-9]{2}:[0-9]{2}:[0-9]{2}")
    
    # get the day1, day2 hours 00-23
    day1_hours = EPA_HTTP_dataset.time[day1]
    day2_hours = EPA_HTTP_dataset.time[day2]
    
    # extract the hour on each day
    day2_hours = day2_hours.map(lambda y: y[3:5])
    day1_hours = day1_hours.map(lambda x: x[3:5])
    
    # group the hours
    day2_hours_counts = day2_hours.groupby(day2_hours.values).count()
    day1_hours_counts = day1_hours.groupby(day1_hours.values).count()
    
    # compare which day had the hour with the most requests
    
    if day1_hours_counts.max() < day2_hours_counts.max():
        return day2_hours_counts.sort_values().tail(1)
    else:
        return day1_hours_counts.sort_values().tail(1)

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    EPA_HTTP_dataset = getEPA_HTTP_data()
    
    print EPA_HTTP_dataset.head()
    
    # A properly clean dataset
    print "Cleaned Dataset:"
    EPA_HTTP_dataset = clean_and_tidy_data(EPA_HTTP_dataset)
    print EPA_HTTP_dataset.head(10)
    print
    
    print "Hostname or IP address with the most requests and how many:"
    print get_hostname_with_most_req(EPA_HTTP_dataset)
    print
    
    print "Hostname or IP address that received the most bytes and how many:"
    print get_hostname_most_bytes_rec(EPA_HTTP_dataset)
    print
    
    print "Most common .gif image requested and how many times:"
    print most_gif_image_downloaded(EPA_HTTP_dataset)
    print
    
    print "List of HTTP reply codes sent besides 200:"
    print HTTP_reply_codes_not_200(EPA_HTTP_dataset)
    print
    
    print "hour segment that had the most server requests:"
    print busiest_hour_requests(EPA_HTTP_dataset)
    print
    
    
    
    