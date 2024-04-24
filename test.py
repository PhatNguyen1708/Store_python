import json

class Product:
    def __init__(self, Name, Price, Quantity,ID,Infromation):
        self.ID = ID
        self.Name = Name
        self.Price = Price
        self.Quantity = Quantity
        self.Infromation = Infromation

    def display(self):
        print(f"ID: {self.ID} Product: {self.Name}, Price: ${self.Price}, Quantity: {self.Quantity}, Infromation: {self.Infromation}")


class ProductManager:
    def __init__(self):
        self.products = []
        self.load_products()

    def load_products(self):
        try:
            with open('store_data.json', 'r',encoding='utf-8') as file:
                self.products = json.load(file)
        except FileNotFoundError:
            print("Store file not found. Initializing empty store.")
            self.products = []

    def save_products(self):
        with open('store_data.json', 'w',encoding='utf-8') as file:
            json.dump(self.products, file, indent=4)

    def add_product(self, product):
        self.products.append(vars(product))
        self.save_products()
        print("Product added successfully!")

    def display_products(self):
        if self.products:
            print("List of Products:")
            for product in self.products:
                Product(**product).display()
        else:
            print("No products available.")

    def search_product(self, name):
        for product in self.products:
            if product['Name'].lower() == name.lower():
                Product(**product).display()
                return
        print("Product not found.")

    def update_product_quantity(self, name, quantity):
        for product in self.products:
            if product['Name'].lower() == name.lower():
                product['Quantity'] = quantity
                self.save_products()
                print("Product quantity updated successfully!")
                return
        print("Product not found.")

    def remove_product(self, name):
        for product in self.products:
            if product['Name'].lower() == name.lower():
                self.products.remove(product)
                self.save_products()
                print("Product removed successfully!")
                return
        print("Product not found.")


# Example usage:
if __name__ == "__main__":
    manager = ProductManager()

    # Displaying products
    manager.display_products()

    manager.remove_product("Product 2")

    manager.display_products()



#root.bind("<Delete>", space_pressed)