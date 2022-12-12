#import required libraries
#import pandas as pd
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.layers import Input, Lambda, Dense, Flatten
from keras.models import Model
from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential

#path for train, validation, and test sets
path_train = ''
path_valid = ''
path_test = ''

IMAGE_SIZE = [224, 224] #default image input size for vgg19

folders = glob('datasets/train/*') #num of classes

#ImageDataGenerator for image augmentation
datagen_train = ImageDataGenerator(rescale = 1./225, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
datagen_val = ImageDataGenerator(rescale = 1./225)
datagen_test = ImageDataGenerator(rescale = 1./225)
#Through flow_from_directory - we create an array of images that can be used for training. 
training_set = datagen_train.flow_from_directory('data/train',
                                                 target_size = (224, 224),
                                                 batch_size = 64,
                                                 class_mode = 'categorical')
validation_set = datagen_val.flow_from_directory('data/val',
                                                 target_size = (224, 224),
                                                 batch_size = 64,
                                                 class_mode = 'categorical')
test_set = datagen_test.flow_from_directory('data/test',
                                            target_size = (224, 224),
                                            batch_size = 32,
                                            class_mode = 'categorical')

# Create a VGG16 model, and removing the last layer that is classifying 1000 images. This will be replaced with images classes we have. 
vgg = VGG19(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False) #Training with Imagenet weights
# Use this line for VGG19 network. Create a VGG19 model, and removing the last layer that is classifying 1000 images. This will be replaced with images classes we have. 
#vgg = VGG19(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)
# This sets the base that the layers are not trainable. If we'd want to train the layers with custom data, these two lines can be ommitted. 
for layer in vgg.layers:
  layer.trainable = False
x = Flatten()(vgg.output) #Output obtained on vgg16 is now flattened. 
prediction = Dense(len(folders), activation='softmax')(x) # We have 5 classes, and so, the prediction is being done on len(folders) - 5 classes
#Creating model object 
model = Model(inputs=vgg.input, outputs=prediction)
model.summary()


#Compile the model 
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 
history = model.fit(training_set, validation_data=validation_set, epochs=20, batch_size=32)

#loss
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.legend()
plt.show()
 
#accuracies
plt.plot(history.history['accuracy'], label='train acc')
plt.plot(history.history['val_accuracy'], label='val acc')
plt.legend()
plt.show()

#from tensorflow.keras.models import load_model
#model.save('FlowerClassification.h5')








