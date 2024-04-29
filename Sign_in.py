from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Store_admin import *
from Store_user import *
from PIL import Image,ImageTk



root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.config(bg='white')
root.resizable(False, False)


def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        page_admin = Tk()
        obj = admin_store(page_admin)
        root.destroy()
        page_admin.mainloop()
    elif username!= 'admin' or password != '1234':
        page_admin = Tk()
        obj = user_store(page_admin)
        root.destroy()
        page_admin.mainloop()

    

img=PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text='Sign in', fg="#57a1f8", font=('Pacifico', 23, 'bold'))
heading.place(x=100, y=5)

#######--------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name =='':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Pacifico', 11))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame,width=295, height=2, bg='black').place(x=25, y=107)


def on_enter_pass(e):
    code.delete(0, 'end')
    code.config(show="*")

def on_leave_pass(e):
    name=code.get()
    if name =='':
        code.insert(0, 'Password')
        code.config(show="")

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Pacifico', 11))
code.place(x=30, y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter_pass)
code.bind('<FocusOut>', on_leave_pass)
 
Frame(frame,width=295, height=2, bg='black').place(x=25, y=177)


Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
label=Label(frame, text="Don't have an account !", fg='black', bg='white', font=('Pacifico', 11))
label.place(x=75, y=270)

Sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
Sign_up.place(x=235, y=270)


root.mainloop()