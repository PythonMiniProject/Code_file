from tkinter import *
import tkinter.messagebox as tmsg 
from PIL import Image,ImageTk
root = Tk()
root.geometry("800x600")
def resizer(e):
    global bg1,resized_bg,new_bg
    #open our image
    bg1 = ImageTk.open("bg2.jpg")
    #image.Antialias used to provide anti-aliase effect to the image
    resized_bg = bg1.resize((e.width ,e.height),Image.ANTIALIAS)
    #Define image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    #Add image back to the canvas 
    my_canvas.create_image(0,0, image = new_bg,anchor = "nw")

bg = ImageTk.PhotoImage(file = "bg1.png")
# my_label = Label(root,image = bg)
# my_label.place(x = 0,y = 0 , relwidth = 1, relheight = 1)

my_canvas = Canvas(root,width = 800,height = 600)
my_canvas.pack(fill = "both",expand = True)

#Set image in a canvas
my_canvas.create_image(0,0, image = bg,anchor = "nw")

#add label 
my_canvas.create_text(400,300,text = "Grow More" , font = 'Helvetica 30 bold',fill = "white")




root.bind('<Configure>',resizer)
root.mainloop()
