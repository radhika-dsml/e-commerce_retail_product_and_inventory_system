
import pytest
from datetime import datetime
from unittest.mock import patch
import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.models.Electronics import Electronics
from src.models.Interfaces import DiscountableInterface, TaxableInterface


class TestProduct:
    def test_product_price_validation_negative(self):
        """Test price validation on creation - negative price"""
        # Arrange & Act & Assert
        with pytest.raises(ValueError, match="Price cannot be negative"):
            Electronics(
                name="Test Product",
                ID="P001",
                price=10.00,
                description="Test",
                brand="Test"
            )
        def test_product_interface_implementation(self):
        #Test Product implements required interfaces
        # Arrange
            electronic_product = Electronics(
                product_id="P001",
                name="Charger",
                price=800.00,
                description="Test",
                brand="Test",
                category="Electronics"
            )
            
            # Assert
            assert isinstance(electronic_product, DiscountableInterface), "Product should implement Discountable interface"
            assert isinstance(electronic_product, TaxableInterface), "Product should implement Taxable interface"
            
            # Test abstract methods exist and can be called
            discount = electronic_product.calculate_discount()
            assert discount == 0.0, "Base product should return 0 discount"
            
            discount_percent = electronic_product.get_discount_percentage()
            assert discount_percent == 0.0, "Base product should return 0 discount percentage"
            
            tax = electronic_product.calculate_tax()
            assert tax == 0.0, "Base product should return 0 tax"
            
            tax_rate = electronic_product.tax_rate
            assert tax_rate == 0.0, "Base product should return 0 tax rate"
        
