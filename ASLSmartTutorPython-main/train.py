#run python3 train.py

import cv2
import numpy as np
from keras_squeezenet import SqueezeNet
#from tf.keras.optimizers import Adam
from keras.optimizers import adam_v2
from keras.utils import np_utils
from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
from keras.models import Sequential
import tensorflow as tf
import os


IMG_SAVE_PATH = 'images'
CLASS_MAP = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
    "nothing": 26
}
NUM_CLASSES = len(CLASS_MAP)
def mapper(val):
    return CLASS_MAP[val]
def get_model():
    model = Sequential([
        SqueezeNet(input_shape=(227, 227, 3), include_top=False),
        Dropout(0.5),
        Convolution2D(NUM_CLASSES, (1, 1), padding='valid'),
        Activation('relu'),
        GlobalAveragePooling2D(),
        Activation('softmax')
    ])
    return model
# load images from the directory
dataset = []
for directory in os.listdir(IMG_SAVE_PATH):
    path = os.path.join(IMG_SAVE_PATH, directory)
    if not os.path.isdir(path):
        continue
    for item in os.listdir(path):
        # to make sure no hidden files get in our way
        if item.startswith("."):
            continue
        img = cv2.imread(os.path.join(path, item))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (227, 227))
        dataset.append([img, directory])
data, labels = zip(*dataset)
labels = list(map(mapper, labels)) 
# one hot encode the labels
#labels = np_utils.to_categorical(labels)
# define the model
model = get_model()
model.compile(
    optimizer=adam_v2.Adam(learning_rate=0.0001), #
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
# start training
model.fit(np.array(data), np.array(labels), epochs=15) #
# save the model for later use
model.save("game-model.h5")