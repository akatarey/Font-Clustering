from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input

from keras.applications.vgg16 import VGG16
from keras.models import Model

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import pickle
from PIL import Image, ImageFont, ImageDraw
#Convert ttf into image files, then plug in

font_path = Path("C:/Users/arkin/Desktop/Fonts/Roboto-Regular.ttf")
font_name = "Roboto-Regular.ttf"
out_path = Path("C:/Users/arkin/Desktop/Fonts")

font_size = 16 #px
font_color = "#000000" #HEX for black

font = ImageFont.truetype(str(font_path), font_size)

desired_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

for character in desired_characters:
    width, height = font.getsize(character)
    img = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(img)
    draw.text((-2, -2), str(character), font=font, fill=font_color)
    try:
        img.save(str(out_path) + "\\" + str(ord(character)) + ".png")
    except:
        print(f"[-] Couldn't save:\t{character}")
