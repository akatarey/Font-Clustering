from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input

from keras.applications.vgg16 import VGG16
from keras.models import Model

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from pathlib import Path
import os
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import pickle
#Convert ttf into image files, then plug in

path = Path("C:/Users/arkin/Desktop/Fonts")
os.chdir(path)  #Changes current path of process from FontClustering.py's filepath to the Fonts filepath

font_imgs = []
with os.scandir(path) as files: #Scans through directory looking for png files
    for file in files:
        if file.name.endswith(".png"):
            font_imgs.append(file.name)

#load model
model = VGG16()
model = Model(inputs=model.inputs, outputs=model.layers[-2].output) #Remove output layer

def extract_features(file, model):
    img = load_img(file, target_size=(224, 224)) #VGG model expects images to be 224x224 NumPy arrays
    img = np.array(img) #This np array only has 3 dimensions, model needs batches
    #Model needs 4 dimensions: Number of Images, Number of rows, number of columns, number of channels
    img = img.reshape(1, 224, 224, 3) 

    x = preprocess_input(img)

    features = model.predict(x, use_multiprocessing=True)
    return features

data = {}

for font in font_imgs:
    feat = extract_features(font, model)
    data[font] = feat

filenames = np.array(list(data.keys())) #Save filenames as NumPy array

features = np.array(list(data.values()))
features = features.reshape(-1, 4096)
print(feat.shape)