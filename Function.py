import json
import requests

class Product:
    def __init__(self,ID,Name,Price,Quantity,Information,Fluctuations):
        self.ID = ID
        self.Name = Name
        self.Price = Price
        self.Quantity = Quantity
        self.Information = Information
        self.Fluctuations = Fluctuations

class Products:
    def __init__(self):
        self.products = []
        self.loadfile()

    def loadfile(self):
        try:
            with open('data/store_data.json','r',encoding='utf-8') as file:
                self.products = json.load(file)
        except Exception:
            self.products =[]
        return self.products

    def savefile(self):
        with open('data/store_data.json','w',encoding='utf-8') as file:
            json.dump(self.products, file, indent=4,ensure_ascii=False)
    
    def search_product(self, name):
        data = []
        with open('data/store_data.json','r',encoding='utf-8') as file:
                self.products = json.load(file)
        for product in self.products:
            if product['Name'].lower() == name.lower() or product['ID'].lower() == name.lower():
                data.append(product)
        return data
    
    def remove_product(self,ID):
        for product in self.products:
            if product['ID'].lower() == ID.lower():
                self.products.remove(product)
                self.savefile()
                return 0
        return 1
    
    def add_product(self,product):
        self.products.append(vars(product))
        self.savefile()
    
    def update_product(self,new_product):
        for product in self.products:
            if product['ID'].lower() == new_product.ID.lower():
                fluctuations = ((float(new_product.Price)-float(product['Price']))/float(product['Price']))*100
                product['Name'] = new_product.Name 
                product['Price'] = new_product.Price
                product['Quantity']= new_product.Quantity
                product['Information']= new_product.Information
                product['Fluctuations'] = "{:.2f}%".format(fluctuations) 
                self.savefile()
    
    def sell_product(self,product_sell):
        for product in self.products:
            if product['ID'].lower() == product_sell.ID.lower():
                product['Quantity'] = int(product['Quantity']) - int(product_sell.Quantity)
        self.savefile()

    

    