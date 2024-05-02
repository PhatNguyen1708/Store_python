from tkinter import *
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
co4 = "#ffb6c1"   #hongnhat
co5 = "#dda0dd"


class user_store:
    def __init__(self,admin):
        self.admin = admin
        self.contruction()
        self.carts = []
        self.API()
        self.show()
        self.help_use = None
        self.shopping_cart = None

    def API(self):
        response = requests.get('https://v1.slashapi.com/hehehehe/mysql/njU5fzbTtN/store')
        if response.status_code == 200:
             data =response.json()['data']
             with open('store_data.json','w',encoding='utf-8') as file:
                json.dump(data,file, ensure_ascii=False, indent=4)
        else:
            messagebox.showinfo("Fail","Can't get data from API, use last data")

    def show_shopping_cart(self):
        if not self.shopping_cart or not self.shopping_cart.winfo_exists():
            self.shopping_cart = Toplevel(self.admin)
            self.shopping_cart.geometry('590x480')
            self.shopping_cart.resizable(width=FALSE, height=FALSE)
            self.frame_down_shopping_cart = Frame(self.shopping_cart, width=500, height=170, bg = co2)
            self.frame_down_shopping_cart.grid(row= 0, column=0, padx=0, pady=0)

        def show_cart():

            listheader = ['ID','Name','Price', 'Quantity','Information']

            list_item = ttk.Treeview(self.frame_down_shopping_cart,height=20, selectmode="extended", columns=listheader, show="headings")
            list_vsb = ttk.Scrollbar(self.frame_down_shopping_cart, orient="vertical", command=tree.yview)
            list_hsb = ttk.Scrollbar(self.frame_down_shopping_cart, orient="horizontal", command=tree.xview)

            tree.configure(yscrollcommand=list_vsb.set, xscrollcommand=list_hsb.set)

            list_item.grid(column=0, row=0, sticky='nsew')
            list_vsb.grid(column=1, row=0, sticky='ns')
            list_hsb.grid(column=0, row=1, sticky='ew')

            list_item.heading(0, text='ID', anchor=NW)
            list_item.heading(1, text='Name', anchor=NW)
            list_item.heading(2, text='Price', anchor=NW)
            list_item.heading(3, text='Quantity', anchor=NW)
            list_item.heading(4, text='Information', anchor=NW)
                
            list_item.column(0, width=50,anchor='nw')
            list_item.column(1, width=120, anchor='nw')
            list_item.column(2, width=100, anchor='nw')
            list_item.column(3, width=100, anchor='nw')
            list_item.column(4, width=180, anchor='nw')

            for cart in self.carts:
                list_item.insert('', 'end',values=(cart["ID"],cart["Name"],cart["Price"], cart["Quantity"],cart["Information"]))
        show_cart()

    def add_cart(self):
        self.admin.e_Id.configure(state="normal")
        self.admin.e_Name.configure(state="normal")
        self.admin.e_Price.configure(state="normal")
        self.admin.e_Infromation.configure(state="normal")
        id=self.admin.e_Id.get("1.0",'end-1c')
        name = self.admin.e_Name.get("1.0",'end-1c')
        price =self.admin.e_Price.get("1.0",'end-1c')
        quantity=self.admin.e_Quantity.get("1.0",'end-1c')
        information=self.admin.e_Infromation.get("1.0",'end-1c')
        self.admin.e_Id.configure(state="disabled")
        self.admin.e_Name.configure(state="disabled")
        self.admin.e_Price.configure(state="disabled")
        self.admin.e_Infromation.configure(state="disabled")
        add = Product(id,name,price,quantity,information)
        self.carts.append(vars(add))
    def help(self): 
        if not self.help_use or not self.help_use.winfo_exists():
            self.help_use = Toplevel(admin)
            self.help_use.resizable(width=FALSE, height=FALSE)
            self.help_use.geometry('550x480')
            frame_down_help = Frame(self.help_use, width=500, height=170, bg = co2)
            frame_down_help.grid(row= 0, column=0, padx=0, pady=0)
            help_text = "-sadghwqehwerhwerhw"
            l_help = Label(frame_down_help,text=help_text,width=20, height=1, font=('Ivy 10'), bg=co0)
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
        self.admin.e_Id.configure(state="normal")
        self.admin.e_Name.configure(state="normal")
        self.admin.e_Price.configure(state="normal")
        self.admin.e_Infromation.configure(state="normal")

        self.admin.e_Id.delete('1.0', 'end')
        self.admin.e_Name.delete('1.0', 'end')
        self.admin.e_Price.delete('1.0', 'end')
        self.admin.e_Quantity.delete('1.0', 'end')
        self.admin.e_Infromation.delete('1.0', 'end')

        self.admin.e_Id.configure(state="disabled")
        self.admin.e_Name.configure(state="disabled")
        self.admin.e_Price.configure(state="disabled")
        self.admin.e_Infromation.configure(state="disabled")

    def show(self):
        def getrow(event):
            item = tree.focus()
            item_text = tree.item(item)['values']
            
            self.admin.e_Id.configure(state="normal")
            self.admin.e_Name.configure(state="normal")
            self.admin.e_Price.configure(state="normal")
            self.admin.e_Infromation.configure(state="normal")

            self.admin.e_Id.delete('1.0', 'end')
            self.admin.e_Name.delete('1.0', 'end')
            self.admin.e_Price.delete('1.0', 'end')
            self.admin.e_Quantity.delete('1.0', 'end')
            self.admin.e_Infromation.delete('1.0', 'end')

            self.admin.e_Id.insert('1.0',item_text[0])
            self.admin.e_Name.insert('1.0',item_text[1])
            self.admin.e_Price.insert('1.0',item_text[2])
            self.admin.e_Infromation.insert('1.0',item_text[4])

            self.admin.e_Id.configure(state="disabled")
            self.admin.e_Name.configure(state="disabled")
            self.admin.e_Price.configure(state="disabled")
            self.admin.e_Infromation.configure(state="disabled")

        global tree

        listheader = ['ID','Name','Price', 'Quantity','Information']

        product_manager = Products()

        demo_list = product_manager.loadfile()

        tree =ttk.Treeview(self.admin.frame_table,height=20, selectmode="extended", columns=listheader, show="headings")

        vsb = ttk.Scrollbar(self.admin.frame_table, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(self.admin.frame_table, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.bind('<Double 1>', getrow)

        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        tree.heading(0, text='ID', anchor=NW)
        tree.heading(1, text='Name', anchor=NW)
        tree.heading(2, text='Price', anchor=NW)
        tree.heading(3, text='Quantity', anchor=NW)
        tree.heading(4, text='Information', anchor=NW)
            
        tree.column(0, width=50,anchor='nw')
        tree.column(1, width=120, anchor='nw')
        tree.column(2, width=100, anchor='nw')
        tree.column(3, width=100, anchor='nw')
        tree.column(4, width=180, anchor='nw')

        for item in demo_list:
            tree.insert('', 'end',values=(item["ID"],item["Name"],item["Price"], item["Quantity"],item["Information"]))
    
    def contruction(self):
        self.admin.title ("Store")
        self.admin.geometry('900x520')
        self.admin.configure(background=co0)
        self.admin.resizable(width=FALSE, height=FALSE)

        self.admin.frame_up = Frame(self.admin, width=900, height=50, bg = co4)
        self.admin.frame_up.grid(row= 0, column=0, padx=0, pady=0)

        self.admin.frame_function = Frame(self.admin, width=300, height=150, bg = co0,highlightbackground=co1, highlightthickness=2)
        self.admin.frame_function.place(x=590, y=60)

        self.admin.frame_product = Frame(self.admin, width=300, height=287, bg = co0,highlightbackground=co1, highlightthickness=2)
        self.admin.frame_product.place(x=590, y=220)

        self.admin.frame_table = Frame(self.admin, width=570, height=500, bg = co5,highlightbackground=co1, highlightthickness=2, relief="flat")
        self.admin.frame_table.place(x=10, y=60)

        app_name = Label(self.admin.frame_up, text="Store", height=1, font=('Verdana 17 bold'), bg=co4 ,fg=co1)
        app_name.place(x=5, y=5)

        self.admin.l_Id =Label(self.admin.frame_product, text="ID ", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        self.admin.l_Id.place(x=10, y=30)
        self.admin.e_Id = Text(self.admin.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.admin.e_Id.place(x=80, y=30)
        self.admin.e_Id.configure(state="disabled")

        self.admin.l_Name = Label(self.admin.frame_product, text="Name ",width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        self.admin.l_Name.place(x=10, y=60)
        self.admin.e_Name = Text(self.admin.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.admin.e_Name.place(x=80, y=60)
        self.admin.e_Name.configure(state="disabled")

        self.admin.l_Price = Label(self.admin.frame_product, text="Price ", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        self.admin.l_Price.place(x=10, y=90)
        self.admin.e_Price = Text(self.admin.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.admin.e_Price.place(x=80, y=90)
        self.admin.e_Price.configure(state="disabled")

        self.admin.l_Quantity = Label(self.admin.frame_product, text="Quantity ", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        self.admin.l_Quantity.place(x=10, y=120)
        self.admin.e_Quantity = Text(self.admin.frame_product, width=25,height=1,highlightbackground=co1,highlightthickness=1)
        self.admin.e_Quantity.place(x=80, y=120)

        self.admin.l_Infromation = Label(self.admin.frame_product, text="Infromation ", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        self.admin.l_Infromation.place(x=10, y=150)
        self.admin.e_Infromation = Text(self.admin.frame_product, width=25,height=3,highlightbackground=co1,highlightthickness=1)
        self.admin.e_Infromation.place(x=80, y=150)
        self.admin.e_Infromation.configure(state="disabled")

        self.admin.help_use = Button(self.admin.frame_up, text="help", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.help)
        self.admin.help_use.place(x=800, y=10)

        self.admin.b_search = Button(self.admin.frame_function, text="Search",width=5, height=1, bg=co4, font=('Ivy 8 bold'),command=self.search)
        self.admin.b_search.place(x=10, y=20)
        self.admin.e_search = Entry(self.admin.frame_function, width=20, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
        self.admin.e_search.place(x=70, y=20)

        self.admin.b_view = Button(self.admin.frame_function, text="View", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.show)
        self.admin.b_view.place(x=10, y=50)

        self.admin.b_clean = Button(self.admin.frame_product, text="Clean all",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=self.clean)
        self.admin.b_clean.place(x=10, y=210)

        self.admin.b_add= Button(self.admin.frame_product, text="Add to cart",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=self.add_cart)
        self.admin.b_add.place(x=80, y=210)

        self.admin.b_cart = Button(self.admin.frame_product, text="Cart",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=self.show_shopping_cart)
        self.admin.b_cart.place(x=210, y=250)

if __name__ == "__main__":
    admin = Tk()
    obj = user_store(admin)
    admin.mainloop()