
from tensorflow import keras
from keras.applications.vgg19 import VGG19
from keras.utils import load_img
from keras.utils import img_to_array
from keras.applications.vgg16 import decode_predictions



#loading vgg16 model
model = VGG19()

#laoad image from file
image = load_img('src/mug.jpg', target_size=(224,224))

#convert image nito numpy array
image = img_to_array(image)

#reshape data for model
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

#predit probability accross all output classes
yhat = model.predict(image)

#convert probabilities to class labels
label = decode_predictions(yhat)
#retrieve highest probability result
label = label[0][0]
#print classification
print('%s (%.2f%%)' % (label[1], label[2]*100))

