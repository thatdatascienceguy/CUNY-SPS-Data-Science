""" Author: Jonathan Hernandez
	DATA622 Final Project: Image Classification using Alien/predator images
	
Image datase URL: https://www.kaggle.com/pmigdal/alien-vs-predator-images
Image location on (temp AWS Ubuntu Deep Learning AMI g3s.xlarge instance):
	/home/ubuntu/alien_vs_predator_thumbnails/data/train for training images
	/home/ubuntu/alien_vs_predator_thumbnails/data/validation for validation/test images
	
"""

# importing libraries 
from keras.preprocessing.image import ImageDataGenerator 
from keras.models import Sequential 
from keras.layers import Conv2D, MaxPooling2D 
from keras.layers import Activation, Dropout, Flatten, Dense 
from keras.preprocessing import image
import numpy as np

# length of width and height of each image.
# For all images in the training and validation folders, they should be the same exact size
# before doing CNN
img_width, img_height = 250, 250

# training and test dataset locations 
train_data_dir = 'alien_vs_predator_thumbnails/data/train'
test_data_dir = 'alien_vs_predator_thumbnails/data/validation'

# each example
n_train_samples = 694  # number of training images of aliens and predators
n_validation_samples = 200 # number of validation images
epochs = 10 # number of epochs (each one based on testing takes about 90 seconds to complete
batch_size = 32

# i'm using a MXnet backend as I had trouble using a tensorflow so it's more channels_last
# also per warnings can make the CNN and epochs slow.

input_shape = (img_width, img_height, 3) 

# Add a sequential model (linear stack of layers) 
avp_classifier = Sequential()

""" This CNN will be as follows:
	2 CNN layers each with a relu activation function and at the end flatten, do another relu function and use a 
	sigmoid function (classify) to classify the image
"""
# Add a layer with a relu activation function 
avp_classifier.add(Conv2D(32, (2, 2), input_shape = input_shape)) 
avp_classifier.add(Activation('relu')) 
avp_classifier.add(MaxPooling2D(pool_size =(2, 2)))

# add another layer with relu
avp_classifier.add(Conv2D(32, (2, 2)))
avp_classifier.add(Activation('relu'))
avp_classifier.add(MaxPooling2D(pool_size =(2, 2)))

# add another with relu but with 64 output filters
avp_classifier.add(Conv2D(64, (2, 2)))
avp_classifier.add(Activation('relu'))
avp_classifier.add(MaxPooling2D(pool_size =(2, 2))) 

# another layer?
avp_classifier.add(Conv2D(64, (2, 2)))
avp_classifier.add(Activation('relu'))
avp_classifier.add(MaxPooling2D(pool_size =(2, 2)))

# flatten, make a fully connected layer using relu and prevent overfitting with dropout
# also last layer has one node which will be a sigmoid function to classify the image
avp_classifier.add(Flatten()) 
avp_classifier.add(Dense(64)) 
avp_classifier.add(Activation('relu')) 
avp_classifier.add(Dropout(0.5)) 
avp_classifier.add(Dense(1)) 
avp_classifier.add(Activation('sigmoid')) 

avp_classifier.compile(loss ='binary_crossentropy', 
                     optimizer ='rmsprop', 
                   metrics =['accuracy']) 

train_datagen = ImageDataGenerator( 
                rescale = 1. / 255, 
                 shear_range = 0.2, 
                  zoom_range = 0.2, 
            horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1. / 255) 

train_generator = train_datagen.flow_from_directory(train_data_dir, 
                              target_size =(img_width, img_height), 
                     batch_size = batch_size, class_mode ='binary') 

validation_generator = test_datagen.flow_from_directory( 
                                    test_data_dir, 
                   target_size =(img_width, img_height), 
          batch_size = batch_size, class_mode ='binary') 

avp_classifier.fit_generator(train_generator, 
    steps_per_epoch = n_train_samples // batch_size, 
    epochs = epochs, validation_data = validation_generator, 
    validation_steps = n_validation_samples // batch_size) 

# test it out with a sample image (250,250,3) see if it can guess that the picture is a predator

test_image = image.load_img('/home/ubuntu/alien_vs_predator_thumbnails/data/testimages/is_predator.png', target_size = (250, 250))
# convert to number array
test_image = image.img_to_array(test_image)

test_image = np.expand_dims(test_image, axis = 0)
#print(test_image)

# make a prediction. If 0 it's an alien otherwise it's an predator
result = avp_classifier.predict(test_image)
print(avp_classifier.predict_classes(test_image))
print(avp_classifier.predict_proba(test_image))
print("Labels and their value: ", train_generator.class_indices)
if result[0][0] == 0:
	prediction = 'alien'
else:
	prediction = 'predator'

print("The picture is a: ", prediction)
