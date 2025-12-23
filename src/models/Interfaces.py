from abc import ABC, abstractmethod
class DiscountableInterface(ABC):
    @abstractmethod
    def calculate_discount(self):
        pass

class TaxableInterface(ABC):
    @abstractmethod
    def calculate_tax(self):
        pass
