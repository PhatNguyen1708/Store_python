import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
    def __init__(self,admin):
        self.admin = admin
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
            self.shopping_cart = tk.Toplevel(self.admin)
            self.shopping_cart.geometry('590x480')
            self.shopping_cart.resizable(width=tk.FALSE, height=tk.FALSE)
            self.frame_table_shopping_cart = tk.Frame(self.shopping_cart, width=500, height=170, bg = co2)
            self.frame_table_shopping_cart.grid(row= 0, column=0, padx=0, pady=0)
            self.frame_funtion = tk.Frame(self.shopping_cart, width=590, height=120, bg = co0)
            self.frame_funtion.place(x=0,y=350)
            
        def show_cart():
            listheader = ['ID','Name','Price', 'Quantity','Information']

            global list_item

            list_item = ttk.Treeview(self.frame_table_shopping_cart,height=15, selectmode="extended", columns=listheader, show="headings")
            list_vsb = ttk.Scrollbar(self.frame_table_shopping_cart, orient="vertical", command=list_item.yview)
            list_hsb = ttk.Scrollbar(self.frame_table_shopping_cart, orient="horizontal", command=list_item.xview)

            list_item.configure(yscrollcommand=list_vsb.set, xscrollcommand=list_hsb.set)

            list_item.grid(column=0, row=0, sticky='nsew')
            list_vsb.grid(column=1, row=0, sticky='ns')
            list_hsb.grid(column=0, row=1, sticky='ew')

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
            item = list_item.focus()
            item_text = tree.item(item)['values']
            for cart in self.carts:
                if len(self.carts)==1:
                    self.carts = []
                if cart["ID"] == item_text[0]:
                    self.carts.remove(cart)
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
        self.shopping_cart.e_count.configure(state="disabled")
        self.remove = tk.Button(self.frame_funtion,text="remove",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=remove)
        self.remove.place(x=30,y=50)
        self.pay = tk.Button(self.frame_funtion,text="Pay",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=Pay)
        self.pay.place(x=250,y=80)

    def configure_normal(self):
        self.admin.e_Id.configure(state="normal")
        self.admin.e_Name.configure(state="normal")
        self.admin.e_Price.configure(state="normal")
        self.admin.e_Infromation.configure(state="normal")
    
    def configure_disabled(self):
        self.admin.e_Id.configure(state="disabled")
        self.admin.e_Name.configure(state="disabled")
        self.admin.e_Price.configure(state="disabled")
        self.admin.e_Infromation.configure(state="disabled")

    def add_cart(self):
        product_manager = Products()
        self.configure_normal()
        id=self.admin.e_Id.get("1.0",'end-1c')
        name = self.admin.e_Name.get("1.0",'end-1c')
        price =self.admin.e_Price.get("1.0",'end-1c')
        quantity=self.admin.e_Quantity.get("1.0",'end-1c')
        information=self.admin.e_Infromation.get("1.0",'end-1c')
        self.configure_disabled()
        if id=="":
            messagebox.showinfo("Fail", "NULL")
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
            self.help_use = tk.Toplevel(admin)
            self.help_use.resizable(width=tk.FALSE, height=tk.FALSE)
            self.help_use.geometry('550x480')
            frame_down_help = tk.Frame(self.help_use, width=500, height=170, bg = co2)
            frame_down_help.grid(row= 0, column=0, padx=0, pady=0)
            help_text = "-sadghwqehwerhwerhw"
            l_help = tk.Label(frame_down_help,text=help_text,width=20, height=1, font=('Ivy 10'), bg=co0)
            l_help.place(x=50, y=50)

    def search(self):
            product_manager = Products()
            search_data = self.admin.e_search.get()
            data = product_manager.search_product(search_data)
            tree.delete(*tree.get_children())
            for item in data:
                tree.insert('', 'end',values=(item["ID"],item["Name"],item["Price"], item["Quantity"],item["Information"]))
            self.admin.e_search.delete(0, 'end')

    def clean(self):
        self.configure_normal()
        self.admin.e_Id.delete('1.0', 'end')
        self.admin.e_Name.delete('1.0', 'end')
        self.admin.e_Price.delete('1.0', 'end')
        self.admin.e_Quantity.delete('1.0', 'end')
        self.admin.e_Infromation.delete('1.0', 'end')
        self.configure_disabled()

    def show(self):
        def getrow(event):
            item = tree.focus()
            item_text = tree.item(item)['values']
            self.configure_normal()
            self.admin.e_Id.delete('1.0', 'end')
            self.admin.e_Name.delete('1.0', 'end')
            self.admin.e_Price.delete('1.0', 'end')
            self.admin.e_Quantity.delete('1.0', 'end')
            self.admin.e_Infromation.delete('1.0', 'end')

            self.admin.e_Id.insert('1.0',item_text[0])
            self.admin.e_Name.insert('1.0',item_text[1])
            self.admin.e_Price.insert('1.0',item_text[2])
            self.admin.e_Quantity.insert('1.0','1')
            self.admin.e_Infromation.insert('1.0',item_text[4])
            self.configure_disabled()
        global tree

        listheader = ['ID','Name','Price', 'Quantity','Information','Fluctuations']

        product_manager = Products()

        demo_list = product_manager.loadfile()

        tree =ttk.Treeview(self.admin.frame_table,height=20, selectmode="extended", columns=listheader, show="headings")

        scrolly = ttk.Scrollbar(self.admin.frame_table, orient="vertical", command=tree.yview)
        scrollx = ttk.Scrollbar(self.admin.frame_table, orient="horizontal", command=tree.xview)

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

        for item in demo_list:
            tree.insert('', 'end',values=(item["ID"],item["Name"],item["Price"], item["Quantity"],item["Information"],item["Fluctuations"]))
    
    def contruction(self):
        self.admin.title ("Store")
        self.admin.geometry('960x520')
        self.admin.configure(background=co0)
        self.admin.resizable(width=tk.FALSE, height=tk.FALSE)

        self.admin.frame_up = tk.Frame(self.admin, width=960, height=50, bg = co4)
        self.admin.frame_up.grid(row= 0, column=0, padx=0, pady=0)

        self.admin.frame_function = tk.Frame(self.admin, width=300, height=150, bg = co0,highlightbackground=co1, highlightthickness=2)
        self.admin.frame_function.place(x=650, y=60)

        self.admin.frame_product = tk.Frame(self.admin, width=300, height=287, bg = co0,highlightbackground=co1, highlightthickness=2)
        self.admin.frame_product.place(x=650, y=220)

        self.admin.frame_table = tk.Frame(self.admin, width=570, height=500, bg = co5,highlightbackground=co1, highlightthickness=2, relief="flat")
        self.admin.frame_table.place(x=10, y=60)

        app_name = tk.Label(self.admin.frame_up, text="Store", height=1, font=('Verdana 17 bold'), bg=co4 ,fg=co1)
        app_name.place(x=5, y=5)

        self.admin.l_Id =tk.Label(self.admin.frame_product, text="ID ", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.admin.l_Id.place(x=10, y=30)
        self.admin.e_Id =tk.Text(self.admin.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.admin.e_Id.place(x=80, y=30)
        self.admin.e_Id.configure(state="disabled")

        self.admin.l_Name = tk.Label(self.admin.frame_product, text="Name ",width=20, height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.admin.l_Name.place(x=10, y=60)
        self.admin.e_Name = tk.Text(self.admin.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.admin.e_Name.place(x=80, y=60)
        self.admin.e_Name.configure(state="disabled")

        self.admin.l_Price = tk.Label(self.admin.frame_product, text="Price ", height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.admin.l_Price.place(x=10, y=90)
        self.admin.e_Price = tk.Text(self.admin.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.admin.e_Price.place(x=80, y=90)
        self.admin.e_Price.configure(state="disabled")

        self.admin.l_Quantity = tk.Label(self.admin.frame_product, text="Quantity ", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.admin.l_Quantity.place(x=10, y=120)
        self.admin.e_Quantity = tk.Text(self.admin.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.admin.e_Quantity.place(x=80, y=120)

        self.admin.l_Infromation = tk.Label(self.admin.frame_product, text="Infromation ", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=tk.NW)
        self.admin.l_Infromation.place(x=10, y=150)
        self.admin.e_Infromation = tk.Text(self.admin.frame_product, width=25,height=3,highlightbackground=co1,highlightthickness=1)
        self.admin.e_Infromation.place(x=80, y=150)
        self.admin.e_Infromation.configure(state="disabled")

        self.admin.help_use = tk.Button(self.admin.frame_up, text="help", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.help)
        self.admin.help_use.place(x=850, y=10)

        self.admin.b_search = tk.Button(self.admin.frame_function, text="Search",width=5, height=1, bg=co4, font=('Ivy 8 bold'),command=self.search)
        self.admin.b_search.place(x=10, y=20)
        self.admin.e_search = tk.Entry(self.admin.frame_function, width=20, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
        self.admin.e_search.place(x=70, y=20)

        self.admin.b_view = tk.Button(self.admin.frame_function, text="View", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.show)
        self.admin.b_view.place(x=10, y=50)

        self.admin.b_clean = tk.Button(self.admin.frame_product, text="Clean all",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=self.clean)
        self.admin.b_clean.place(x=10, y=210)

        self.admin.b_add= tk.Button(self.admin.frame_product, text="Add to cart",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=self.add_cart)
        self.admin.b_add.place(x=80, y=210)

        self.admin.b_cart = tk.Button(self.admin.frame_product, text="Cart",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=self.show_shopping_cart)
        self.admin.b_cart.place(x=210, y=250)

if __name__ == "__main__":
    admin = tk.Tk()
    obj = user_store(admin)
    admin.mainloop()