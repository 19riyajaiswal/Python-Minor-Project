from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality Part

def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All fields Are Required',parent=window)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Error','Password and Confirm Password are not matching',parent=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='',database='userdata')
            mycursor=con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, please login with new password',parent=window)
                window.destroy()
    window = Toplevel()
    window.title('Change Password')
    window.geometry('990x600+50+50')
    bgPic = ImageTk.PhotoImage(file='IMG_20210212_180134.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()
    heading_label = Label(window, text='RESET PASSWORD',font=('arial','18','bold'),
    bg='white',fg='magenta')
    heading_label.place(x=380,y=120)

    userlabel = Label(window, text='Username', font=('arial',12,'bold'),bg='white',fg='orchid')
    userlabel.place(x=340,y=180)
    user_entry = Entry(window, width=40, fg='magenta2', font=('arial',11,'bold'),bd=0)
    user_entry.place(x=340,y=210)

    passwordlabel = Label(window, text='New Password', font=('arial',12,'bold'),bg='white',fg='orchid')
    passwordlabel.place(x=340,y=250)
    newpass_entry = Entry(window, width=40, fg='magenta2', font=('arial',11,'bold'),bd=0)
    newpass_entry.place(x=340,y=280)

    confirmpasslabel = Label(window, text='Confirm Password', font=('arial',12,'bold'),bg='white',fg='orchid')
    confirmpasslabel.place(x=340,y=320)
    confirmpass_entry = Entry(window, width=40, fg='magenta2', font=('arial',11,'bold'),bd=0)
    confirmpass_entry.place(x=340,y=350)

    submitButton = Button(window, text='SUBMIT',bd=0,bg='magenta2',fg='white',font=('Open Sans','16','bold'),
    width=19,cursor='hand2',activebackground='magenta2',activeforeground='white',command=change_password)
    submitButton.place(x=340,y=400)    
    window.mainloop()

def signup_page():
    login_window.destroy()
    import Sign_up

def Login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='')
            mycursor=con.cursor()
            
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
            login_window.destroy()
            import Employee        
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
        passwordEntry.config(show='*')       

#Gui Part
login_window=Tk()
login_window.geometry('990x600+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='IMG_20210212_180134.jpg')

login_window.wm_iconbitmap('Employee.ico')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)
heading=Label(login_window,text='USER LOGIN',font=('Times New Roman',23,'bold'),bg='white',fg='firebrick')
heading.place(x=380,y=120)

usernameEntry=Entry(login_window,width=40,font=('Times New Roman',15,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=300,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

passwordEntry=Entry(login_window,width=40,font=('Times New Roman',15,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=300,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2'
,font=('Times New Roman',12,'bold'),fg='firebrick',command=forget_pass)
forgetButton.place(x=570,y=295)

loginButton=Button(login_window,text='Login',font=('Open Sans',15,'bold'),fg='white',bg='firebrick'
,activeforeground='white',activebackground='firebrick',cursor='hand2',bd=0,width=19,command=Login)
loginButton.place(x=300,y=350)

signupLabel=Label(login_window,text="Don't have an account?",font=('Open Sans',9,'bold'),fg='firebrick',bg='white')
signupLabel.place(x=300,y=400)

newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),fg='blue',bg='white'
,activeforeground='blue',activebackground='firebrick',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=450,y=400)

login_window.mainloop()






