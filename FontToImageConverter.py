from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import pickle
from PIL import Image, ImageFont, ImageDraw

font_path = Path("C:/Users/arkin/Desktop/Fonts/Roboto-Regular.ttf")
font_name = "Roboto-Regular"
out_path = Path("C:/Users/arkin/Desktop/Fonts")

font_size = 16 #px
font_color = "#000000" #HEX for black

font = ImageFont.truetype(str(font_path), font_size)

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
init_char = "Q"

width, height = font.getsize(init_char)
img = Image.new("RGBA", (width * 100, height * 100))
draw = ImageDraw.Draw(img)
draw.text((0, 0), characters, font=font, fill=font_color)
try:
     img.save(str(out_path) + "\\" + font_name + ".png")
except:
     print(f"[-] Couldn't save font image")


#for character in desired_characters:
 #   width, height = font.getsize(character)
  #  img = Image.new("RGBA", (width * 70, height * 70))
   # draw = ImageDraw.Draw(img)
    #draw.text((-2, -2), str(character), font=font, fill=font_color)
    #try:
     #   img.save(str(out_path) + "\\" + str(ord(character)) + ".png")
    #except:
     #   print(f"[-] Couldn't save:\t{character}")