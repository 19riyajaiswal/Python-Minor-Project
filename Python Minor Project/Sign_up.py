from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms & Conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectvity Issue, Please Try Again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','Username Already Exist')
       
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            import Login


def Login():
    signup_window.destroy()
    import Login

signup_window=Tk()
signup_window.geometry('990x600+50+50')
signup_window.title("Signup Page")
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='IMG_20210212_180134.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window)
frame.place(x=300,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Times New Roman',20,'bold'),bg='white',fg='firebrick')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Times New Roman',12,'bold'),bg='white',fg='firebrick')
emailLabel.grid(row=2,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=40,font=('Times New Roman',10,'bold'),fg='white',bg='firebrick')
emailEntry.grid(row=3,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Times New Roman',12,'bold'),bg='white',fg='firebrick')
usernameLabel.grid(row=4,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=40,font=('Times New Roman',10,'bold'),fg='white',bg='firebrick')
usernameEntry.grid(row=5,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Times New Roman',12,'bold'),bg='white',fg='firebrick')
passwordLabel.grid(row=6,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=40,font=('Times New Roman',10,'bold'),fg='white',bg='firebrick')
passwordEntry.grid(row=7,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Times New Roman',12,'bold'),bg='white',fg='firebrick')
confirmLabel.grid(row=8,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry=Entry(frame,width=40,font=('Times New Roman',10,'bold'),fg='white',bg='firebrick')
confirmEntry.grid(row=9,column=0,sticky='w',padx=25)
check=IntVar()

termsandconditions=Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Times New Roman',10,'bold'),
fg='firebrick',bg='white',activebackground='white',activeforeground='firebrick',cursor='hand2',variable=check)
termsandconditions.grid(row=10,column=0,padx=15,pady=10)

signupButton=Button(frame,text='Signup',font=('Times New Roman',16,'bold'),bd=0,bg='firebrick',fg='white',
activebackground='firebrick',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=11,column=0,pady=10)

alreadyaccount=Label(frame,text="Don't have an account?",font=('Open Sans','9','bold'),bg='white',fg='firebrick')
alreadyaccount.grid(row=12,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text="Log in",font=('Open Sans',9,'bold underline')
,bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=Login)
loginButton.place(x=170,y=385)

signup_window.mainloop()