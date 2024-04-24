import json

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Products:
    def __init__(self):
        self.products = []
        self.loadfile()
    def loadfile(self):
        try:
            with open('store_data.json','r',encoding='utf-8') as file:
                self.products = json.load(file)
        except FileNotFoundError:
            self.products =[]
        return self.products

    def savefile(self):
        with open('store_data.json','w',encoding='utf-8') as file:
            json.dump(self.products, file, indent=4)
    
    def search_product(self, name):
        data = []
        with open('store_data.json','r',encoding='utf-8') as file:
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
                print("Product removed successfully!")
                return 0
        print("Product not found.")
        return 1
    
    def add_product(self,product):
        self.products.append(vars(product))

        
    

    