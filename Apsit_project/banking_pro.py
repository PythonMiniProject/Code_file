from tkinter import *
import tkinter.messagebox as tmsg #to import message box
from PIL import Image, ImageTk    # pillow library to vieww images
import os
import re
from tkinter import ttk
import shelve
from tkinter.ttk import Combobox   #to import combobox
root = Tk()
root.title("BANKING PROJECT")
root.geometry("600x600")

#=========================list of districts for COMBOBOX=====================================
ls = ['Ahmednagar','Akola','Amravati','Aurangabad','Beed','Bhandara','Buldhana','Chandrapur','Dhule','Gadchiroli',
      'Gondia','Hingoli','Jalgaon','Jalna','Kolhapur','Latur','Mumbai City','Mumbai Suburban','Nagpur','Nanded',
      'Nandurbar','Nashik','Osmanabad','Palghar','Parbhani','Pune','Raigad','Ratnagiri','Sangli','Satara','Sindhudurg',
      'Solapur','Thane','Wardha','Washim','Yavatmal']

#func for combobox
def comboclick(event):
    pass

def clearAll():
    namevalue.set("")
    addressvalue.set("")
    phonevalue.set("")
    emailvalue.set("")
    agevalue.set("")
    adharcardvalue.set("")
    passwordvalue.set("")
    gendervalue.set("")
    accountvalue.set("")
    datevalue.set("")
    monthvalue.set("")
    yearvalue.set("")


def submit():
    username = namevalue.get()
    name = namevalue.get()
    age = agevalue.get()
    gender = gendervalue.get()
    password = passwordvalue.get()
    adharcard = adharcardvalue.get()
    address = addressvalue.get()
    phone = phonevalue.get()
    email = emailvalue.get()
    account_type = accountvalue.get()
    date_var = datevalue.get()
    month_var = monthvalue.get()
    year_var = yearvalue.get()
    users = os.chdir(r'C:\Users\Yash\Desktop\Python\Apsit_project\Users')
    all_accounts = os.listdir()
    exists = False
    isValid = False

    if username == "" or age == "" or gender == "" or password == "" or adharcard == "" or address=="" or phone =="":
        tmsg.showerror("Error","All feilds are required!")
        return

    print(adharcard)
#======================Check if same user exists or not using adharcard as key validation ========================
    for adharcard_check in all_accounts:
        # print(adharcard_check)
        if adharcard_check == adharcard:
            exists = True
            tmsg.showwarning("Alert","Account already exists!")
            break

#===========================Calling functions for step by step execution ===============================

    isValid = checkPhoneNumber(phone) and checkName(username) and checkAdharcard(adharcard) and \
              isValidEmail(email)



#===============================creating account if all conditons satisfies=========================
    #======================we use file handling for the account creation========================
    if exists == False and isValid == True:
        new_file = open(adharcard, "w")
        new_file.write(username + '\n')
        new_file.write(password + '\n')
        new_file.write(age + '\n')
        new_file.write(gender + '\n')
        new_file.write(adharcard + '\n')
        new_file.write(phone + '\n')
        new_file.write(address + '\n')
        new_file.write(email + '\n')
        new_file.write(account_type + '\n')
        new_file.write(date_var + '/' )
        new_file.write(month_var +'/' )
        new_file.write(year_var)
        new_file.write('0')
        new_file.close()
        tmsg.showinfo("Congratulations!","Your account has been succesfully created")
    else:
        tmsg.showerror("Error", "Please check input")

#===================Function for the validation of name==================
def checkName(user_name):
    print("checkName ", user_name)
    if user_name.isalpha():
        return True
    else:
        tmsg.showwarning("Invalid Input!", "Please Enter the correct name")
        print("checking name", user_name)
# #================================= Validation for age =====================
#
# def isValidAge(user_age):
#     if len(user_age)>0 and len(user_age) < 4 and user_age.isdigit():
#         v_age = int(user_age)
#         print("v_age kya hai?",type(v_age))
#         if v_age < 120 or v_age>0:
#             tmsg.showwarning("Alert!","Invalid age input please check your age again")
#             return True
#         else:
#             tmsg.showwarning("Alert","Please enter correct age value")
#             return False
#     else:
#         tmsg.showwarning("Alert","Please enter correct age value")
#         return False
#=====================Function for the validation of phone=================
def checkPhoneNumber(ph):
    print("checkPhoneNumber ", ph)
    if ph.isdigit() and len(ph) == 10:
         return True
    else:
        tmsg.showwarning("Invalid Input!", "Please Enter the correct phone number")
        print("Checking phone ", ph)
        return False
#================== Function for the validation of the adharcard=================
def checkAdharcard(user_adhar):
    print("checking adharcard number",user_adhar)
    if user_adhar.isdigit() and len(user_adhar) == 12:
         return True
    else:
        tmsg.showwarning("Alert!","The given adharcard number is Wrong Please Check Again!")
        return False


#============Function for the valiation of the email(We use regular expressions)===============
def isValidEmail(user_email):
    print("checking email",user_email)
    if len(user_email) > 7:
        if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",user_email) != None:
            return True
        else:
            tmsg.showwarning("Alert!", "Invalid Email please check your Email again!")
            return False
    else:
        tmsg.showwarning("Alert!", "Invalid Email please check your Email again!")
        return False



def log_in():
    window = Toplevel(root)
    window.title("Log-In ACCOUNT")
    #window = Tk()
    window.state('zoomed')

# def logout():
#     answer = tmsg.askyesno("Logout", "ARE YOU SURE YOU WANT TO LEAVE!")
#     if answer == YES:
#         account_dashboard.destroy()
    def admin_login():

#============================================Creating admin validations ==========================================
        if temp_admin_id.get()=="" or temp_admin_password.get()=="":
            tmsg.showerror("Error!","All fields are required.")

            #=============================== Admin key access=====================================
        elif temp_admin_id.get()=="admin" and temp_admin_password.get()=="password":
            window.destroy()
            admin_account = Toplevel(root)
            admin_account.state("zoomed")
            admin_account.title('Admin Page')

            #===========admin login image==============
            admin_account_dashboard_img = Label(admin_account, image=bg_img_admin)
            admin_account_dashboard_img.pack()

            admin_head = Label(admin_account, text="Welcome to our page 4", font="Impact 45 ",
                           bg="yellow", fg="orange", relief=SUNKEN, borderwidth=8)
            admin_head.place(x=0, y=0, relwidth=1)  # relwidth is used to adjust text according to the window
            admin_dashboard_frame_btn= Frame(admin_account,bg = "white",relief = SUNKEN,borderwidth=5)
            admin_dashboard_frame_btn.place(x = 8 , y= 250)
            page5btn1 = Button(admin_dashboard_frame_btn, text='User-Details', font='times 25', width=25, height=2,relief = "ridge", borderwidth=8).grid(row = 0,column = 0,pady = 1)
            page5btn2 = Button(admin_dashboard_frame_btn, text='Remove-User', font='times 25', width=25, height=2,relief = "ridge", borderwidth=8).grid(row = 1,column = 0,pady = 1)
            admin_logout_btn = Button(admin_dashboard_frame_btn, text='Log-Out', font='times 25', width=25, height=2,relief = "ridge", borderwidth=8).grid(row = 2,column = 0,pady = 1)
            showvalues = Frame(admin_account, bg="gray98", width=1020, height=900)
            showvalues.place(x=500, y=100)

        else:
            tmsg.showerror("Error!","Invalid Username or Password")



    def user_login():

        global login_adharcard


        users = os.chdir(r'C:\Users\Yash\Desktop\Python\Apsit_project\Users')
        all_accounts = os.listdir()

        login_adharcard = temp_user_adharcard.get()
        login_password = temp_user_password.get()

        for adhar_check in all_accounts:
            if adhar_check == login_adharcard:
                file = open(adhar_check, "r")
                file_data = file.read()
                file_data = file_data.split('\n')
                password = file_data[1]


                if login_adharcard == "" or login_password == "":
                    print("lawde kam kia ki nai ")
                    tmsg.showerror("Error", "All feids are requird")

#=================creating new window to display account credentials=======================
                elif login_password == password:
                    window.destroy()
                    account_dashboard = Toplevel(root)
                    account_dashboard.state("zoomed")
                    account_dashboard.title('Dashboard')

#===================background image of our account window=======================================

                    account_dashboard_bg_img = Label(account_dashboard, image=bg_img)
                    account_dashboard_bg_img.pack()

                    title1 = Label(account_dashboard, text="Welcome to our page 4", font="Impact 45 ",
                                   bg="yellow", fg="orange",relief=SUNKEN,borderwidth=8)
                    title1.place(x=0, y=0, relwidth=1)  # relwidth is used to adjust text according to the window
                    page4btn_frame = Frame(account_dashboard,bg = 'white',relief = SUNKEN,borderwidth=10)
                    page4btn_frame.place(x = 8,y = 120)
                    page4btn1 = Button(page4btn_frame, text='Personal-Details', font='times 25', width=25, height=2,relief = "ridge", borderwidth=8).grid(row =0 ,column = 0)
                    page4btn2 = Button(page4btn_frame, text='Deposit', font='times 25', width=25, height=2,relief = "ridge", borderwidth=8).grid(row =1 ,column = 0)
                    page4btn3 = Button(page4btn_frame, text='Withdraw', font='times 25', width=25, height=2,relief = "ridge", borderwidth=8).grid(row = 2,column = 0)
                    page4btn4 = Button(page4btn_frame, text='Check-Balance', font='times 25', width=25, height=2,relief = "ridge", borderwidth=8).grid(row = 3,column = 0)
                    logout_btn = Button(page4btn_frame, text='Log-Out', font='times 25', width=25, height=2,relief = "ridge", borderwidth=8).grid(row =4 ,column = 0)
                    showvalues = Frame(account_dashboard, bg="azure", width=1000, height=900,borderwidth=10)
                    showvalues.place(x=520, y=100)


                else:
                    tmsg.showerror("Error", "Please Enter a Valid Password !")


#==========================Show frame fuctions allows us to swap the frames in page form======================
    #===========================tkraise is used to overlap one frame with another one==========================
    def show_frame(frame):
        frame.tkraise()

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    page1 = Frame(window)
    page2 = Frame(window)
    page3 = Frame(window)

    global page1_bg_img
    for frame in (page1, page2, page3):
        frame.grid(row=0, column=0, sticky='nsew')

# =================================page-1 code===============================================

    page1_bg_img = ImageTk.PhotoImage(file="bg2.jpg")

    bg_page1 = Label(page1, image=page1_bg_img)
    bg_page1.place(x = 0 ,y = 0)

    frame1_title = Label(page1, text='Selct the above options for respective log-in',bg = "DarkOrange1", font='Impact 45')
    frame1_title.place(x = 0,y = 0,relwidth = 1)

    page1_btn_frame = Frame(page1, bg='white')
    page1_btn_frame.place(x = 200,y = 200)

    frame1_btn = Button(page1_btn_frame, text='User Log-In',relief = "ridge",borderwidth = 8, font='times 25', width=30, height=2,
                        command=lambda: show_frame(page2))
    frame1_btn.grid(row = 0,column = 0)

    frame1_btn = Button(page1_btn_frame, text='Admin Log-In',relief = "ridge",borderwidth = 8, font='times 25', width=30, height=2,
                        command=lambda: show_frame(page3))
    frame1_btn.grid(row = 1,column = 0)

# ============================page-2 code (User login)======================================

    global bg_img,user_img,adhar_img,log_user_img,pass_lock_img,loginbutton_img,exitbutton_img,backbutton_page2_img

    # =============== Images =================
    bg_img = ImageTk.PhotoImage(file="account_bg.jpg")
    user_img = PhotoImage(file="user_image.png")
    adhar_img = PhotoImage(file="adhar_card.png")
    log_user_img = PhotoImage(file="man_user.png")
    pass_lock_img = PhotoImage(file="pass_lock.png")
    loginbutton_img = PhotoImage(file="login.png")
    exitbutton_img = PhotoImage(file="exit.png")
    backbutton_page2_img = PhotoImage(file="backimage_button.png")

    # ===============to set bg image user login page ==================
    bg = Label(page2, image=bg_img)
    bg.pack()
    title = Label(page2, text="User Log-In", font="Impact 45 ", bg="yellow", relief=SUNKEN, borderwidth=8)
    title.place(x=0, y=0, relwidth=1)  # relwidth is used to adjust text according to the window

    # =============login frame============================
    Login_frame = Frame(page2, bg='white')
    Login_frame.place(x=500, y=145)

    # user logo on top image in user login form
    user_logo = Label(Login_frame, image=user_img, borderwidth=0).grid(row=0, columnspan=4, pady=40)

    # ===============================Labels and text==================================
    # adding user_image to the user name
    user_lbl = Label(Login_frame, text="USERNAME:", image=log_user_img, compound=LEFT,
                     font='comicsans 15 bold', bg="white").grid(row=1, column=0, pady=5)

    global temp_user_name, temp_user_adharcard, temp_user_password

    #===========================initailizing our variables ==========================
    temp_user_name = StringVar()
    temp_user_adharcard = StringVar()
    temp_user_password = StringVar()
    txtuser = Entry(Login_frame, bd=5, relief=SUNKEN,textvariable = temp_user_name, font="Lucida 20 bold").grid(row=1, column=2, padx=10)

    adhar_lbl = Label(Login_frame, text="ADHARCARD:", image=adhar_img, compound=LEFT,
                      font='comicsans 15 bold', bg="white").grid(row=2, column=0, pady=5)
    txtadhar = Entry(Login_frame, bd=5, relief=SUNKEN,textvariable = temp_user_adharcard, font="Lucida 20 bold").grid(row=2, column=2, padx=10)

    pass_lbl = Label(Login_frame, text="PASSWORD:", image=pass_lock_img, compound=LEFT,
                     font='comicsans 15 bold', bg="white").grid(row=3, column=0, pady=5)
    txtpass = Entry(Login_frame, bd=5, relief=SUNKEN,textvariable = temp_user_password, font="Lucida 20 bold").grid(row=3, column=2, padx=10)

    # ========================Buttons=========================================
    login_btn = Button(Login_frame, image=loginbutton_img,command=user_login,borderwidth=0, background="white")
    login_btn.grid(row=4, column=2, pady=40)

    exit_btn = Button(Login_frame, image=exitbutton_img, command=exit, borderwidth=0, background="white")
    exit_btn.grid(row=4, column=0, pady=40)

    # =======================creating back button to swith through frames=============================
    frame2_btn = Button(page2, image=backbutton_page2_img, borderwidth=0, background="yellow",
                        command=lambda: show_frame(page1))
    frame2_btn.place(x=10, y=8)

    # ==================page-3 code (Admin log-in)=========================================

    global admin_name_logo,admin_main_logo,wlc_admin,backbutton_img,admin_login_button,bg_img_admin

    # ====================images admin frame ===============================
    # bank_logo = PhotoImage(file="new_bank_symbol.png")
    admin_main_logo = PhotoImage(file="adminuser.png")
    backbutton_img = PhotoImage(file="backimage_button.png")
    admin_login_button = ImageTk.PhotoImage(file="admin_login_button1.png")

    # ======================to set bg image for admin login page================

    global temp_admin_id,temp_admin_password

    bg_img_admin = ImageTk.PhotoImage(file="account_bg.2.jpg")
    bg_admin = Label(page3, image=bg_img_admin)
    bg_admin.pack()
    admin_title = Label(page3, text="Admin Log-In", font="Impact 45 ", bg="yellow", relief=SUNKEN,
                        borderwidth=8)
    admin_title.place(x=0, y=0, relwidth=1)  # relwidth is used to adjust text according to the window

    # ================creating admin frame in page 3======================
    admin_frame = Frame(page3, bg='white')
    admin_frame.place(x=520, y=180)

    # =================Labels and Entry widgets for admin form=================
    # bank_logo_label = Label(admin_frame,image = bank_logo,bg = "white").grid ( row = 0,columnspan= 2)
    admin_user_logo = Label(admin_frame, image=admin_main_logo, bg="white").grid(row=2, columnspan=4)

    # ====== text variables ========
    temp_admin_id = StringVar()
    temp_admin_password = StringVar()

    admin_lbl_id = Label(admin_frame, text="ADMIN-ID:", image=log_user_img, compound=LEFT,
                         font='comicsans 15 bold', bg="white").grid(row=3, column=0)
    entry_admin_lbl_id = Entry(admin_frame, bd=5,textvariable = temp_admin_id, relief=SUNKEN, font="Lucida 20 bold").grid(row=3, column=1, padx=7,
                                                                                             pady=4)

    admin_lbl_password = Label(admin_frame, text="PASSWORD:", image=pass_lock_img, compound=LEFT,
                               font='comicsans 15 bold', bg="white").grid(row=4, column=0, pady=2)
    entry_admin_lbl_password = Entry(admin_frame, bd=5,textvariable = temp_admin_password, relief=SUNKEN, font="Lucida 20 bold").grid(row=4, column=1,padx=7)

    # ===================================Button for admin login==================

    admin_button_login = Button(admin_frame, image=admin_login_button,command = admin_login, borderwidth=0, background="white")
    admin_button_login.grid(row=5, columnspan=4)

    # =======================creating back button to swith through frames=============================

    frame3_btn = Button(page3, image=backbutton_img, borderwidth=0, background="yellow",
                        command=lambda: show_frame(page1))
    frame3_btn.place(x=10, y=8)


    show_frame(page1)





#================================================      MAIN GUI      ============================================
def create_acc():

    global namevalue,addressvalue,phonevalue,emailvalue,agevalue,adharcardvalue,passwordvalue,gendervalue,accountvalue
    global datevalue,monthvalue,yearvalue
    # ======================We created new window using toplevel function=====================
    #new window name is register_screen
    register_screen = Toplevel(root)
    register_screen.geometry("750x600")
    register_screen.title("CREATE ACCOUNT")
    re_frame1 = Frame(register_screen,width = 700,height = 100,highlightbackground = 'grey',highlightthickness = 2,relief = SUNKEN,bg = "CadetBlue1")
    Label(re_frame1,text = 'Get Your ONLINE-BANK Account in a few minutes with GROW-MORE.\n',font = 'comicsans 15 bold',bg = "CadetBlue1").place(x = 40,y = 20)
    Label(re_frame1,text = 'With Grow-more we provide our best services and safety Banking for you '
                           'your family.',font = ' comicsans 8 italic',bg = "CadetBlue1").place(x = 40 , y = 60)
    re_frame1.pack(pady = 2,fill = X)
    re_frame2 = Frame(register_screen, width=700, height=600, highlightbackground='grey', highlightthickness=2,
                      relief=SUNKEN, bg="azure")

    #=====================================combobox============================
    mycombo = ttk.Combobox(register_screen,value = ls)
    mycombo.current(0)
    mycombo.bind("<<comboboxsselected>>",comboclick)
    mycombo.place(x = 252,y = 187)


    #=====================================Labels============================
    Label(re_frame2, text='NAME:', font='comicsans 10 bold', bg="azure").place(x= 40,y=10)
    Label(re_frame2, text='ADDRESS:', font='comicsans 10 bold', bg="azure").place(x=40, y=40)
    Label(re_frame2, text='DISTRICT:', font='comicsans 10 bold', bg="azure").place(x=40, y=70)
    Label(re_frame2, text='PHONE-NO:', font='comicsans 10 bold', bg="azure").place(x=40, y=100)
    Label(re_frame2, text='GENDER:', font='comicsans 10 bold', bg="azure").place(x=40, y=130)
    Label(re_frame2, text='DOB:', font='comicsans 10 bold', bg="azure").place(x=40, y=160)
    Label(re_frame2, text='E-MAIL:', font='comicsans 10 bold', bg="azure").place(x=40, y=190)
    Label(re_frame2, text='AGE:', font='comicsans 10 bold', bg="azure").place(x=40, y=220)
    Label(re_frame2, text='ADHARCARD:', font='comicsans 10 bold', bg="azure").place(x=40, y=250)
    Label(re_frame2, text='PASSWORD:', font='comicsans 10 bold', bg="azure").place(x=40, y=280)
    Label(re_frame2, text='ACCOUNT-TYPE:', font='comicsans 10 bold', bg="azure").place(x=40, y=310)

    #=====================================Entry box variables============================
    namevalue = StringVar()
    addressvalue = StringVar()
    phonevalue = StringVar()
    emailvalue = StringVar()
    agevalue = StringVar()
    adharcardvalue = StringVar()
    passwordvalue = StringVar()
    gendervalue = StringVar()
    accountvalue = StringVar()
    datevalue = StringVar()
    monthvalue = StringVar()
    yearvalue = StringVar()

    #=====================================Entry box============================
    Entry_name = Entry(re_frame2,textvariable =namevalue,font="comicsans 10 bold")
    Entry_name.place(x=250,y= 10)
    Entry_address = Entry (re_frame2,textvariable =addressvalue,font="comicsans 10 bold")
    Entry_address.place(x=250,y= 40)
    Entry_phone = Entry (re_frame2,textvariable =phonevalue,font="comicsans 10 bold")
    Entry_phone.place(x=250,y= 100)
    Entry_email = Entry (re_frame2, textvariable=emailvalue, font="comicsans 10 bold")
    Entry_email.place(x=250,y= 190)
    Entry_age = Entry (re_frame2,textvariable =agevalue,font="comicsans 10 bold")
    Entry_age.place(x=250,y= 220)
    Entry_adhar = Entry (re_frame2,textvariable =adharcardvalue,font="comicsans 10 bold")
    Entry_adhar.place(x=250,y= 250)
    Entry_password = Entry (re_frame2,textvariable =passwordvalue,show = "*",font="comicsans 10 bold")
    Entry_password.place(x=250,y= 280)
    Entry_date = Entry (re_frame2,textvariable = datevalue,font= 'Lucida 10 bold',width = 2)
    Entry_date.place(x = 250,y = 160)  #dd
    Entry_month = Entry (re_frame2,textvariable = monthvalue, font='Lucida 10 bold', width=2)
    Entry_month.place(x=275, y=160)  #mm
    Entry_year = Entry (re_frame2,textvariable = yearvalue, font='Lucida 10 bold', width=4)
    Entry_year.place(x=300, y=160) #yy



    gendervalue.set("male")
    #=====================================Radio button for gender============================
    r1 = Radiobutton(re_frame2,text = 'male', variable = gendervalue, value = "male", bg="azure")
    r2 = Radiobutton(re_frame2,text = 'female',variable = gendervalue,value = "female", bg="azure")
    r1.place(x = 249, y = 130)
    r2.place(x = 320 , y = 130)

    #=====================================Radio button for account type============================
    accountvalue.set("saving")
    r3 = Radiobutton(re_frame2,text = 'CURRENT', variable = accountvalue, value = "current", bg="azure")
    r4 = Radiobutton(re_frame2,text = 'SAVING',variable = accountvalue,value = "saving", bg="azure")
    r3.place(x = 249, y = 310)
    r4.place(x = 350 , y = 310)

    #
    # Button(re_frame2, text="SUBMIT", font="comicsans 12",bg = "green",fg = "white",
    #        width=20, command=submit).place(x=249, y=350)

    Button(re_frame2, text="SUBMIT",command = submit, font="comicsans 12",bg = "green",fg = "white",
           width=20,borderwidth = 5,relief = RAISED).place(x=249, y=350)
    Button(re_frame2, text="RESET",command = clearAll, font="comicsans 12",bg = "green",fg = "white",
           width=20,borderwidth = 5,relief = RAISED).place(x=249, y=390)

    re_frame2.pack(fill = 'both')



#==============================main window frame of the first page========================
mframe1 = Frame (root,width = 700,height = 100,highlightbackground = 'grey',highlightthickness = 2,relief = SUNKEN,bg = "green")
Label(mframe1,text = " Grow more ",font = 'Lucida 40 bold',bg = 'green',fg = 'white').place(x = 44,y = 10)
Label(mframe1,text = " Since 1992 ",font = 'Lucida 10 bold',bg = 'green').place(x = 60,y = 70)
mframe1.pack(padx = 20,pady = 5,fill = 'both')

#=====================changing Image of main window=========================


#=====================Image swaping ===================================
#image Tk used to import jpg images in tk window
img1=ImageTk.PhotoImage(Image.open("img1.jpg"))
img1 = Image.open("img1.jpg")
img1= img1.resize((400,300))
img1 = ImageTk.PhotoImage(img1)


img2=ImageTk.PhotoImage(Image.open("img2.png"))
img2 = Image.open("img2.png")
img2= img2.resize((400,300))
img2 = ImageTk.PhotoImage(img2)

img3=ImageTk.PhotoImage(Image.open("img3.png"))
img3 = Image.open("img3.png")
img3= img3.resize((400,300))
img3 = ImageTk.PhotoImage(img3)

#Create a label
l=Label(root,font="bold")
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
    #you can do it for thousands of images
    #now increase the count by one
    x+=1
    #set images to work automatically by "after" feature in tkinter
    #after view image one by one after the given time i.e 2000 mil sec.
    root.after(2000,move)
move()

#=============================main window buttons ========================================
Button(root,text = 'Create Account',bg = 'yellow green',command = create_acc).place(x = 100,y = 434)
Button(root,text = 'Log-In',bg = 'yellow green',command = log_in).place(x = 230,y = 434)




root.mainloop()
