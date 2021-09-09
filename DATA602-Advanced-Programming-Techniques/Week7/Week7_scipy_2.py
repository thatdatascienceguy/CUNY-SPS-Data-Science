# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:03:59 2017

@author: jonboy1987

Program that reads in images, converts them to binary, then computes the 
Number of objects and the center of the image.

images used are the circles, objects and peppers png files
"""

from scipy import ndimage
from scipy import misc
import mahotas as mh
from Tkinter import Tk
from tkFileDialog import askopenfilename

def getImage():
    """Reads in the image, uses a file dialog to point to the file"""
    Tk().withdraw()
    filename = askopenfilename()
    # print out image
    img = ndimage.imread(filename)
    return img

def convert2binaryimg(img, threshold):
    """ Convert the image to a black/white (binary) image given a 
    Threshold"""
    # if a certain mumber less than the threshold set to 0 otherwise
    # set to 1 meaning black
    img[img < threshold] = 0 # black
    img[img >= threshold] = 255 # white
    return img

def count_objects_in_img(img):
    """ Counts the number of objects in a image"""
    # input should be a binary image 
    labeled, nr_objects = mh.label(img)
    # return number of objects
    return nr_objects
    
def center_of_image(img):
    """ Simply return the center point (center of mass) of an image"""
    return mh.center_of_mass(img)
    
if __name__ == "__main__":
    my_img = getImage()
    
    print "Converting image to a binary (black/white) image given a threshold 0 <= threshold <= 255"
    binary_image = convert2binaryimg(my_img, 100) # try different values for the threshold
    misc.imshow(binary_image) # display the black/white image
    
    print "Count the number of objects in the image"
    n_objects = count_objects_in_img(binary_image)
    print n_objects
    
    print "Finding the center point of an image: (coordinates are x,y"
    print "with the vertical axis as x and horizontal axis as y)"
    print center_of_image(binary_image)[:2]
    
    
    
    