from .Product import product
from .Interfaces import DiscountableInterface, TaxableInterface
class Electronics(product):
    CATEGORY = "Electronics"

    def __init__(self, name, ID, price, description, brand, warranty_period, power_consumption):
        super().__init__(name, ID, price, description, brand)
        self.warranty_period = warranty_period
        self.power_consumption = power_consumption

    def calculate_discount(self):
        percent = 5
        discount_amount = self.price * (percent / 100) #5 percent standard discount for category electronics
        self.price -= discount_amount
        return self.price        

    def get_discount_percentage(self):
        return 5   
        
    def calculate_tax(self):
        tax_amount = self.price * (8/100)
        return tax_amount
    
    @property
    def tax_rate(self): 
        return 8.0

    def calculate_final_price(self):
        tax_amount = self.calculate_tax()
        discounted_amount = self.calculate_discount()
        final_price = self.price -discounted_amount+ tax_amount
        return final_price

    def get_product_category(self):
        return self.CATEGORY
