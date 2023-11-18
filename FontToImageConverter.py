from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import pickle
from PIL import Image, ImageFont, ImageDraw

font_name = str(input())
font_path = Path("C:/Users/arkin/Desktop/Fonts/"+ font_name + ".ttf")
out_path = Path("C:/Users/arkin/Desktop/Fonts")

font_size = 16 #px
font_color = "#000000" #HEX for black

font = ImageFont.truetype(str(font_path), font_size)

characters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0"

width, height = font.getsize("Q")
img = Image.new("RGBA", (width * 100, height * 2), color="white")
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