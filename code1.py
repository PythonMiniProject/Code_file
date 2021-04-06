from tkinter import *
import tkinter.messagebox as tmsg 
from PIL import Image,ImageTk
import os
root = Tk()
root.title("BANKING PROJECT")

def login():
    pass 


def finish():
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
        return
    print("well done")
     
#agar ye nai likhta toh global variable error de rha hai I dont know why but de rha h
# none remove karne se error aa rha hai        
# namevalue=None
# phonevalue=None
# agevalue=None
# statevalue=None
# districtvalue=None
# pincodevalue=None
# adharcardvalue=None
# passwordvalue =None


#aur ye dusra way hai i don't know both are giving me errors 
namevalue=""
phonevalue=""
agevalue=""
statevalue=""
districtvalue=""
pincodevalue=""
adharcardvalue=""
passwordvalue =""


#top level used to create a new pop-up window    
def register():
        #resiter Screen
    register_screen = Toplevel(root)
    register_screen.title("CREATE ACCOUNT")

    
    #we have to globalize the variable to use it in our other functions 
    global namevalue
    global phonevalue
    global agevalue
    global statevalue
    global districtvalue
    global pincodevalue
    global adharcardvalue
    #Entries for Labels 
    Entry_dict = {
    'namevalue' : StringVar(),
    'phonevalue' : StringVar(),   
    'agevalue' : StringVar(),
    'statevalue' : StringVar(),
    'districtvalue' : StringVar(),
    'pincodevalue' : StringVar(),
    'adharcardvalue' :StringVar(),
    }
    #textvarialbes for our entries in form of dictionary
    counter=1
    for i in Entry_dict:
        ent = 'entry'+i
        ent = Entry(register_screen,textvariable = Entry_dict[i],font="comicsans 16 bold")
        ent.grid(column=1,row = counter,pady = 4)
        counter+=1
    

    #Entry widget without using loops uproach (uncomment karke check karna toh kar lo )
    # namevalue = StringVar()
    # phonevalue = StringVar()   
    # agevalue = StringVar()
    # statevalue = StringVar()
    # districtvalue = StringVar()
    # pincodevalue = StringVar()
    # adharcardvalue =StringVar()
    # passwordvalue = StringVar() 
    # Entry(register_screen,textvariable =namevalue,font="comicsans 16 bold").grid(row = 0,column = 1,pady=4)
    # Entry(register_screen,textvariable =phonevalue,font="comicsans 16 bold").grid(row = 0,column = 1,pady=4)
    # Entry(register_screen,textvariable =agevalue,font="comicsans 16 bold").grid(row = 0,column = 1,pady=4)
    # Entry(register_screen,textvariable =statevalue,font="comicsans 16 bold").grid(row = 0,column = 1,pady=4)
    # Entry(register_screen,textvariable =districtvalue,font="comicsans 16 bold").grid(row = 0,column = 1,pady=4)
    # Entry(register_screen,textvariable =pincodevalue,font="comicsans 16 bold").grid(row = 0,column = 1,pady=4)
    # Entry(register_screen,textvariable =adharcardvalue,font="comicsans 16 bold").grid(row = 0,column = 1,pady=4)
    # Entry(register_screen,textvariable =passwordvalue,font="comicsans 16 bold").grid(row = 0,column = 1,pady=4)

    #adding labels to our register screeen
    Label(root,text = "Please Enter your details below to Create an Account",font ="lucida 12 bold").grid(row = 0,sticky = N,pady = 8)
    ls = ['Name','Phone-Number','Age','State','District','PINCODE','Adharcard','Password']
    i=1
    for index,item in enumerate(ls):
        create = Label(register_screen,text =item,font="comicsans 10 bold")
        create.grid(row=i,sticky = W)
        i+=1



    #to encrpt password,we created a diffrent variable out of the for loop 
   
    Entry(register_screen,text = "Password",textvar = passwordvalue,show="*").grid(row = 8,column = 1,pady=4)

    #Buttons 
    Button(register_screen,text = "Register",command = finish,font = "comicsans 10 bold").grid(row = 9,sticky = N,pady = 10)


img = Image.open("a.png")
img = img.resize((200,200))
img = ImageTk.PhotoImage(img)

#Main window labels
Label(root,text= "LAXMII CHIT FUND",font = "lucida 20 bold").grid(row = 0 ,sticky = N,pady = 5)
Label(root,text= "21 din mai paisa double",font = "lucida 10 bold").grid(row = 1 ,sticky = N)

#Label form image module
Label(root,image = img).grid(row =2,sticky = N,pady = 15)

#Creating login and register Button 
Button(root,text = "Create Account",font = "comicsans 12",width=20,command =register).grid(row = 3,sticky = N,pady = 2)
Button(root,text = "Log-In",font = "comicsans 12",width = 20,command = login).grid(row = 4,sticky = N)


root.mainloop()
