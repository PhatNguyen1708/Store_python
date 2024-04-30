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
        self.show()

    def help_use(self):
            help_use = Tk()
            help_use.geometry('590x480')
            frame_down_help = Frame(help_use, width=500, height=170, bg = co2)
            frame_down_help.grid(row= 0, column=0, padx=0, pady=0)
            help_text = "-sadghwqehwerhwerhw"
            l_help = Label(frame_down_help,text=help_text,width=20, height=1, font=('Ivy 10'), bg=co0)
            l_help.place(x=50, y=50)
            help_use.mainloop()

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

        self.admin.frame_table = Frame(self.admin, width=570, height=500, bg = co2,highlightbackground=co1, highlightthickness=2, relief="flat")
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

        self.admin.help_use = Button(self.admin.frame_up, text="help", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.help_use)
        self.admin.help_use.place(x=800, y=10)

        self.admin.b_search = Button(self.admin.frame_function, text="Search",width=5, height=1, bg=co4, font=('Ivy 8 bold'),command=self.search)
        self.admin.b_search.place(x=10, y=20)
        self.admin.e_search = Entry(self.admin.frame_function, width=20, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
        self.admin.e_search.place(x=70, y=20)

        self.admin.b_view = Button(self.admin.frame_function, text="View", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.show)
        self.admin.b_view.place(x=10, y=50)

        self.admin.b_clean = Button(self.admin.frame_product, text="Clean all",width=8, height=1, bg=co4, font=('Ivy 8 bold'),command=self.clean)
        self.admin.b_clean.place(x=10, y=210)

if __name__ == "__main__":
    admin = Tk()
    obj = user_store(admin)
    admin.mainloop()