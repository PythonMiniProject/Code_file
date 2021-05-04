#Today we see how to change a picture
#automatcally in an fixed interval
#Using pillow module
#LEt's see

#Import all module inside tkinter
from tkinter import *

#import pillow module and related module like
from PIL import Image,ImageTk

#create a tkinter window
t=Tk()

#Create a size for tkinter window
t.geometry("300x200")#here use alphabet 'x' not '*' this one

#now set an image for moving
img1=ImageTk.PhotoImage(Image.open("img1.jpg"))
img1 = Image.open("img1.png")
img1= img1.resize((400,300))
img1 = ImageTk.PhotoImage(img1)

#make sure that you have a photo
#in you current folder that you are working with
img2=ImageTk.PhotoImage(Image.open("img2.png"))
img2 = Image.open("img2.png")
img2= img2.resize((400,300))
img2 = ImageTk.PhotoImage(img2)

img3=ImageTk.PhotoImage(Image.open("img3.png"))
img3 = Image.open("img3.png")
img3= img3.resize((400,300))
img3 = ImageTk.PhotoImage(img3)

img4=ImageTk.PhotoImage(Image.open("img4.jpg"))
img4 = Image.open("img4.jpg")
img4= img4.resize((400,300))
img4 = ImageTk.PhotoImage(img4)
#Create a label
l=Label(t,font="bold")
l.pack()
#take a variable
x=1
#create a function for moving a picture
def move():#name anything but meaningful
    global x
    if x==4:
        x=0
    if x==1:
        l.config(image=img1)#by writing this line first picture will appear
    elif x==2:
        l.config(image=img2)
    elif x==3:
        l.config(image=img3)
    elif x==4:
        l.config(image=img4)
    #you can do it for thousands of images
    #now increase the count by one
    x+=1
    #set images to work automatically by "after" feature in tkinter
    t.after(2000,move)
#Call the function
move()
t.mainloop()
