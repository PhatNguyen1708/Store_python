from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from Function import *

#colors
co0 = "#ffffff" #trang
co1 = "#000000"  #den
co2 = "#4456F0"  #xanh
co3 = "#ff69b4"   #hotpink
co4 = "#ffb6c1"   #hongnhat
co5 = "#dda0dd"


class admin_store:
    def __init__(self,admin):
        self.admin = admin
        self.admin.title ("Store")
        self.admin.geometry('550x480')
        self.admin.configure(background=co0)
        self.admin.resizable(width=FALSE, height=FALSE)

        self.admin.frame_up = Frame(self.admin, width=550, height=50, bg = co4)
        self.admin.frame_up.grid(row= 0, column=0, padx=0, pady=0)

        self.admin.frame_down = Frame(self.admin, width=500, height=170, bg = co0)
        self.admin.frame_down.grid(row= 1, column=0, padx=0, pady=0)

        self.admin.frame_table = Frame(self.admin, width=550, height=100, bg = co5, relief="flat")
        self.admin.frame_table.grid(row= 2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

        t1 = StringVar()
        t2 = StringVar()
        t3 = StringVar()
        t4 = StringVar()
        t5 = StringVar()

        def getrow(event):
            rowid = tree.identify_row(event.y)
            item = tree.item(tree.focus())
            t1.set(item['values'][0])
            t2.set(item['values'][1])
            t3.set(item['values'][2])
            t4.set(item['values'][3])
            t5.set(item['values'][4])
        def show():
            global tree

            listheader = ['ID','Name','Price', 'Quantity','Infromation']

            product_manager = Products()

            demo_list = product_manager.loadfile()

            tree =ttk.Treeview(admin.frame_table, selectmode="extended", columns=listheader, show="headings")

            vsb = ttk.Scrollbar(admin.frame_table, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(admin.frame_table, orient="horizontal", command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

            tree.bind('<Double 1>', getrow)

            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')

            tree.heading(0, text='ID', anchor=NW)
            tree.heading(1, text='Name', anchor=NW)
            tree.heading(2, text='Price', anchor=NW)
            tree.heading(3, text='Quantity', anchor=NW)
            tree.heading(4, text='Infromation', anchor=NW)
            
            tree.column(0, width=50,anchor='nw')
            tree.column(1, width=120, anchor='nw')
            tree.column(2, width=50, anchor='nw')
            tree.column(3, width=100, anchor='nw')
            tree.column(4, width=180, anchor='nw')

            for item in demo_list:
                tree.insert('', 'end',values=(item["ID"],item["Name"],item["Price"], item["Quantity"],item["Infromation"]))
        show()

        def help():
            help_use = Tk()
            help_use.geometry('550x480')
            frame_down_help = Frame(help_use, width=500, height=170, bg = co2)
            frame_down_help.grid(row= 0, column=0, padx=0, pady=0)
            help_text = "-sadghwqehwerhwerhw"
            l_help = Label(frame_down_help,text="hello",width=20, height=1, font=('Ivy 10'), bg=co0)
            l_help.place(x=50, y=50)
            help_use.mainloop()
        def search():
            product_manager = Products()
            search_data = admin.e_search.get()
            data = product_manager.search_product(search_data)
            tree.delete(*tree.get_children())
            for item in data:
                tree.insert('', 'end',values=(item["ID"],item["Name"],item["Price"], item["Quantity"],item["Infromation"]))
            admin.e_search.delete(0, 'end')
        
        def remove():
            item = admin.e_Id.get()
            product_manager = Products()
            search_data = admin.e_search.get()
            check = product_manager.remove_product(item)
            if check == 0:
                messagebox.showinfo('Success', 'Data has been deleted successfully !')
            else:
                messagebox.showinfo('Fail',"Not Found!")
            show()
            admin.e_Name.delete(0, 'end')
            admin.e_Price.delete(0, 'end')
            admin.e_Id.delete(0, 'end')
            admin.e_Quantity.delete(0, 'end')
            admin.e_Infromation.delete(0, 'end')



        admin.app_name = Label(admin.frame_up, text="Store", height=1, font=('Verdana 17 bold'), bg=co4 ,fg=co1)
        admin.app_name.place(x=5, y=5)

        admin.help_use = Button(admin.frame_up, text="help", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=help)
        admin.help_use.place(x=450, y=10)

        admin.l_Id =Label(admin.frame_down, text="ID *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        admin.l_Id.place(x=10, y=20)
        admin.e_Id = Entry(admin.frame_down, width=25, justify='left', highlightthickness=1, relief="solid",textvariable=t1)
        admin.e_Id.place(x=80, y=20)

        admin.l_Name = Label(admin.frame_down, text="Name *",width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        admin.l_Name.place(x=10, y=50)
        admin.e_Name = Entry(admin.frame_down, width=25, justify='left', highlightthickness=1, relief="solid",textvariable=t2)
        admin.e_Name.place(x=80, y=50)

        admin.l_Price = Label(admin.frame_down, text="Price *", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        admin.l_Price.place(x=10, y=80)
        admin.e_Price = Entry(admin.frame_down, width=25, justify='left', highlightthickness=1, relief="solid",textvariable=t3)
        admin.e_Price.place(x=80, y=80)

        admin.l_Quantity = Label(admin.frame_down, text="Quantity *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        admin.l_Quantity.place(x=10, y=110)
        admin.e_Quantity = Entry(admin.frame_down, width=25, justify='left', highlightthickness=1, relief="solid",textvariable=t4)
        admin.e_Quantity.place(x=80, y=110)

        admin.l_Infromation = Label(admin.frame_down, text="Infromation *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        admin.l_Infromation.place(x=10, y=140)
        admin.e_Infromation = Entry(admin.frame_down, width=25, justify='left', highlightthickness=1, relief="solid",textvariable=t5)
        admin.e_Infromation.place(x=80, y=140)


        admin.b_search = Button(admin.frame_down, text="Search", height=1, bg=co4, font=('Ivy 8 bold'),command=search)
        admin.b_search.place(x=290, y=20)
        admin.e_search = Entry(admin.frame_down, width=16, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
        admin.e_search.place(x=340, y=20)

        admin.b_view = Button(admin.frame_down, text="View", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=show)
        admin.b_view.place(x=290, y=50)

        admin.b_add = Button(admin.frame_down, text="Add", width=10, height=1, bg=co4, font=('Ivy 8 bold'))
        admin.b_add.place(x=400, y=50)

        admin.b_update = Button(admin.frame_down, text="Update", width=10, height=1, bg=co4, font=('Ivy 8 bold'))
        admin.b_update.place(x=400, y=80)

        admin.b_delete = Button(admin.frame_down, text="Delete", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=remove)
        admin.b_delete.place(x=400, y=110)
if __name__ == "__main__":
    admin = Tk()
    obj = admin_store(admin)
    admin.mainloop()