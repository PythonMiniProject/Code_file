from tkinter import *
import tkinter.messagebox as tmsg 
from PIL import Image,ImageTk
import os
root = Tk()
root.title("BANKING PROJECT")

def login():
    pass 

def finish():
    #No global varss are used we have to declare it with code used in funcitons
    namevalue = StringVar()
    phonevalue = StringVar()   
    agevalue = StringVar()
    statevalue = StringVar()
    districtvalue = StringVar()
    pincodevalue = StringVar()
    adharcardvalue =StringVar()
    passwordvalue = StringVar() 

    name = namevalue.get()
    phone = phonevalue.get()    
    age = agevalue.get() 
    state = statevalue.get() 
    district = districtvalue.get() 
    pincode = pincodevalue.get() 
    adharcard = adharcardvalue.get() 
    password = passwordvalue.get() 
    all_accounts = os.listdir()

    if name=="" or phone==""or age==""or state==""or district==""or pincode==""or adharcard==""or password=="":
        a = tmsg.showinfo("Alert","No arguments are given")
    else:
        with open ("accounts.txt","a") as f:
            # f.write(f'''name = {namevalue.get()}, phone = {phonevalue.get()},age = {agevalue.get()},state = {statevalue.get()},district = {districtvalue.get()},pincode = {pincodevalue.get()},
            #         adharcard = {adharcardvalue.get()},password = {passwordvalue.get()}\n''')
            f.write(f'''name = {name}, phone = {phone},age = {age},state = {state},district = {district},pincode = {pincode},
                    adharcard = {adharcard},password = {password}\n''')
            f.close()

    


def register():

    register_screen = Toplevel(root)
    register_screen.title("CREATE ACCOUNT")
  
    Entry_dict = {
    'namevalue' : StringVar(),
    'phonevalue' : StringVar(),   
    'agevalue' : StringVar(),
    'statevalue' : StringVar(),
    'districtvalue' : StringVar(),
    'pincodevalue' : StringVar(),
    'adharcardvalue' :StringVar(),
    }
    passwordvalue = StringVar()

    counter=1
    for i in Entry_dict:
        ent = 'entry'+i
        ent = Entry(register_screen,textvariable = Entry_dict[i],font="comicsans 16 bold")
        ent.grid(column=1,row = counter,pady = 4)
        counter+=1

    Label(root,text = "Please Enter your details below to Create an Account",font ="lucida 12 bold").grid(row = 0,sticky = N,pady = 8)
    ls = ['Name','Phone-Number','Age','State','District','PINCODE','Adharcard','Password']
    i=1
    for index,item in enumerate(ls):
        create = Label(register_screen,text =item,font="comicsans 10 bold")
        create.grid(row=i,sticky = W)
        i+=1



    Entry(register_screen,text = "Password",textvar = passwordvalue,show="*").grid(row = 8,column = 1,pady=4)

    Button(register_screen,text = "Register",command = finish,font = "comicsans 10 bold").grid(row = 9,sticky = N,pady = 10)

img = Image.open("a.png")
img = img.resize((200,200))
img = ImageTk.PhotoImage(img)

Label(root,text= "LAXMII CHIT FUND",font = "lucida 20 bold").grid(row = 0 ,sticky = N,pady = 5)
Label(root,text= "21 din mai paisa double",font = "lucida 10 bold").grid(row = 1 ,sticky = N)

Label(root,image = img).grid(row =2,sticky = N,pady = 15)

Button(root,text = "Create Account",font = "comicsans 12",width=20,command =register).grid(row = 3,sticky = N,pady = 2)
Button(root,text = "Log-In",font = "comicsans 12",width = 20,command = login).grid(row = 4,sticky = N)



root.mainloop()
