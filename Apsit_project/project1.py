from tkinter import *
import tkinter.messagebox as tmsg #to import message box
from PIL import Image, ImageTk    # pillow library to vieww images
import os
import datetime
import tkinter as t
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

#def menufunc():
    #pass
def submit():

# we inintialized values of variables in from entrybox
    name = namevalue.get()
    address = addressvalue.get()
    phone = phonevalue.get()
    email = emailvalue.get()
    age = agevalue.get()
    adharcard = adharcardvalue.get()
    password = passwordvalue.get()
    gender = gendervalue.get()
    account_type = accountvalue.get()
    date_var = datevalue.get()
    month_var = monthvalue.get()
    year_var = yearvalue.get()
    all_accounts = os.listdir()

    #else:
        #with open("accounts.txt","a") as f:
            #f.write(f'name = {name}\n,address = {address}\n,phone = {phone}\n,email = {email}\n,age = {age}\n,'
             #       f'adharcard = {adharcard}\n,password = {password}\n,gender ={gender}\n,account type = {account_type},\n')
            #tmsg.showinfo("CONGRATULATIONS","YOUR ACCOUNT HAS SUCCESSFULLY CREATED")

    # if  name.isalpha() or phone.isdigit() or address.isalnum() or age.isdigit() or adharcard.isdigit():
        # with open("accounts.txt","a") as f:
        #     f.write(f'name = {name},address = {address},phone = {phone},email = {email},'
        #             f'DOB = {datevalue.get()}/{monthvalue.get()}/{yearvalue.get()},age = {age},'
        #             f'adharcard = {adharcard},password = {password}\n,gender ={gender},account type = {account_type},\n')
        #     tmsg.showinfo("CONGRATULATIONS","YOUR ACCOUNT HAS SUCCESSFULLY CREATED")
    # else :
    #     tmsg.showerror("ERROR",'YOU HAVE GIVEN THE WRONG INPUT PLEASE CHECK AGAIN')

    #validtions or exception handling for our code
    if name =="" or address == "" or phone == "" or email == "" or age == "" or adharcard == "" or password ==""\
            or gender == "" or account_type=="" or date_var == "" or month_var=="" or year_var =="":
            tmsg.showerror("Alert","NO Arguement are given plzz check again")
            return
    elif len(phone) > 10:
        tmsg.showwarning("PHONE NO.LIMIT EXCEEDED",'Mobile number must be less than 10 digit no.')
    elif len(phone) < 10:
        tmsg.showwarning("INCOMPLETE NUMBER","Your mobile no. must be less than 10")
    elif len(adharcard) > 12:
        tmsg.showwarning("INCORRECT ADHAR-NO.","Your entered adharcard no. is incorrect please check again")
    elif len(adharcard) < 12:
        tmsg.showwarning("INCORRECT ADHAR-NO.","Your entered adharcard no. is incorrect please check again")
    elif len(date_var) < 2:
        tmsg.showwarning("INCORRECT DATE","Please check your date again")
    elif len(date_var) > 2:
        tmsg.showwarning("INCORRECT DATE","Please check your date again")
    elif len(month_var) > 2:
        tmsg.showwarning("INCORRECT MONTH","Please check your date again")
    elif len(date_var) < 2:
        tmsg.showwarning("INCORRECT DATE","Please check your date again")
    elif len(year_var) > 4:
        tmsg.showwarning("INCORRECT YEAR","Please check your year again")
    elif len(year_var) < 4:
        tmsg.showwarning("INCORRECT DATE","Please check your date again")
    else:
        with open("accounts.txt","a") as f:
            f.write(f'name = {name},address = {address},phone = {phone},email = {email},'
            f'DOB = {datevalue.get()}/{monthvalue.get()}/{yearvalue.get()},age = {age},'
            f'adharcard = {adharcard},password = {password}\n,gender ={gender},account type = {account_type},\n')
        tmsg.showinfo("CONGRATULATIONS","YOUR ACCOUNT HAS SUCCESSFULLY CREATED")

    # #we are using adharcard value to differentiate our users..
    # for adharcard_check in all_accounts:
    #     if adharcard == adharcard_check:
    #         tmsg.showerror("ALERT-SAME ACCOUNT DETECTED","Account already exists")
    #         return
    #     elif len(phone) > 10:
    #         tmsg.showerror("PHONE NO.LIMIT EXCEEDED",'Mobile number must be less than 10 digit no.')
    #     elif len(phone) < 10:
    #         tmsg.showerror("INCOMPLETE NUMBER","Your mobile no. must be less than 10")
    #     elif len(adharcard) > 12:
    #         tmsg.showerror("INCORRECT ADHAR-NO.","Your entered adharcard no. is incorrect please check again")
    #     elif len(adharcard) < 12:
    #         tmsg.showerror("INCORRECT ADHAR-NO.","Your entered adharcard no. is incorrect please check again")
    #     elif len(date_var) < 2:
    #         tmsg.showerror("INCORRECT DATE","Please check your date again")
    #     elif len(date_var) > 2:
    #         tmsg.showerror("INCORRECT DATE","Please check your date again")
    #     elif len(month_var) > 2:
    #         tmsg.showerror("INCORRECT MONTH","Please check your date again")
    #     elif len(date_var) < 2:
    #         tmsg.showerror("INCORRECT DATE","Please check your date again")
    #     elif len(year_var) > 4:
    #         tmsg.showerror("INCORRECT YEAR","Please check your year again")
    #     elif len(year_var) < 4:
    #         tmsg.showerror("INCORRECT DATE","Please check your date again")
    #     else:
    #         with open("accounts.txt","a") as f:
    #             f.write(f'name = {name},address = {address},phone = {phone},email = {email},'
    #             f'DOB = {datevalue.get()}/{monthvalue.get()}/{yearvalue.get()},age = {age},'
    #             f'adharcard = {adharcard},password = {password}\n,gender ={gender},account type = {account_type},\n')
    #         tmsg.showinfo("CONGRATULATIONS","YOUR ACCOUNT HAS SUCCESSFULLY CREATED")



def create_acc():
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

    #menubar
    #menubar = Menu(register_screen)
    #m1 = Menu(menubar, tearoff=0)
    #m1.add_command(label="Clear All", command=menufunc)
    #m1.add_command(label="Close", command=menufunc)
    #m1.add_command(label="Print", command=menufunc)
    #m1.add_command(label="Help", command=menufunc)
    #root.config(menu=menubar)
    #menubar.add_cascade(label="file", menu=m1)

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
    Entry(re_frame2,textvariable =namevalue,font="comicsans 10 bold").place(x=250,y= 10)
    Entry(re_frame2, textvariable=addressvalue, font="comicsans 10 bold").place(x=250,y= 40)
    Entry(re_frame2,textvariable =phonevalue,font="comicsans 10 bold").place(x=250,y= 100)
    Entry(re_frame2, textvariable=emailvalue, font="comicsans 10 bold").place(x=250,y= 190)
    Entry(re_frame2,textvariable =agevalue,font="comicsans 10 bold").place(x=250,y= 220)
    Entry(re_frame2,textvariable =adharcardvalue,font="comicsans 10 bold").place(x=250,y= 250)
    Entry(re_frame2,textvariable =passwordvalue,show = "*",font="comicsans 10 bold").place(x=250,y= 280)
    Entry(re_frame2,textvariable = datevalue,font= 'Lucida 10 bold',width = 2).place(x = 250,y = 160)  #dd
    Entry(re_frame2,textvariable = monthvalue, font='Lucida 10 bold', width=2).place(x=275, y=160)  #mm
    Entry(re_frame2,textvariable = yearvalue, font='Lucida 10 bold', width=4).place(x=300, y=160) #yy


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

    #Image inside frame of register window
    #re_img = Image.open("img4.jpg")
    #re_img = re_img.resize((300, 320))
    #re_img = ImageTk.PhotoImage(re_img)
    #Label(re_frame2, image=re_img).place(x=430, y=10)


    #Button(re_frame2,text = 'CURRENT ACCOUNT',bg = "green",fg = "white").place(x = 250,y = 320)
    #Button(re_frame2,text = 'SAVING ACCOUNT',bg = "green",fg = "white").place(x=380, y=320)
    Button(re_frame2, text="SUBMIT", font="comicsans 12",bg = "green",fg = "white",
           width=20, command=submit).place(x=249, y=350)

    re_frame2.pack(fill = 'both')


def log_in():
    login_screen = Toplevel(root)
    login_screen.geometry("750x600")
    login_screen.title("Log-In ACCOUNT")



frame1 = Frame (root,width = 700,height = 100,highlightbackground = 'grey',highlightthickness = 2,relief = SUNKEN,bg = "green")
Label(frame1,text = " Grow more ",font = 'Lucida 40 bold',bg = 'green',fg = 'white').place(x = 44,y = 10)
Label(frame1,text = " Since 1992 ",font = 'Lucida 10 bold',bg = 'green').place(x = 60,y = 70)
frame1.pack(padx = 20,pady = 5,fill = 'both')

#Image of our login window
#frame2 = Frame (root,width = 700,height = 500,highlightbackground = 'grey',highlightthickness = 2,relief = SUNKEN,bg = "orange")
#now set an image for moving

#image Tk used to import jpg images in tk window
img1=ImageTk.PhotoImage(Image.open("img1.jpg"))
img1 = Image.open("img1.jpg")
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
