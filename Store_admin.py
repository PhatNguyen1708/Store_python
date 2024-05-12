from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from Function import *
import re
import requests
#colors
co0 = "#ffffff" #trang
co1 = "#000000"  #den
co2 = "#4456F0"  #xanh
co3 = "#ff69b4"   #hotpink
co4 = "#6495ED"   #hongnhat
co5 = "#dda0dd"


class admin_store:
    def __init__(self,admin):
        self.admin = admin
        self.contruction()
        self.show()
        self.help_use = None
        self.get_api = None

    def API(self):
        if not self.get_api or not self.get_api.destroy():
            self.get_api = Toplevel(self.admin)
            self.get_api.resizable(width=FALSE, height=FALSE)
            self.get_api.geometry('550x100+400+300')

            def check_fluctuations(json_file_path):
                    with open(json_file_path, 'r') as file:
                        data = json.load(file)
                    if "Fluctuations" in data:
                        return True
                    else:
                        return False
            def Get():
                link = e_api.get()
                if link=='':
                    messagebox.showinfo("Fail","Can't get data from API, use last data")
                else:
                    response = requests.get(link)
                    if response.status_code == 200:
                        data =response.json()['data']
                        with open('data/store_data.json','w',encoding='utf-8') as file:
                            json.dump(data,file, ensure_ascii=False, indent=4)
                        with open('data/store_data.json', 'r',encoding='utf-8') as file:
                                data = json.load(file)
                        if not check_fluctuations("data/store_data.json"):
                            for item in data:
                                item["Fluctuations"] = "0%"
                            with open('data/store_data.json', 'w',encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        messagebox.showinfo("Successful","Data retrieved from API.")
                        self.show()
                        self.get_api.destroy()
                    else:
                        messagebox.showinfo("Fail","Can't get data from API, use last data")

            l_api = Label(self.get_api,text="Link API:",width=20, height=1, font=('Ivy 10'))
            l_api.place(x=30, y=30)
            e_api = Entry(self.get_api, width=25, justify='left', highlightthickness=1, relief="solid")
            e_api.place(x=150, y=30)
            b_api = Button(self.get_api,text="Get",width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=Get)
            b_api.place(x=320, y=30)

    def help(self): 
        if not self.help_use or not self.help_use.destroy():
            self.help_use = Toplevel(admin)
            self.help_use.resizable(width=FALSE, height=FALSE)
            self.help_use.geometry('550x480+300+150')
            frame_down_help = Frame(self.help_use, width=500, height=170, bg = co2)
            frame_down_help.grid(row= 0, column=0, padx=0, pady=0)
            help_text = "-sadghwqehwerhwerhw"
            l_help = Label(frame_down_help,text=help_text,width=20, height=1, font=('Ivy 10'), bg=co0)
            l_help.place(x=50, y=50)

    def clean(self):
        self.admin.e_Name.delete(0, 'end')
        self.admin.e_Price.delete(0, 'end')
        self.admin.e_Id.delete(0, 'end')
        self.admin.e_Quantity.delete(0, 'end')
        self.admin.e_Infromation.delete(0, 'end')

    def search(self):
            product_manager = Products()
            search_data = self.admin.e_search.get()
            data = product_manager.search_product(search_data)
            tree.delete(*tree.get_children())
            for item in data:
                tree.insert('', 'end',values=(item["ID"],item["Name"],item["Price"], item["Quantity"],item["Information"]))
            self.admin.e_search.delete(0, 'end')
        
    def remove(self):
            item = self.admin.e_Id.get()
            product_manager = Products()
            self.search_data = self.admin.e_search.get()
            check = product_manager.remove_product(item)
            if check == 0:
                messagebox.showinfo('Successful', 'Data has been deleted successfully !')
            else:
                messagebox.showinfo('Fail',"Not Found!")
            self.show()
            self.admin.e_Name.delete(0, 'end')
            self.admin.e_Price.delete(0, 'end')
            self.admin.e_Id.delete(0, 'end')
            self.admin.e_Quantity.delete(0, 'end')
            self.admin.e_Infromation.delete(0, 'end')
 
    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def check_data(self,Id):
        product_manager = Products()
        check = 0
        products = product_manager.loadfile()
        for product in products:
            if product['ID'].lower() == Id.lower():
                 check = check
            else:
                 check += 1
        if check == len(products):
             check = 0
        else:
             check =1
        return check

    def add(self):
        product_manager = Products()
        id=self.admin.e_Id.get()
        name = self.admin.e_Name.get()
        price =self.admin.e_Price.get()
        quantity=self.admin.e_Quantity.get()
        information=self.admin.e_Infromation.get()
        fluctuations = 0
        check_id = self.check_data(id)
        check_price = self.is_number(price)
        check_quantity = self.is_number(quantity)

        if id == '' or name == '' or price == '' or quantity == '' or information == '':
            messagebox.showinfo("Fail", "Data missing" )
            return
        elif not re.search(r'^#+[0-9]',id):
            id = "#"+id
            add = Product(id,name,price,quantity,information)
            product_manager.add_product(add)
            self.show()
            self.admin.e_Name.delete(0, 'end')
            self.admin.e_Price.delete(0, 'end')
            self.admin.e_Id.delete(0, 'end')
            self.admin.e_Quantity.delete(0, 'end')
            self.admin.e_Infromation.delete(0, 'end')
            return
        elif not check_quantity or not check_price:
            messagebox.showinfo("Fail", "Price and Quantity is a number")
            return
        elif check_id == 1:
            messagebox.showinfo("Fail","Duplicate ID already exists")
            return
        else:
            add = Product(id,name,price,quantity,information,fluctuations)
            product_manager.add_product(add)
            self.show()
            messagebox.showinfo("Successful","Data add successfully !")
            self.admin.e_Name.delete(0, 'end')
            self.admin.e_Price.delete(0, 'end')
            self.admin.e_Id.delete(0, 'end')
            self.admin.e_Quantity.delete(0, 'end')
            self.admin.e_Infromation.delete(0, 'end')
    
    def update(self):
        product_manager = Products()
        id=self.admin.e_Id.get()
        name = self.admin.e_Name.get()
        price =self.admin.e_Price.get()
        quantity=self.admin.e_Quantity.get()
        information=self.admin.e_Infromation.get()
        fluctuations = 0
        check_id = self.check_data(id)
        check_price = self.is_number(price)
        check_quantity = self.is_number(quantity)
        if id == '' or name == '' or price == '' or quantity == '' or information == '':
            messagebox.showinfo("Fail", "Data missing" )
            return
        elif not re.search(r'^#+[0-9]',id):
            id = "#"+id
            add = Product(id,name,price,quantity,information,fluctuations)
            check_id = self.check_data(id)
            if check_id == 0:
                product_manager.add_product(add)
            else:
                product_manager.update_product(add)
            self.show()
            self.admin.e_Name.delete(0, 'end')
            self.admin.e_Price.delete(0, 'end')
            self.admin.e_Id.delete(0, 'end')
            self.admin.e_Quantity.delete(0, 'end')
            self.admin.e_Infromation.delete(0, 'end')
            return
        elif not check_quantity or not check_price:
            messagebox.showinfo("Fail", "Price and Quantity is a number")
            return
        elif check_id == 0:
            messagebox.showinfo("Fail","Not Found")
            return
        else:
            add = Product(id,name,price,quantity,information,fluctuations)
            product_manager.update_product(add)
            self.show()
            messagebox.showinfo("Successful","Data update successfully !")
            self.admin.e_Name.delete(0, 'end')
            self.admin.e_Price.delete(0, 'end')
            self.admin.e_Id.delete(0, 'end')
            self.admin.e_Quantity.delete(0, 'end')
            self.admin.e_Infromation.delete(0, 'end')

    def show(self):
        def getrow(event):
            item = tree.focus()
            item_text = tree.item(item)['values']
            
            self.admin.e_Name.delete(0, 'end')
            self.admin.e_Price.delete(0, 'end')
            self.admin.e_Id.delete(0, 'end')
            self.admin.e_Quantity.delete(0, 'end')
            self.admin.e_Infromation.delete(0, 'end')

            self.admin.e_Id.insert(0,item_text[0])
            self.admin.e_Name.insert(0,item_text[1])
            self.admin.e_Price.insert(0,item_text[2])
            self.admin.e_Quantity.insert(0,item_text[3])
            self.admin.e_Infromation.insert(0,item_text[4])

        global tree

        listheader = ['ID','Name','Price', 'Quantity','Information','Fluctuations']

        product_manager = Products()

        demo_list = product_manager.loadfile()

        tree =ttk.Treeview(self.admin.frame_table, selectmode="extended", columns=listheader, show="headings")

        scrolly = ttk.Scrollbar(self.admin.frame_table, orient="vertical", command=tree.yview)
        scrollx = ttk.Scrollbar(self.admin.frame_table, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        tree.bind('<Double 1>', getrow)

        tree.grid(column=0, row=0, sticky='nsew')
        scrolly.grid(column=1, row=0, sticky='ns')
        scrollx.grid(column=0, row=1, sticky='ew')

        tree.heading(0, text='ID', anchor=NW)
        tree.heading(1, text='Name', anchor=NW)
        tree.heading(2, text='Price', anchor=NW)
        tree.heading(3, text='Quantity', anchor=NW)
        tree.heading(4, text='Information', anchor=NW)
        tree.heading(5, text='Fluctuations', anchor=NW)
            
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
        self.admin.geometry('650x480+300+150')
        self.admin.configure(background=co0)
        self.admin.resizable(width=FALSE, height=FALSE)

        self.admin.frame_up = Frame(self.admin, width=650, height=50, bg = co4)
        self.admin.frame_up.grid(row= 0, column=0, padx=0, pady=0)

        self.admin.frame_down = Frame(self.admin, width=650, height=170, bg = co0)
        self.admin.frame_down.grid(row= 1, column=0, padx=0, pady=0)

        self.admin.frame_table = Frame(self.admin, width=650, height=100, bg = co0, relief="flat")
        self.admin.frame_table.grid(row= 2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

        app_name = Label(self.admin.frame_up, text="Store Manager", height=1, font=('Verdana 17 bold'), bg=co4 ,fg=co1)
        app_name.place(x=5, y=5)
        
        self.admin.help_use = Button(self.admin.frame_up, text="help", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.help)
        self.admin.help_use.place(x=550, y=10)

        self.admin.l_Id =Label(self.admin.frame_down, text="ID *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        self.admin.l_Id.place(x=10, y=20)
        self.admin.e_Id = Entry(self.admin.frame_down, width=30, justify='left', highlightthickness=1, relief="solid")
        self.admin.e_Id.place(x=80, y=20)

        self.admin.l_Name = Label(self.admin.frame_down, text="Name *",width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        self.admin.l_Name.place(x=10, y=50)
        self.admin.e_Name = Entry(self.admin.frame_down, width=30, justify='left', highlightthickness=1, relief="solid")
        self.admin.e_Name.place(x=80, y=50)

        self.admin.l_Price = Label(self.admin.frame_down, text="Price *", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        self.admin.l_Price.place(x=10, y=80)
        self.admin.e_Price = Entry(self.admin.frame_down, width=30, justify='left', highlightthickness=1, relief="solid")
        self.admin.e_Price.place(x=80, y=80)

        self.admin.l_Quantity = Label(self.admin.frame_down, text="Quantity *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        self.admin.l_Quantity.place(x=10, y=110)
        self.admin.e_Quantity = Entry(self.admin.frame_down, width=30, justify='left', highlightthickness=1, relief="solid")
        self.admin.e_Quantity.place(x=80, y=110)

        self.admin.l_Infromation = Label(self.admin.frame_down, text="Infromation *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
        self.admin.l_Infromation.place(x=10, y=140)
        self.admin.e_Infromation = Entry(self.admin.frame_down, width=30, justify='left', highlightthickness=1, relief="solid")
        self.admin.e_Infromation.place(x=80, y=140)

        self.admin.b_search = Button(self.admin.frame_down, text="Search", height=1, bg=co4, font=('Ivy 8 bold'),command=self.search)
        self.admin.b_search.place(x=400, y=20)
        self.admin.e_search = Entry(self.admin.frame_down, width=20, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
        self.admin.e_search.place(x=450, y=20)

        self.admin.b_view = Button(self.admin.frame_down, text="View", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.show)
        self.admin.b_view.place(x=400, y=50)

        self.admin.b_clean = Button(self.admin.frame_down, text="Clean", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.clean)
        self.admin.b_clean.place(x=400, y=80)

        self.admin.b_api = Button(self.admin.frame_down, text="API", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.API)
        self.admin.b_api.place(x=400, y=110)

        self.admin.b_add = Button(self.admin.frame_down, text="Add", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.add)
        self.admin.b_add.place(x=535, y=50)

        self.admin.b_update = Button(self.admin.frame_down, text="Update", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.update)
        self.admin.b_update.place(x=535, y=80)

        self.admin.b_delete = Button(self.admin.frame_down, text="Delete", width=10, height=1, bg=co4, font=('Ivy 8 bold'),command=self.remove)
        self.admin.b_delete.place(x=535, y=110)

if __name__ == "__main__":
    admin = Tk()
    obj = admin_store(admin)
    admin.mainloop()