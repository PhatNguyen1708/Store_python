import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, scrolledtext
from PIL import Image,ImageTk
from Function import *
import re
#colors
co0 = "#ffffff" #trang
co1 = "#000000"  #den
co2 = "#4456F0"  #xanh
co3 = "#ff69b4"   #hotpink
co4 = "#6495ED"   #hongnhat
co5 = "#dda0dd"


class user_store:
    def __init__(self,user,name_user):
        self.name_user =name_user
        self.user = user
        self.contruction()
        self.carts = []
        self.show()
        self.help_use = None
        self.shopping_cart = None

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def show_shopping_cart(self):
        if not self.shopping_cart or not self.shopping_cart.winfo_exists():
            self.shopping_cart = tk.Toplevel(self.user)
            self.shopping_cart.geometry('590x480+300+150')
            self.shopping_cart.resizable(width=tk.FALSE, height=tk.FALSE)
            self.frame_table_shopping_cart = tk.Frame(self.shopping_cart, width=500, height=170, bg = co2)
            self.frame_table_shopping_cart.grid(row= 0, column=0, padx=10, pady=20)
            self.frame_funtion = tk.Frame(self.shopping_cart, width=590, height=120, bg = co0)
            self.frame_funtion.place(x=0,y=350)
            
        def show_cart():
            global list_item
            listheader = ['ID','Name','Price', 'Quantity','Information']

            list_item = ttk.Treeview(self.frame_table_shopping_cart,height=15, selectmode="extended", columns=listheader, show="headings")
            list_vsb = ttk.Scrollbar(self.frame_table_shopping_cart, orient="vertical", command=list_item.yview)
            list_hsb = ttk.Scrollbar(self.frame_table_shopping_cart, orient="horizontal", command=list_item.xview)

            def get_ID(event):
                item_cart = list_item.focus()
                item_text = list_item.item(item_cart)['values']
                self.shopping_cart.e_remove.delete(0,tk.END)
                self.shopping_cart.e_remove.insert(0,item_text[0])
                self.shopping_cart.e_update.delete(0,tk.END)
                self.shopping_cart.e_update.insert(0,item_text[3])

            list_item.configure(yscrollcommand=list_vsb.set, xscrollcommand=list_hsb.set)

            list_item.grid(column=0, row=0, sticky='nsew')
            list_vsb.grid(column=1, row=0, sticky='ns')
            list_hsb.grid(column=0, row=1, sticky='ew')

            list_item.bind('<Double 1>', get_ID)

            list_item.heading(0, text='ID', anchor=tk.NW)
            list_item.heading(1, text='Name', anchor=tk.NW)
            list_item.heading(2, text='Price', anchor=tk.NW)
            list_item.heading(3, text='Quantity', anchor=tk.NW)
            list_item.heading(4, text='Information', anchor=tk.NW)
                
            list_item.column(0, width=50,anchor='nw')
            list_item.column(1, width=120, anchor='nw')
            list_item.column(2, width=100, anchor='nw')
            list_item.column(3, width=100, anchor='nw')
            list_item.column(4, width=180, anchor='nw')
            for cart in self.carts:
                    list_item.insert('', 'end',values=(cart["ID"],cart["Name"],cart["Price"], cart["Quantity"],cart["Information"]))
        show_cart()

        def check_price():
            Count = 0
            self.shopping_cart.e_count.configure(state="normal")
            for cart in self.carts:
                Count += float(cart["Price"])*float(cart["Quantity"])
            self.shopping_cart.e_count.delete(0,tk.END)
            self.shopping_cart.e_count.insert(0,Count)
            self.shopping_cart.e_count.configure(state="disabled")

        def remove():
            ID_remove = self.shopping_cart.e_remove.get()
            for cart in self.carts:
                if cart["ID"] == ID_remove:
                    self.carts.remove(cart)
            show_cart()
            check_price()
        
        def update_q():
            ID_update = self.shopping_cart.e_remove.get()
            Q_update = self.shopping_cart.e_update.get()
            if ID_update =="":
                messagebox.showinfo("Fail", "Please Enter ID")
            for cart in self.carts:
                if cart["ID"] == ID_update:
                    cart["Quantity"]=Q_update
            show_cart()
            check_price()

        def Pay():
            product = Products()
            for cart in self.carts:
                product.sell_product(Product(cart["ID"],cart["Name"],cart["Price"], cart["Quantity"],cart["Information"],0))
            self.carts = []
            self.show()
            show_cart()
            check_price()
        
        self.shopping_cart.l_count=tk.Label(self.frame_funtion, text=f"Price:", height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.shopping_cart.l_count.place(x=30,y=80)
        self.shopping_cart.e_count=tk.Entry(self.frame_funtion,width=20, font=('Ivy 10'), bg=co0)
        self.shopping_cart.e_count.place(x=100,y=80)
        check_price() 

        self.shopping_cart.remove = tk.Button(self.frame_funtion,text="Remove",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=remove)
        self.shopping_cart.remove.place(x=250,y=10)
        self.shopping_cart.l_remove =tk.Label(self.frame_funtion, text=f"ID:", height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.shopping_cart.l_remove.place(x=30,y=10)
        self.shopping_cart.e_remove = tk.Entry(self.frame_funtion, width=20, justify='left', font=('Ivy', 10), highlightthickness=1, relief="solid")
        self.shopping_cart.e_remove.place(x=100,y=10)

        self.shopping_cart.b_update = tk.Button(self.frame_funtion,text="Update",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=update_q)
        self.shopping_cart.b_update.place(x=250,y=40)
        self.shopping_cart.l_update =tk.Label(self.frame_funtion, text=f"Quantity:", height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.shopping_cart.l_update.place(x=30,y=40)
        self.shopping_cart.e_update = tk.Entry(self.frame_funtion, width=20, justify='left', font=('Ivy', 10), highlightthickness=1, relief="solid")
        self.shopping_cart.e_update.place(x=100,y=40)

        self.shopping_cart.pay = tk.Button(self.frame_funtion,text="Pay",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=Pay)
        self.shopping_cart.pay.place(x=250,y=80)

    def configure_normal(self):
        self.user.e_Id.configure(state="normal")
        self.user.e_Name.configure(state="normal")
        self.user.e_Price.configure(state="normal")
        self.user.e_Infromation.configure(state="normal")
    
    def configure_disabled(self):
        self.user.e_Id.configure(state="disabled")
        self.user.e_Name.configure(state="disabled")
        self.user.e_Price.configure(state="disabled")
        self.user.e_Infromation.configure(state="disabled")

    def add_cart(self):
        product_manager = Products()
        self.configure_normal()
        id=self.user.e_Id.get("1.0",'end-1c')
        name = self.user.e_Name.get("1.0",'end-1c')
        price =self.user.e_Price.get("1.0",'end-1c')
        quantity=self.user.e_Quantity.get("1.0",'end-1c')
        information=self.user.e_Infromation.get("1.0",'end-1c')
        self.configure_disabled()
        if id=="":
            messagebox.showinfo("Fail", "Data missing")
            return
        elif quantity == '0' or not self.is_number(quantity):
            messagebox.showinfo("Fail", "Quantity is a number")
            return
        else:
            add = Product(id,name,price,quantity,information,0)
        
        products = product_manager.loadfile()
        for product in products:
            if product['ID']==add.ID:
                if int(product['Quantity'])<int(add.Quantity):
                    messagebox.showinfo("Fail", "The quantity of goods is insufficient.")
                    return

        if self.carts == []:
            self.carts.append(vars(add))
        else:
            check =0
            for cart in self.carts:
                if cart['ID']==add.ID:
                    cart['Quantity'] = int(add.Quantity)
                    check =+1
            if check == 0:
                self.carts.append(vars(add))

    def help(self): 
        if not self.help_use or not self.help_use.winfo_exists():
            self.help_use = tk.Toplevel(user)
            self.help_use.resizable(width=tk.FALSE, height=tk.FALSE)
            self.help_use.geometry('550x480+300+150')
            frame_down_help = tk.Frame(self.help_use, width=500, height=170, bg = co2)
            frame_down_help.grid(row= 0, column=0, padx=0, pady=0)
            help_text = "-sadghwqehwerhwerhw"
            l_help = tk.Label(frame_down_help,text=help_text,width=20, height=1, font=('Ivy 10'), bg=co0)
            l_help.place(x=50, y=50)

    def search(self):
            product_manager = Products()
            search_data = self.user.e_search.get()
            data = product_manager.search_product(search_data)
            tree.delete(*tree.get_children())
            for item in data:
                tree.insert('', 'end',values=(item["ID"],item["Name"],item["Price"], item["Quantity"],item["Information"]))
            self.user.e_search.delete(0, 'end')

    def clean(self):
        self.configure_normal()
        self.user.e_Id.delete('1.0', 'end')
        self.user.e_Name.delete('1.0', 'end')
        self.user.e_Price.delete('1.0', 'end')
        self.user.e_Quantity.delete('1.0', 'end')
        self.user.e_Infromation.delete('1.0', 'end')
        self.configure_disabled()

    def show(self):
        def getrow(event):
            item = tree.focus()
            item_text = tree.item(item)['values']
            self.configure_normal()
            self.user.e_Id.delete('1.0', 'end')
            self.user.e_Name.delete('1.0', 'end')
            self.user.e_Price.delete('1.0', 'end')
            self.user.e_Quantity.delete('1.0', 'end')
            self.user.e_Infromation.delete('1.0', 'end')

            self.user.e_Id.insert('1.0',item_text[0])
            self.user.e_Name.insert('1.0',item_text[1])
            self.user.e_Price.insert('1.0',item_text[2])
            self.user.e_Quantity.insert('1.0','1')
            self.user.e_Infromation.insert('1.0',item_text[4])
            self.configure_disabled()
        global tree

        listheader = ['ID','Name','Price', 'Quantity','Information','Fluctuations']

        product_manager = Products()

        list_product = product_manager.loadfile()

        tree =ttk.Treeview(self.user.frame_table,height=20, selectmode="extended", columns=listheader, show="headings")

        scrolly = ttk.Scrollbar(self.user.frame_table, orient="vertical", command=tree.yview)
        scrollx = ttk.Scrollbar(self.user.frame_table, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        tree.bind('<Double 1>', getrow)

        tree.grid(column=0, row=0, sticky='nsew')
        scrolly.grid(column=1, row=0, sticky='ns')
        scrollx.grid(column=0, row=1, sticky='ew')

        tree.heading(0, text='ID', anchor=tk.NW)
        tree.heading(1, text='Name', anchor=tk.NW)
        tree.heading(2, text='Price', anchor=tk.NW)
        tree.heading(3, text='Quantity', anchor=tk.NW)
        tree.heading(4, text='Information', anchor=tk.NW)
        tree.heading(5, text='Fluctuations', anchor=tk.NW)
            
        tree.column(0, width=50,anchor='nw')
        tree.column(1, width=120, anchor='nw')
        tree.column(2, width=50, anchor='nw')
        tree.column(3, width=100, anchor='nw')
        tree.column(4, width=180, anchor='nw')
        tree.column(5,width=100, anchor='nw')

        for item in list_product:
            tree.insert('', 'end',values=(item["ID"],item["Name"],item["Price"], item["Quantity"],item["Information"],item["Fluctuations"]))
    
    def contruction(self):
        self.user.title ("Store")
        self.user.geometry('960x520+300+150')
        self.user.configure(background=co0)
        self.user.resizable(width=tk.FALSE, height=tk.FALSE)

        self.user.frame_up = tk.Frame(self.user, width=960, height=50, bg = co4)
        self.user.frame_up.grid(row= 0, column=0, padx=0, pady=0)

        self.user.frame_function = tk.Frame(self.user, width=300, height=150, bg = co0,highlightbackground=co1, highlightthickness=2)
        self.user.frame_function.place(x=650, y=60)

        self.user.frame_product = tk.Frame(self.user, width=300, height=287, bg = co0,highlightbackground=co1, highlightthickness=2)
        self.user.frame_product.place(x=650, y=220)

        self.user.frame_table = tk.Frame(self.user, width=570, height=500, bg = co5,highlightbackground=co1, highlightthickness=2, relief="flat")
        self.user.frame_table.place(x=10, y=60)

        app_name = tk.Label(self.user.frame_up, text="Store", height=1, font=('Verdana 17 bold'), bg=co4 ,fg=co1)
        app_name.place(x=5, y=5)

        self.user.l_Id =tk.Label(self.user.frame_product, text="ID ", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.user.l_Id.place(x=10, y=30)
        self.user.e_Id =tk.Text(self.user.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.user.e_Id.place(x=80, y=30)
        self.user.e_Id.configure(state="disabled")

        self.user.l_Name = tk.Label(self.user.frame_product, text="Name ",width=20, height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.user.l_Name.place(x=10, y=60)
        self.user.e_Name = tk.Text(self.user.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.user.e_Name.place(x=80, y=60)
        self.user.e_Name.configure(state="disabled")

        self.user.l_Price = tk.Label(self.user.frame_product, text="Price ", height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.user.l_Price.place(x=10, y=90)
        self.user.e_Price = tk.Text(self.user.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.user.e_Price.place(x=80, y=90)
        self.user.e_Price.configure(state="disabled")

        self.user.l_Quantity = tk.Label(self.user.frame_product, text="Quantity ", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.user.l_Quantity.place(x=10, y=120)
        self.user.e_Quantity = tk.Text(self.user.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.user.e_Quantity.place(x=80, y=120)

        self.user.l_Infromation = tk.Label(self.user.frame_product, text="Infromation ", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.user.l_Infromation.place(x=10, y=150)
        self.user.e_Infromation = scrolledtext.ScrolledText(self.user.frame_product, width=24, height=4, wrap=tk.WORD,highlightthickness=1, relief="solid")
        self.user.e_Infromation.place(x=80, y=150)
        self.user.e_Infromation.configure(state="disabled")

        self.user.help_use = tk.Button(self.user.frame_up, text="help", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.help)
        self.user.help_use.place(x=850, y=10)

        self.user.l_name_user = tk.Label(self.user.frame_function, text="Name: "+self.name_user, width=20, height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.user.l_name_user.place(x=10, y=10)

        self.user.b_search = tk.Button(self.user.frame_function, text="Search",width=5, height=1, bg=co4, font=('Ivy 8 bold'),command=self.search)
        self.user.b_search.place(x=10, y=40)
        self.user.e_search = tk.Entry(self.user.frame_function, width=20, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
        self.user.e_search.place(x=70, y=40)

        self.user.b_view = tk.Button(self.user.frame_function, text="View", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.show)
        self.user.b_view.place(x=10, y=70)

        self.user.b_clean = tk.Button(self.user.frame_product, text="Clean",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=self.clean)
        self.user.b_clean.place(x=10, y=225)

        self.user.b_add= tk.Button(self.user.frame_product, text="Add to cart",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=self.add_cart)
        self.user.b_add.place(x=80, y=225)

        self.user.b_cart = tk.Button(self.user.frame_product, text="Cart",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=self.show_shopping_cart)
        self.user.b_cart.place(x=210, y=250)

if __name__ == "__main__":
    user = tk.Tk()
    obj = user_store(user,"Phat")
    user.mainloop()