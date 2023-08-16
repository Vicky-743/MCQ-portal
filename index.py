from tkinter import *
from tkinter import messagebox as mb
import pymysql
import re
import json
win =Tk()
def Login():
    # pass
    messagebox.showinfo('showinfo',"Welcome to Home page")
    conobj= pymysql.connect(host='localhost',user='root',password='',port=3306)
    curobj=conobj.cursor()
    curobj.execute('use MCQPORTAL')
    x=username.get()
    y=password.get()
    curobj.execute('Select username ,password from register')
    record=conobj.fetchall()
    for u,p in record:
        if u==x and p==y:
            messagebox.showinfo('showinfo',"welcome to login page")
            win2=TK()
            win2.title("MCQ")
            
            win2('780x550')
            win2.mainloop()
        # else:        #     messagebox.showinfo
    print(x," ",y)
    curobj.close()
    conobj.close()
def Exit():
    # pass
    win.destroy()
def New():
    # pass
    messagebox.showinfo('showinfo',"Welcome to Resgistration page")
    def Submit():
        
        #getting details from persepective entry box
        a1=username.get()
        b1=email.get()
        c1=str(var.get())
        d1=npassword.get()
        e1=cnpassword.get()
        print(a1,b1,c1,d1,e1)
        #creating mysql object
        conobj=pymysql.connect(host="localhost",user="root",password='',port=3306)
        
        #creating cursor obj
        curobj=conobj.cursor() 
        
        checkP="^[a-zA-Z0-9]{8,16}$"
        Tr=re.match(checkP,d1)
        #Executing query
        curobj.execute('use MCQPORTAL;') 
        if int(c1)==0:
            c1="male"
        else:
            c1="Female"
        if len(d1)>= 8 and len(d1)<=16:
            if re.findall(checkP,d1):
                curobj.execute('insert into register values("' +username.get()+ '","' +email.get()+ '","' +str(var.get())+ '","' +npassword.get() + '","' +cnpassword.get()+ '")')
                # print('insert into register values("' +a1+ '","' +b1+ '","' +c1+ '","' +d1+ '","' +e1+ '")')

                conobj.commit()
                curobj.close()
                conobj.close()
        else:
            messagebox.showinfo('password length between ')
        print(a1," ",b1," ",c1,"  ",d1," ",e1)
    def Reset():
        username.delete(0,END)
        email.delete(0,END)
        npassword.delete(0,END)
        cnpassword.delete(0,END)
    
    win1=Tk()
    win.title("Registration page")
    win1.geometry('45x450')
    win1.maxsize(height='600',width='750')
    win1.minsize(height='600',width='750')
    Label(win1,text="Please Registration Here",font=('bold',25),bg="black",fg="green",width="25",height="2") .place(x=150,y=50)
    l1=Label(win1,text="Enter Regno/user Id",font=('bold',15),bg="white",fg="black",width="16",height="1") .place(x=100,y=150)
    username=Entry(win1,font=('bold',15),bg="white",fg="black")
    username.place(x=350,y=150)
    l2=Label(win1,text="Enter email Id",font=('bold',15),bg="white",fg="black",width="16",height="1") .place(x=100,y=200)
    email=Entry(win1,font=('bold',15),bg="white",fg="black")
    email.place(x=350,y=200)

    l3=Label(win1,text="select gender",font=('bold',15),bg="white",fg="black",width="16",height="1") .place(x=100,y=250)
    var=IntVar()
    r1=Radiobutton(win1,text="M",value=0)
    r1.place(x=350,y=255)
    r2=Radiobutton(win1,text="F",value=1)
    r2.place(x=400,y=255)

    l4=Label(win1,text="set new password",font=('bold',15),bg="white",fg="black",width="16",height="1") .place(x=100,y=300)

    npassword=Entry(win1,font=('bold',15),bg="white",fg="black",show="*")
    npassword.place(x=350,y=300)

    l5=Label(win1,text="confirm password",font=('bold',15),bg="white",fg="black",width="16",height="1") .place(x=100,y=350)

    cnpassword=Entry(win1,font=('bold',15),bg="white",fg="black",show="*")
    cnpassword.place(x=350,y=350)

    #login button
    submit=Button(win1,text="Submit",font=('bold',12),bg="red",fg="white",command=Submit).place(x=350,y= 400)
    #exiting button
    reset=Button(win1,text="Reset",font=('bold',12),bg="red",fg="white",command=Reset).place(x=450,y=400)
    win1.mainloop()

#password field
# l2=Label(win,text="Enter password",font=('bold',15),bg="white",fg="black",width="16",height="1") .grid(row=7,column=1)
# password=Entry(win,font=('bold',15),bg="white",fg="black",show="*")
# password.grid(row=7,column=2)
win.title("Login page")
win.geometry('450x600')
win.maxsize(height='600',width='750')
win.minsize(height='600',width='750')

#first label
Label(win,text="Please Login Here",font=('bold',25),bg="black",fg="green",width="25",height="2") .place(x=150,y=50)
#username field
l1=Label(win,text="Enter Regno/user Id",font=('bold',15),bg="white",fg="black",width="16",height="1") .place(x=100,y=150)
username=Entry(win,font=('bold',15),bg="white",fg="black")
username.place(x=350,y=150)
#password field
l2=Label(win,text="Enter password",font=('bold',15),bg="white",fg="black",width="16",height="1") .place(x=105,y=200)
password=Entry(win,font=('bold',15),bg="white",fg="black",show="*")
password.place(x=350,y=200)
#login button
Login=Button(win,text="Sign In",font=('bold',12),bg="red",fg="white",command=Login).place(x=320,y=240)
#exiting button
Exit=Button(win,text="Sign Up",font=('bold',12),bg="red",fg="white",command=Exit).place(x=440,y=240)
#creating new user botton
New=Button(win,text="New User click",font=('bold',12),bg="red",fg="white",height="1",width="20",command=New).place(x=550,y=240)


win.mainloop()

