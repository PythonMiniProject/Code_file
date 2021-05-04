from tkinter import *
from PIL import Image,ImageTk

def show_frame(frame):
    frame.tkraise()


window = Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)
page4 = Frame(window)

for frame in (page1, page2, page3,page4):
    frame.grid(row=0, column=0, sticky='nsew')



#==============func for the user login ======================



# ==================page-1 code========================================

page1_bg_img = ImageTk.PhotoImage(file = "bg2.jpg")

bg_page1 = Label(page1, image=page1_bg_img)
bg_page1.pack()

frame1_title = Label(page1, text='Selct the above options for respective log-in', font='times 35')
frame1_title.pack(fill='both', expand=True,anchor = "nw")


frame1_btn = Button(page1, text='User Log-In',font='times 25',width = 30,height = 2, command=lambda: show_frame(page2))
frame1_btn.place(x =600, y = 250)


frame1_btn = Button(page1, text='Admin Log-In',font='times 25',width = 30,height = 2, command=lambda: show_frame(page3))
frame1_btn.place(x =600, y = 380)



# ==================page-2 code (User login)======================================

        #=============== Images =================
bg_img = ImageTk.PhotoImage(file = "account_bg.jpg")
user_img = PhotoImage(file = "user_image.png")
adhar_img = PhotoImage(file="adhar_card.png")
log_user_img = PhotoImage(file="man_user.png")
pass_lock_img = PhotoImage(file="pass_lock.png")
loginbutton_img = PhotoImage(file="login.png")
exitbutton_img = PhotoImage(file="exit.png")
backbutton_page2_img = PhotoImage(file = "backimage_button.png")

        #===============to set bg image user login page ==================
bg = Label(page2, image=bg_img)
bg.pack()
title = Label(page2,text = "User Log-In", font = "Impact 45 ",bg = "yellow",fg = "orange",relief = SUNKEN,borderwidth = 8)
title.place(x = 0 , y = 0,relwidth = 1)  #relwidth is used to adjust text according to the window

        #=============login frame============================
Login_frame = Frame(page2,bg = 'white')
Login_frame.place(x = 500,y = 145)

        #user logo on top image in user login form
user_logo = Label(Login_frame,image = user_img,borderwidth=0).grid(row = 0,columnspan = 4,pady = 40)

        # ===============================Labels and text==================================
        #adding user_image to the user name
user_lbl = Label(Login_frame,text = "USERNAME:",image = log_user_img,compound = LEFT,
                 font = 'comicsans 15 bold',bg = "white").grid(row = 1,column = 0, pady =5)

txtuser = Entry(Login_frame,bd = 5 ,relief = SUNKEN,font = "Lucida 20 bold").grid(row=1,column=2,padx = 10)

adhar_lbl = Label(Login_frame,text = "ADHARCARD:",image = adhar_img,compound = LEFT,
                         font = 'comicsans 15 bold',bg = "white").grid(row = 2,column = 0, pady =5)
txtadhar = Entry(Login_frame, bd=5, relief=SUNKEN, font="Lucida 20 bold").grid(row=2, column=2, padx=10)

pass_lbl = Label(Login_frame,text = "PASSWORD:",image = pass_lock_img,compound = LEFT,
                 font = 'comicsans 15 bold',bg = "white").grid(row = 3,column = 0, pady =5)
txtpass = Entry(Login_frame, bd=5, relief=SUNKEN, font="Lucida 20 bold").grid(row=3, column=2, padx=10)

        #========================Buttons=========================================

exit_btn = Button(Login_frame,image =exitbutton_img,command = exit,borderwidth = 0,background = "white")
exit_btn.grid(row = 4,column = 0,pady = 40)


#=======================creating back button to swith through frames=============================
frame2_btn = Button(page2,image = backbutton_page2_img,borderwidth = 0,background = "yellow", command=lambda: show_frame(page1))
frame2_btn.place(x = 10,y = 8)


login_btn = Button(Login_frame,image =loginbutton_img,command=lambda: show_frame(page4),borderwidth = 0,background = "white")
login_btn.grid(row = 4,column = 2,pady = 40)




# ==================page-3 code (Admin log-in)=========================================

        #====================images admin frame ===============================
admin_name_logo = ImageTk.PhotoImage(file = "admin1.png")
admin_main_logo = PhotoImage(file = "adminuser.png")
wlc_admin = PhotoImage(file = "welcome1.png")
backbutton_img = PhotoImage(file = "backimage_button.png")
admin_login_button = ImageTk.PhotoImage(file = "admin_login_button1.png")



        #======================to set bg image for admin login page================
bg_img_admin = ImageTk.PhotoImage(file = "account_bg.2.jpg")
bg_admin = Label(page3, image=bg_img_admin)
bg_admin.pack()
admin_title = Label(page3,text = "Admin Log-In", font = "Impact 45 ",bg = "yellow",fg = "orange",relief = SUNKEN,borderwidth = 8)
admin_title.place(x = 0 , y = 0,relwidth = 1)  #relwidth is used to adjust text according to the window

        #================creating admin frame in page 3======================
admin_frame = Frame(page3,bg ='white')
admin_frame.place(x = 520,y = 110)


        #=================Labels and Entry widgets for admin form=================
wlc_lbl = Label(admin_frame,image = wlc_admin,bg = "white").grid(row= 0, columnspan = 4)
admin_logo = Label(admin_frame,image = admin_name_logo,bg = "white").grid(row= 1, columnspan = 4)
admin_user_logo = Label(admin_frame,image = admin_main_logo,bg = "white").grid(row= 2, columnspan = 4)

admin_lbl_id = Label(admin_frame,text = "ADMIN-ID:",image = log_user_img,compound = LEFT,
                 font = 'comicsans 15 bold',bg = "white").grid(row = 3,column = 0)
entry_admin_lbl_id = Entry(admin_frame,bd = 5 ,relief = SUNKEN,font = "Lucida 20 bold").grid(row=3,column=1,padx = 7,pady = 4)


admin_lbl_password = Label(admin_frame,text = "PASSWORD:",image = pass_lock_img,compound = LEFT,
                 font = 'comicsans 15 bold',bg = "white").grid(row = 4,column = 0,pady =2)
entry_admin_lbl_password = Entry(admin_frame,bd = 5 ,relief = SUNKEN,font = "Lucida 20 bold").grid(row=4,column = 1,padx = 7)

            #===================================Button for admin login==================

admin_button = Button(admin_frame,image = admin_login_button,borderwidth = 0,background = "white")
admin_button.grid(row = 5,columnspan = 4)

#=======================creating back button to swith through frames=============================



frame3_btn = Button(page3,image = backbutton_img,borderwidth = 0,background = "yellow", command=lambda: show_frame(page1))
frame3_btn.place(x = 10,y = 8)



#=====================================page 4============================
title1 = Label(page4,text = "Welcome to our page 4", font = "Impact 45 ",bg = "yellow",fg = "orange",relief = SUNKEN,borderwidth = 8)
title1.place(x = 0 , y = 0,relwidth = 1)  #relwidth is used to adjust text according to the window

def user_login():
    if user_pass == password:


show_frame(page1)

window.mainloop()
