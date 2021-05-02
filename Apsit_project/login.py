from tkinter import *
import os

window = Tk()
window.title('Log-In')
window.geometry("800x600")

def login():
    frame.tkraise()

window.rowconfigure(0,weight = 1)
window.columnconfigure(0,weight = 1)

lframe1 = Frame(window)
lframe2 = Frame(window)
lframe3 = Frame(window)

for frame in (lframe1,lframe2,lframe3):
    lframe1.place(x = 0,y = 0)


#def login():
    #pass

#labels
Label(lframe1,text = " Log-In : ",font = 'comicsans 20 bold').place(x = 40,y = 90)
Label(lframe1,text = " Username: ",font = 'comicsans 15 bold').place(x = 10,y = 140)
Label(lframe1,text = " Adharcard-Number: ",font = 'comicsans 15 bold').place(x = 10,y = 170)
Label(lframe1,text = " Password: ",font = 'comicsans 15 bold').place(x = 10,y = 200)

#Entry boxes varible
login_var= StringVar()
name_var= StringVar()
pass_var= StringVar()
all_account = os.listdir()

#Entry boxes
Entry(lframe1, textvariable=login_var, font="comicsans 15 bold").place(x=250, y=140)
Entry(lframe1, textvariable=name_var, font="comicsans 15 bold").place(x=250, y=170)
Entry(lframe1, textvariable=pass_var, font="comicsans 15 bold").place(x=250, y=200)

Button(lframe1, text="Log-In", font="comicsans 12",width=20, command=lambda : login(lframe2).place(x=249, y=240)

#code for frame 2
Label(lframe2,text = "this is frame 2",font = 'Lucida 20 bold').place(x = 10 , y = 10)
login(lframe1)

window.mainloop()
