from .Product import Product
from .Interfaces import DiscountableInterface, TaxableInterface
class Clothing(Product,DiscountableInterface,TaxableInterface):
    CATEGORY = "Clothing"
    def __init__(self, name, ID, price, description, brand, size, material, gender,season):
        super().__init__(name, ID, price, description, brand)
        self.size = size
        self.material = material
        self.gender=gender
        self.season=season

    def calculate_discount(self):
        percent = 10 if self.season.lower() == 'winter' else 15
        discount_amount = self.price * (percent / 100) #5 percent standard discount for category electronics
        self.price -= discount_amount
        return self.price        

    def get_discount_percentage(self):
        return 10 if self.season.lower() == 'winter' else 15   
        
    def calculate_tax(self):
        tax_amount = self.price * (12/100)
        return tax_amount
    
    @property
    def tax_rate(self): 
        return 12.0

    def calculate_final_price(self):
        tax_amount = self.calculate_tax()
        discounted_amount = self.calculate_discount()
        final_price = self.price -discounted_amount+ tax_amount
        return final_price
    
    def get_product_category(self):
        return self.CATEGORY
