from tkinter import *
from PIL import Image,ImageTk

img1 = Image.open("backbutton2.png")
MAX_SIZE = (70,70)
img1.thumbnail(MAX_SIZE)
img1.save("backimage_button.png")
