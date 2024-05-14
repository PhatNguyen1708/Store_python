from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Store_admin import *
from Store_user import *
from PIL import Image,ImageTk
import json, os.path, ast



def Signin():
    root=Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.config(bg='white')
    root.resizable(False, False)

    def login():
        username = user.get()
        password = code.get()

        try:
            with open ('data/user_data.json', 'r') as file:
                data = json.load(file)

            accountF = False
            for account in data:
                if username == 'admin' and password == '1234':
                    messagebox.showinfo('Sign in', 'Sucessfully sign in')
                    page_admin = Tk()
                    obj = admin_store(page_admin)
                    root.destroy()
                    page_admin.mainloop()
                    return
                elif username.lower() == account["username"].lower() and password == account["password"]:
                    messagebox.showinfo('Sign in', 'Sucessfully sign in')
                    page_user = Tk()
                    obj = user_store(page_user,username)
                    root.destroy()
                    page_user.mainloop()
                    return
            
            if not accountF:
                for account in data:
                    if username == account["username"] and password != account["password"]:
                        messagebox.showerror('Failed', 'Invalid password')
                    elif username != account["username"]:
                        messagebox.showerror("Failed", "User doesn't exist!")
                        break
        except FileNotFoundError:
            messagebox.showerror("Failed", "Don't have any account!")


    def signup_command():
        root.destroy()
        win = Tk()
        win.title("Sign Up")
        win.geometry('925x500+300+200')
        win.configure(bg='#fff')
        win.resizable(FALSE,False)

        def sign_in():
            win.destroy()
            Signin()

        def signup():
            acc=[]
            username = user.get()
            password = code.get()
            comfirm_password = comfirm_code.get()

            if os.path.exists(r'data/user_data.json'):
                with open ('data/user_data.json', 'r') as file:
                    data = json.load(file)
                for account in data:
                    if username.lower() == account["username"].lower():
                        messagebox.showinfo('Failed', 'an account already exists.')
                        return
            if password == comfirm_password and re.fullmatch(r'[A-Za-z0-9_#@$%&*^+=]{8,}',password):
                new_acc = {
                    "username":username,
                    "password":password
                }
                if os.path.exists(r'data/user_data.json'):
                    with open ("data/user_data.json", "r", encoding='utf-8') as file:
                        accounts = json.load(file)
                else:
                    accounts = []
                accounts.append(new_acc)

                with open ("data/user_data.json", "w", encoding='utf-8') as file:
                    json.dump(accounts, file,indent=4,ensure_ascii=False)
                messagebox.showinfo('Sign up', 'Sucessfully sign up')
                sign_in()
            elif password  != comfirm_password:
                messagebox.showerror('Wrong password', "Both Passwword should match")          
            else:
                messagebox.showerror('Weak password', "Password must be at lest 8 characters and contain one upper case letter, one lower case letter and one numberic character")

        img_signup = PhotoImage(file='picture/sign_up.png')
        panel = tk.Label(win, image = img_signup)
        panel.place(x=50, y=90)

        frame=Frame(win, width=350, height=390, bg='#fff')
        frame.place(x=480, y=50)

        heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('times new roman', 23,'bold'))
        heading.place(x=100, y=5)

        def on_enter(e):
            user.delete(0, 'end')
        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'Username')

        user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('times new roman',11))
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter(e):
            code.delete(0, 'end')
        def on_leave(e):
            if code.get() == '':
                code.insert(0, 'Password')

        code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('times new roman',11))
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind("<FocusIn>", on_enter)
        code.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        def on_enter(e):
            comfirm_code.delete(0, 'end')
        def on_leave(e):
            if comfirm_code.get() == '':
                comfirm_code.insert(0, 'Comfirm Password')

        comfirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('times new roman',11))
        comfirm_code.place(x=30, y=220)
        comfirm_code.insert(0, 'Comfirm Password')
        comfirm_code.bind("<FocusIn>", on_enter)
        comfirm_code.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

        Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
        label=Label(frame, text='I have an account', fg='black', bg='white', font=('times new roman',9))
        label.place(x= 90, y=340)

        signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign_in)
        signin.place(x=200, y=340)
        win.mainloop()

    img=PhotoImage(file='picture/login.png')
    Label(root, image=img, bg='white').place(x=50, y=50)

    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading=Label(frame, text='Sign in', fg="#57a1f8", font=('Pacifico', 23, 'bold'))
    heading.place(x=100, y=5)

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
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name =='':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Pacifico', 11))
    code.place(x=30, y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame,width=295, height=2, bg='black').place(x=25, y=177)

    ###################################
    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=login).place(x=35, y=204)
    label=Label(frame, text="Don't have an account !", fg='black', bg='white', font=('Pacifico', 11))
    label.place(x=75, y=270)

    Sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup_command)
    Sign_up.place(x=235, y=270)

    root.mainloop()

Signin()