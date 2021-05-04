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

#list of districts for combobox
ls = ['Ahmednagar','Akola','Amravati','Aurangabad','Beed','Bhandara','Buldhana','Chandrapur','Dhule','Gadchiroli',
      'Gondia','Hingoli','Jalgaon','Jalna','Kolhapur','Latur','Mumbai City','Mumbai Suburban','Nagpur','Nanded',
      'Nandurbar','Nashik','Osmanabad','Palghar','Parbhani','Pune','Raigad','Ratnagiri','Sangli','Satara','Sindhudurg',
      'Solapur','Thane','Wardha','Washim','Yavatmal']

#func for combobox
def comboclick(event):
    pass

#
# count = 0
def submit():
        global username
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
        all_accounts = os.listdir()

        if username == "" or age == "" or gender == "" or password == "" or adharcard == "" or address==""\
                or phone =="":
            tmsg.showerror("Error","All feilds are required!")
            return

        for adharcard_check in all_accounts:
            if adharcard_check == adharcard:
                tmsg.showwarning("Alert","Account already exists!")
                return
            else:
                new_file = open(name, "w")
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
                new_file.write(year_var+ '\n')
                new_file.write('0.0')
                new_file.close()
                tmsg.showinfo("Congratulations!","Your account has been succesfully created")
                break

#     global count
# # we inintialized values of variables in from entrybox
#     name = namevalue.get()
#     address = addressvalue.get()
#     phone = phonevalue.get()
#     email = emailvalue.get()
#     age = agevalue.get()
#     adharcard = adharcardvalue.get()
#     password = passwordvalue.get()
#     gender = gendervalue.get()
#     account_type = accountvalue.get()
#     date_var = datevalue.get()
#     month_var = monthvalue.get()
#     year_var = yearvalue.get()
#     all_accounts = os.listdir()
#
#
#     #else:
#         #with open("accounts.txt","a") as f:
#             #f.write(f'name = {name}\n,address = {address}\n,phone = {phone}\n,email = {email}\n,age = {age}\n,'
#              #       f'adharcard = {adharcard}\n,password = {password}\n,gender ={gender}\n,account type = {account_type},\n')
#             #tmsg.showinfo("CONGRATULATIONS","YOUR ACCOUNT HAS SUCCESSFULLY CREATED")
#
#     # if  name.isalpha() or phone.isdigit() or address.isalnum() or age.isdigit() or adharcard.isdigit():
#         # with open("accounts.txt","a") as f:
#         #     f.write(f'name = {name},address = {address},phone = {phone},email = {email},'
#         #             f'DOB = {datevalue.get()}/{monthvalue.get()}/{yearvalue.get()},age = {age},'
#         #             f'adharcard = {adharcard},password = {password}\n,gender ={gender},account type = {account_type},\n')
#         #     tmsg.showinfo("CONGRATULATIONS","YOUR ACCOUNT HAS SUCCESSFULLY CREATED")
#     # else :
#     #     tmsg.showerror("ERROR",'YOU HAVE GIVEN THE WRONG INPUT PLEASE CHECK AGAIN')
#
#     #validtions or exception handling for our code
#
#
#     if name =="" or address == "" or phone == "" or email == "" or age == "" or adharcard == "" or password ==""\
#             or gender == "" or account_type=="" or date_var == "" or month_var=="" or year_var =="":
#             tmsg.showerror("Alert","NO Arguement are given plzz check again")
#             # if name.isalpha() or phone.isdigit() or address.isalnum() or age.isdigit() or adharcard.isdigit():
#             #     return True
#             # else:
#             #     tmsg.showwarning("Alert!", "Wrong arguements are given please check again!")
#     elif len(phone) > 10:
#         tmsg.showwarning("PHONE NO.LIMIT EXCEEDED",'Mobile number must be less than 10 digit no.')
#     elif len(phone) < 10:
#         tmsg.showwarning("INCOMPLETE NUMBER","Your mobile no. must be less than 10")
#     elif len(adharcard) > 12:
#         tmsg.showwarning("INCORRECT ADHAR-NO.","Your entered adharcard no. is incorrect please check again")
#     elif len(adharcard) < 12:
#         tmsg.showwarning("INCORRECT ADHAR-NO.","Your entered adharcard no. is incorrect please check again")
#     elif len(date_var) < 2:
#         tmsg.showwarning("INCORRECT DATE","Please check your date again")
#     elif len(date_var) > 2:
#         tmsg.showwarning("INCORRECT DATE","Please check your date again")
#     elif len(month_var) > 2:
#         tmsg.showwarning("INCORRECT MONTH","Please check your date again")
#     elif len(date_var) < 2:
#         tmsg.showwarning("INCORRECT DATE","Please check your date again")
#     elif len(year_var) > 4:
#         tmsg.showwarning("INCORRECT YEAR","Please check your year again")
#     elif len(year_var) < 4:
#         tmsg.showwarning("INCORRECT DATE","Please check your date again")
#     else:
#         with open("accounts.txt","a") as f:
#             f.write(f'no of entries = {count} \n ,name = {name},address = {address},phone = {phone},email = {email},'
#             f'DOB = {datevalue.get()}/{monthvalue.get()}/{yearvalue.get()},age = {age},'
#             f'adharcard = {adharcard},password = {password}\n,gender ={gender},account type = {account_type},\n \n')
#         tmsg.showinfo("CONGRATULATIONS","YOUR ACCOUNT HAS SUCCESSFULLY CREATED")
#
#     # #we are using adharcard value to differentiate our users..
#     # for adharcard_check in all_accounts:
#     #     if adharcard == adharcard_check:
#     #         tmsg.showerror("ALERT-SAME ACCOUNT DETECTED","Account already exists")
#     #         return
#     #     elif len(phone) > 10:
#     #         tmsg.showerror("PHONE NO.LIMIT EXCEEDED",'Mobile number must be less than 10 digit no.')
#     #     elif len(phone) < 10:
#     #         tmsg.showerror("INCOMPLETE NUMBER","Your mobile no. must be less than 10")
#     #     elif len(adharcard) > 12:
#     #         tmsg.showerror("INCORRECT ADHAR-NO.","Your entered adharcard no. is incorrect please check again")
#     #     elif len(adharcard) < 12:
#     #         tmsg.showerror("INCORRECT ADHAR-NO.","Your entered adharcard no. is incorrect please check again")
#     #     elif len(date_var) < 2:
#     #         tmsg.showerror("INCORRECT DATE","Please check your date again")
#     #     elif len(date_var) > 2:
#     #         tmsg.showerror("INCORRECT DATE","Please check your date again")
#     #     elif len(month_var) > 2:
#     #         tmsg.showerror("INCORRECT MONTH","Please check your date again")
#     #     elif len(date_var) < 2:
#     #         tmsg.showerror("INCORRECT DATE","Please check your date again")
#     #     elif len(year_var) > 4:
#     #         tmsg.showerror("INCORRECT YEAR","Please check your year again")
#     #     elif len(year_var) < 4:
#     #         tmsg.showerror("INCORRECT DATE","Please check your date again")
#     #     else:
#     #         with open("accounts.txt","a") as f:
#     #             f.write(f'name = {name},address = {address},phone = {phone},email = {email},'
#     #             f'DOB = {datevalue.get()}/{monthvalue.get()}/{yearvalue.get()},age = {age},'
#     #             f'adharcard = {adharcard},password = {password}\n,gender ={gender},account type = {account_type},\n')
#     #         tmsg.showinfo("CONGRATULATIONS","YOUR ACCOUNT HAS SUCCESSFULLY CREATED")
#
#     count +=1

    # for adhar_check in all_accounts:
    #     if adharcardvalue.get()== adhar_check:
    #         tmsg.showerror("Error","User already exists")
    #         return False
    #     else:
    #         with open("accounts.txt", "a") as f:
    #             f.write(f'''no of entries = \n ,name = {namevalue.get()},address = {addressvalue.get()},phone = {phonevalue.get()},email = {emailvalue.get()},'
    #                     f'DOB = {datevalue.get()}/{monthvalue.get()}/{yearvalue.get()},age = {agevalue.get()},'
    #                     f'adharcard = {adharcardvalue.get()},password = {passwordvalue.get()}\n,gender ={gendervalue.get()},account type = {accountvalue.get()},\n \n''')
    #         tmsg.showinfo("CONGRATULATIONS", "YOUR ACCOUNT HAS SUCCESSFULLY CREATED")
    #         return True
    #     break

def log_in():
    window = Toplevel(root)
    window.title("Log-In ACCOUNT")
    #window = Tk()
    window.state('zoomed')
    
    def exitf():
        exit()

    def show_frame(frame):
        frame.tkraise()

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    page1 = Frame(window)
    page2 = Frame(window)
    page3 = Frame(window)
    page4 = Frame(window)

    global page1_bg_img
    for frame in (page1, page2, page3,page4):
        frame.grid(row=0, column=0, sticky='nsew')

    # ==================page-1 code========================================

    page1_bg_img = ImageTk.PhotoImage(file="bg2.jpg")

    bg_page1 = Label(page1, image=page1_bg_img)
    bg_page1.pack()

    frame1_title = Label(page1, text='Selct the above options for respective log-in', font='times 35')
    frame1_title.pack(fill='both', expand=True, anchor="nw")

    frame1_btn = Button(page1, text='User Log-In', font='times 25', width=30, height=2,
                        command=lambda: show_frame(page2))
    frame1_btn.place(x=600, y=250)

    frame1_btn = Button(page1, text='Admin Log-In', font='times 25', width=30, height=2,
                        command=lambda: show_frame(page3))
    frame1_btn.place(x=600, y=380)

    # ==================page-2 code (User login)======================================
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


    #===========================initailizing our variables ==========================
    global txtuservar,txtadharvar,txtpassvar
    txtuservar = StringVar()
    txtadharvar = StringVar()
    txtpassvar = StringVar()
    txtuser = Entry(Login_frame, bd=5, relief=SUNKEN,textvariable = txtuservar, font="Lucida 20 bold").grid(row=1, column=2, padx=10)

    adhar_lbl = Label(Login_frame, text="ADHARCARD:", image=adhar_img, compound=LEFT,
                      font='comicsans 15 bold', bg="white").grid(row=2, column=0, pady=5)
    txtadhar = Entry(Login_frame, bd=5, relief=SUNKEN,textvariable = txtadharvar, font="Lucida 20 bold").grid(row=2, column=2, padx=10)

    pass_lbl = Label(Login_frame, text="PASSWORD:", image=pass_lock_img, compound=LEFT,
                     font='comicsans 15 bold', bg="white").grid(row=3, column=0, pady=5)
    txtpass = Entry(Login_frame, bd=5, relief=SUNKEN,textvariable = txtpassvar, font="Lucida 20 bold").grid(row=3, column=2, padx=10)

    # ========================Buttons=========================================
    login_btn = Button(Login_frame, image=loginbutton_img,command=lambda: show_frame(page4),borderwidth=0, background="white")
    login_btn.grid(row=4, column=2, pady=40)

    exit_btn = Button(Login_frame, image=exitbutton_img, command=exitf, borderwidth=0, background="white")
    exit_btn.grid(row=4, column=0, pady=40)

    # =======================creating back button to swith through frames=============================
    frame2_btn = Button(page2, image=backbutton_page2_img, borderwidth=0, background="yellow",
                        command=lambda: show_frame(page1))
    frame2_btn.place(x=10, y=8)

    # ==================page-3 code (Admin log-in)=========================================

    global admin_name_logo,admin_main_logo,wlc_admin,backbutton_img,admin_login_button,bg_img_admin
    # ====================images admin frame ===============================
    admin_name_logo = ImageTk.PhotoImage(file="admin1.png")
    admin_main_logo = PhotoImage(file="adminuser.png")
    wlc_admin = PhotoImage(file="welcome1.png")
    backbutton_img = PhotoImage(file="backimage_button.png")
    admin_login_button = ImageTk.PhotoImage(file="admin_login_button1.png")

    # ======================to set bg image for admin login page================
    bg_img_admin = ImageTk.PhotoImage(file="account_bg.2.jpg")
    bg_admin = Label(page3, image=bg_img_admin)
    bg_admin.pack()
    admin_title = Label(page3, text="Admin Log-In", font="Impact 45 ", bg="yellow", relief=SUNKEN,
                        borderwidth=8)
    admin_title.place(x=0, y=0, relwidth=1)  # relwidth is used to adjust text according to the window

    # ================creating admin frame in page 3======================
    admin_frame = Frame(page3, bg='white')
    admin_frame.place(x=520, y=110)

    # =================Labels and Entry widgets for admin form=================
    wlc_lbl = Label(admin_frame, image=wlc_admin, bg="white").grid(row=0, columnspan=4)
    admin_logo = Label(admin_frame, image=admin_name_logo, bg="white").grid(row=1, columnspan=4)
    admin_user_logo = Label(admin_frame, image=admin_main_logo, bg="white").grid(row=2, columnspan=4)

    admin_lbl_id = Label(admin_frame, text="ADMIN-ID:", image=log_user_img, compound=LEFT,
                         font='comicsans 15 bold', bg="white").grid(row=3, column=0)
    entry_admin_lbl_id = Entry(admin_frame, bd=5, relief=SUNKEN, font="Lucida 20 bold").grid(row=3, column=1, padx=7,
                                                                                             pady=4)

    admin_lbl_password = Label(admin_frame, text="PASSWORD:", image=pass_lock_img, compound=LEFT,
                               font='comicsans 15 bold', bg="white").grid(row=4, column=0, pady=2)
    entry_admin_lbl_password = Entry(admin_frame, bd=5, relief=SUNKEN, font="Lucida 20 bold").grid(row=4, column=1,
                                                                                                   padx=7)

    # ===================================Button for admin login==================

    admin_button = Button(admin_frame, image=admin_login_button, borderwidth=0, background="white")
    admin_button.grid(row=5, columnspan=4)

    # =======================creating back button to swith through frames=============================

    frame3_btn = Button(page3, image=backbutton_img, borderwidth=0, background="yellow",
                        command=lambda: show_frame(page1))
    frame3_btn.place(x=10, y=8)

    #=========================page 4 =====================================================
    
    def user_details():
       showvalues = Frame(page4,width = 900 , height = 900)
       login_name = txtuservar.get()
       file = open(login_name, 'r+')
       file_data = file.read()
       details = file_data.split('\n')
       phoneInStars = details[5]       
       Label(showvalues,text = "Hello, " + details[0]+"!",font = 'Calibri 40 bold').place(x = 44,y = 50)
       Label(showvalues,text = "Phone No: *******"+phoneInStars[7]+phoneInStars[8]+phoneInStars[9],font = 'Calibri 20',).place(x = 44,y = 140)
       Label(showvalues,text = "Address: "+details[6],font = 'Calibri 20',).place(x = 44,y = 170)
       showvalues.place(x = 500,y = 100)
    
    def showBalance():
        showBalFrame = Frame(page4,width = 900 , height = 200)
        login_name = txtuservar.get()
        file = open(login_name, 'r+')
        file_data = file.read()
        details = file_data.split('\n')
        Label(showBalFrame,text = "Your Current Balance is: ₹ "+details[10],fg="green",font = 'Calibri 20').place(x = 44,y = 10)
        showBalFrame.place(x = 500,y = 500)
    
    def finish_deposit():
        if amount.get() == "":
            deposit_notif.config(text='Amount is required!',fg="red")
            return
        if float(amount.get()) <=0:
            deposit_notif.config(text='Negative currency is not accepted', fg='red')
            return
        login_name = txtuservar.get()
        file = open(login_name, 'r+')
        file_data = file.read()
        details = file_data.split('\n')
        current_balance = details[10]
        updated_balance = current_balance
        updated_balance = float(updated_balance) + float(amount.get())
        file_data       = file_data.replace(current_balance, str(updated_balance))
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        file.close()
    
        current_balance_label.config(text="Current Balance : ₹ "+str(updated_balance),fg="green")
        deposit_notif.config(text='Balance Updated', fg='green')
    
    def deposit():
    #Vars
        global amount
        global deposit_notif
        global current_balance_label
        login_name = txtuservar.get()
        amount = StringVar()
        file   = open(login_name, "r")
        file_data = file.read()
        user_details = file_data.split('\n')
        print(user_details)
        details_balance = user_details[10]
        #Deposit Screen
        deposit_screen = Toplevel(root)
        deposit_screen.title('Deposit')
        deposit_screen.geometry("750x600")
        
        mframe2 = Frame (deposit_screen,width = 700,height = 100,highlightbackground = 'grey',highlightthickness = 2,relief = SUNKEN,bg = "green")
        Label(mframe2,text = " Grow more ",font = 'Lucida 40 bold',bg = 'green',fg = 'white').place(x = 44,y = 10)
        Label(mframe2,text = " Since 1992 ",font = 'Lucida 10 bold',bg = 'green').place(x = 60,y = 70)
        mframe1.pack(padx = 20,pady = 5,fill = 'both')
        #Label        
        Label(deposit_screen, text="Deposit", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
        current_balance_label = Label(deposit_screen, text="Current Balance : ₹"+details_balance, font=('Calibri',12))
        current_balance_label.grid(row=1,sticky=W)
        Label(deposit_screen, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
        deposit_notif = Label(deposit_screen,font=('Calibri',12))
        deposit_notif.grid(row=4, sticky=N,pady=5)
        #Entry
        Entry(deposit_screen, textvariable=amount).grid(row=2,column=1)
        #Button
        Button(deposit_screen,text="Finish",font=('Calibri',12),command=finish_deposit).grid(row=3,sticky=W,pady=5)
    
    def finish_withdraw():
        if withdraw_amount.get() == "":
            withdraw_notif.config(text='Amount is required!',fg="red")
            return
        if float(withdraw_amount.get()) <=0:
            withdraw_notif.config(text='Negative currency is not accepted', fg='red')
            return
        
        login_name = txtuservar.get()
        file = open(login_name, 'r+')
        file_data = file.read()
        details = file_data.split('\n')
        current_balance = details[10]
    
        if float(withdraw_amount.get()) >float(current_balance):
            withdraw_notif.config(text='Insufficient Funds!', fg='red')
            return
    
        updated_balance = current_balance
        updated_balance = float(updated_balance) - float(withdraw_amount.get())
        file_data       = file_data.replace(current_balance, str(updated_balance))
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        file.close()

        current_balance_label.config(text="Current Balance : ₹"+str(updated_balance),fg="green")
        withdraw_notif.config(text='Balance Updated', fg='green')
    
    def withdraw():
     #Vars
        global withdraw_amount
        global withdraw_notif
        global current_balance_label
        withdraw_amount = StringVar()
        login_name = txtuservar.get()
        file   = open(login_name, "r")
        file_data = file.read()
        user_details = file_data.split('\n')
        details_balance = user_details[10]
        #Deposit Screen
        withdraw_screen = Toplevel(root)
        withdraw_screen.title('Withdraw')
        withdraw_screen.geometry("750x600")
        #Label
        Label(withdraw_screen, text="Deposit", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
        current_balance_label = Label(withdraw_screen, text="Current Balance : ₹ "+details_balance, font=('Calibri',12))
        current_balance_label.grid(row=1,sticky=W)
        Label(withdraw_screen, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
        withdraw_notif = Label(withdraw_screen,font=('Calibri',12))
        withdraw_notif.grid(row=4, sticky=N,pady=5)
        #Entry
        Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2,column=1)
        #Button
        Button(withdraw_screen,text="Finish",font=('Calibri',12),command=finish_withdraw).grid(row=3,sticky=W,pady=5)

    title1 = Label(page4, text="Welcome to our page 4", font="Impact 45 ", bg="yellow", fg="orange", relief=SUNKEN,
                   borderwidth=8)
    title1.place(x=0, y=0, relwidth=1)  # relwidth is used to adjust text according to the window
    page4btn1 = Button(page4, text='Personal-Details', command = user_details,font='times 25', width=25, height=2).place(x=25, y=160)
    page4btn2 = Button(page4, text='Deposit', command = deposit,font='times 25', width=25, height=2).place(x=25, y=260)
    page4btn3 = Button(page4, text='Withdraw', command = withdraw,font='times 25', width=25, height=2).place(x=25, y=360)
    page4btn4 = Button(page4, text='Check-Balance',command = showBalance, font='times 25', width=25, height=2).place(x=25, y=460)

    #showvalues = Frame(page4,bg = "azure",width = 900 , height = 900)
    #showvalues.place(x = 500,y = 100)
    
    
    
    def user_login():
        all_accounts = os.listdir()
        
        login_name = txtuservar.get()
        login_adharcard = adharcardvalue.get()
        login_password = passwordvalue.get()

        if login_name=="" or login_adharcard == "" or login_password=="":
            tmsg.showerror("Alert","all feilds are required!")
            return


        for name_check in all_accounts:
            if name_check == login_name:
                file = open(login_name, "r")
                file_data = file.read()
                file_data = file_data.split('\n')
                password = file_data[1]
                if login_password == password:
                    Label(page4,text = "Dashboard",font = "Impact 45 ").place(x = 320 , y= 10)
                    wlc = Label(page4,text = "welcome user " ,font = 'comicsans 12 green')
                    wlc.place(x = 400, y = 300)
                    return

                else:
                    tmsg.showerror("Error","Check password!")
                    return
                
        tmsg.showerror(fg="red", text="No account found !!")
        return







    show_frame(page1)




#===================== Function for the validation of phone number ==============
# def validate_phone(user_phone):
#     if user_phone.isdigit():
#         return True
#     elif user_phone == "":
#         return True
#     else:
#         tmsg.showwarning("Alert!","Only digits are allowed please check your phone number again")
#         return False
#===================    CALL BACK FUCTIONS ========================


#
# #================== Function for the validation of the adharcard=================
# def validate_adhar(user_adhar):
#     if user_adhar.isdigit():
#         return True
#     elif user_adhar == "":
#         return True
#     else:
#         tmsg.showwarning("Alert!","Only digits are allowed please check your phone number again")
#         return False
#
# #============Function for the valiation of the email(We use regular expressions)===============
# def isValidEmail(user_email):
#     if len(user_email) > 7:
#         if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",user_email) !=None:
#             return True
#         else:
#             tmsg.showwarning("Alert!","Invalid Email please check your email again")
#             return False
#     else:
#         tmsg.showwarning("Alert!", "Invalid Email please check your email again")
#         return False
#
# #============================Validations for all the fields ============================
# def validateAllFields():
#     if namevalue.get()=="" or addressvalue.get()==""or phonevalue.get()==""or agevalue.get()=="" or \
#      adharcardvalue.get()=="" or passwordvalue.get()=="" or \
#      datevalue.get()=="" or monthvalue.get()=="" or yearvalue.get()=="":
#         tmsg.showerror("Error!","All fields are required")
#     elif emailvalue.get()=="":
#         status = isValidEmail(emailvalue.get())
#         if (status):
#             return True
#     else:
#         with open("accounts.txt", "a") as f:
#             f.write(f'no of entries = \n ,name = {namevalue.get()},address = {addressvalue.get()},phone = {phonevalue.get()},email = {emailvalue.get()},'
#                     f'DOB = {datevalue.get()}/{monthvalue.get()}/{yearvalue.get()},age = {agevalue.get()},'
#                     f'adharcard = {adharcardvalue.get()},password = {passwordvalue.get()}\n,gender ={gendervalue.get()},account type = {accountvalue.get()},\n \n')
#         tmsg.showinfo("CONGRATULATIONS", "YOUR ACCOUNT HAS SUCCESSFULLY CREATED")









#================================================      MAIN GUI      ============================================
def create_acc():
#     def validate_name(user_name):
#         if user_name.isalnum():
#             return True
#             print("Successful")
#         else:
#             tmsg.showwarning("Invalid Input!", "Please Enter the correct name")
#             print("Unsucessful")

    global namevalue,addressvalue,phonevalue,emailvalue,agevalue,adharcardvalue,passwordvalue,gendervalue,accountvalue
    global datevalue,monthvalue,yearvalue
    # We created new window using toplevel function
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

    #combobox
    mycombo = ttk.Combobox(register_screen,value = ls)
    mycombo.current(0)
    mycombo.bind("<<comboboxsselected>>",comboclick)
    mycombo.place(x = 252,y = 187)


    #Labels
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

    #Entry box variables
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

    #Entry box
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

    #============== NAME VALIDATION FUNCTION================
    # valid_name = register_screen.register(validate_name)
    # Entry_name.config(validate = "key",validatecommand = (validate_name,'%P'))

    #
    # #================ PHONE VALIDATION FUNCTION================
    # #validations (We have to create a callback function)
    # valid_phone = register_screen.register(validate_phone)
    #
    # # %P  = passes the input value to callback function
    # Entry_phone.config(validate = "key",validatecommand = (validate_phone,'%P'))
    #
    # #================ ADHARCARD VALIDATION FUNCTION==============
    # valid_adhar = register_screen.register(validate_adhar)
    # Entry_adhar.config(validate = "key",validatecommand = (validate_adhar,'%P'))



    gendervalue.set("male")
    #Radio button for gender
    r1 = Radiobutton(re_frame2,text = 'male', variable = gendervalue, value = "male", bg="azure")
    r2 = Radiobutton(re_frame2,text = 'female',variable = gendervalue,value = "female", bg="azure")
    r1.place(x = 249, y = 130)
    r2.place(x = 320 , y = 130)

    #Radio button for account type
    accountvalue.set("saving")
    r3 = Radiobutton(re_frame2,text = 'CURRENT', variable = accountvalue, value = "current", bg="azure")
    r4 = Radiobutton(re_frame2,text = 'SAVING',variable = accountvalue,value = "saving", bg="azure")
    r3.place(x = 249, y = 310)
    r4.place(x = 350 , y = 310)

    #
    # Button(re_frame2, text="SUBMIT", font="comicsans 12",bg = "green",fg = "white",
    #        width=20, command=submit).place(x=249, y=350)

    Button(re_frame2, text="SUBMIT",command = submit, font="comicsans 12",bg = "green",fg = "white",
           width=20).place(x=249, y=350)

    re_frame2.pack(fill = 'both')



#==============================main window frame of the first page========================
mframe1 = Frame (root,width = 700,height = 100,highlightbackground = 'grey',highlightthickness = 2,relief = SUNKEN,bg = "green")
Label(mframe1,text = " Grow more ",font = 'Lucida 40 bold',bg = 'green',fg = 'white').place(x = 44,y = 10)
Label(mframe1,text = " Since 1992 ",font = 'Lucida 10 bold',bg = 'green').place(x = 60,y = 70)
mframe1.pack(padx = 20,pady = 5,fill = 'both')

#=====================changing Image of main window=========================

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

img4=ImageTk.PhotoImage(Image.open("img4.jpg"))
img4 = Image.open("img4.jpg")
img4= img4.resize((400,300))
img4 = ImageTk.PhotoImage(img4)
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
    elif x==4:
        l.config(image=img4)
    #you can do it for thousands of images
    #now increase the count by one
    x+=1
    #set images to work automatically by "after" feature in tkinter
    #after view image one by one after the given time i.e 2000 mil sec.
    root.after(2000,move)
move()


Button(root,text = 'Create Account',bg = 'yellow green',command = create_acc).place(x = 100,y = 434)
Button(root,text = 'Log-In',bg = 'yellow green',command = log_in).place(x = 230,y = 434)





root.mainloop()
