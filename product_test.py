from ast import Pass
import unittest

class Product(unittest.TestCase):
    
    def setUp(self):
        self.fixture = self._Fixture()
        
    def test_product_is_valid(self):
        product = [{'code': '123', 'peanut_butter': 3, 'price': 500}]
        self.fixture.given_a_product(product)
        self.fixture.when_verify_product_is_called()
        self.fixture.then_result_should_be("verified")
    
    def test_product_availability(self):
        product = [{'code': '123', 'peanut_butter': 3, 'price': 500}]
        self.fixture.given_a_product(product)
        self.fixture.when_check_product_availability_is_called()
        self.fixture.then_result_should_be('Avalaible')
    
    def test_check_product_quantity(self):
        product = [{'code': '123', 'peanut_butter': 3, 'price': 500}]
        self.fixture.given_a_product(product)
        self.fixture.when_check_product_quantity_is_called()
        self.fixture.then_result_should_be(3)
        
    def test_update_product_quantity(self):
        product = [{'code': '123', 'peanut_butter': 3, 'price': 500}]
        self.fixture.given_a_product(product)
        self.fixture.when_update_product_quantity_is_called()
        self.fixture.then_result_should_be(4)
    
    def test_update_product_price(self):
        product = [{'code': '123', 'peanut_butter': 3, 'price': 500}]
        self.fixture.given_a_product(product)
        self.fixture.when_update_product_price_is_called()
        self.fixture.then_result_should_be(4)
    
    class _Fixture(unittest.TestCase):
        
        def __init__(self, methodName: str = ...) -> None:
            super().__init__(methodName)
            self.product = Product()
        
        def given_a_product(self, product):
            self._product = product
        
        def when_verify_product_is_called(self):
            self.result = self.product.verify_product(self._product)
        
        def when_check_product_availability_is_called(self):
            self.result = self.product.check_product_availability(self._product)
        
        def when_check_product_quantity_is_called(self):
            self.result = self.product.check_product_quantity(self._product)
        
        def when_update_product_quantity_is_called(self):
            self.result = self.product.update_product_quantity(self._product)
        
        def when_update_product_price_is_called(self):
            self.result = self.product.update_product_price(self._product)
        
        def then_result_should_be(self, result):
            self.assertAlmostEqual(self.result, result)

if __name__ == '__main__':
    unittest.main()     