from tkinter import *
from PIL import Image,ImageTk
import random

class login_sys:
    def __init__(self,window):
        self.window = window
        self.window.title("Log-In")
        self.window.geometry("1000x800+370+0")

        #=============== Images =================
        self.bg_img = ImageTk.PhotoImage(file = "bg4.jpg")
        self.user_img = PhotoImage(file = "user_image.png")
        self.adhar_img = PhotoImage(file="adhar_card.png")
        self.log_user_img = PhotoImage(file="man_user.png")
        self.pass_lock_img = PhotoImage(file="pass_lock.png")
        self.loginbutton_img = PhotoImage(file="login.png")
        self.exitbutton_img = PhotoImage(file="exit.png")

        #===============to set bg image ==================
        bg = Label(self.window, image=self.bg_img)
        bg.pack()
        title = Label(self.window,text = "Log-In", font = "Impact 40 ",bg = "yellow",fg = "orange",relief = SUNKEN)
        title.place(x = 0 , y = 0,relwidth = 1)  #relwidth is used to adjust text according to the window

        Login_frame = Frame(self.window,bg = 'white')
        Login_frame.place(x = 250,y = 100)

        #main image in form
        user_logo = Label(Login_frame,image = self.user_img,borderwidth=0).grid(row = 0,columnspan = 4,pady = 40)

        # ===============================Labels and text==================================
        #adding user_image to the user name
        user_lbl = Label(Login_frame,text = "USERNAME:",image = self.log_user_img,compound = LEFT,
                         font = 'comicsans 15 bold',bg = "white").grid(row = 1,column = 0, pady =5)

        txtuser = Entry(Login_frame,bd = 5 ,relief = SUNKEN,font = "Lucida 20 bold").grid(row=1,column=2,padx = 10)

        adhar_lbl = Label(Login_frame,text = "ADHARCARD:",image = self.adhar_img,compound = LEFT,
                         font = 'comicsans 15 bold',bg = "white").grid(row = 2,column = 0, pady =5)
        txtadhar = Entry(Login_frame, bd=5, relief=SUNKEN, font="Lucida 20 bold").grid(row=2, column=2, padx=10)

        pass_lbl = Label(Login_frame,text = "PASSWORD:",image = self.pass_lock_img,compound = LEFT,
                         font = 'comicsans 15 bold',bg = "white").grid(row = 3,column = 0, pady =5)
        txtpass = Entry(Login_frame, bd=5, relief=SUNKEN, font="Lucida 20 bold").grid(row=3, column=2, padx=10)

        #========================Buttons=========================================
        login_btn = Button(Login_frame,image =self.loginbutton_img,borderwidth = 0,background = "white")
        login_btn.grid(row = 4,column = 2,pady = 40)

        exit_btn = Button(Login_frame,image =self.exitbutton_img,borderwidth = 0,background = "white")
        exit_btn.grid(row = 4,column = 0,pady = 40)


        #lframe = Frame()




window = Tk()
obj = login_sys(window)
window.mainloop()
