class product:
    def __init__(self,name,ID,price,description,brand):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name=name
        self.ID=ID
        self.price=price
        self.description=description
        self.brand=brand
        self.product_info={
            "name":self.name, 
            "id":self.ID,
            "price":self.price,
            "brand":self.brand,
            "description":self.description
            }
    def __str__(self):
        return f"Product(Name: {self.name}, ID: {self.ID}, Price: {self.price}, Description: {self.description}, Brand: {self.brand})"
    


