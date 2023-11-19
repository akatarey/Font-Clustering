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
os.chdir(path)

font_imgs = []
with os.scandir(path) as files:
    for file in files:
        if file.name.endswith(".png"):
            font_imgs.append(file.name)

print(font_imgs)
