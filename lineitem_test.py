import unittest

class LineItems_(unittest.TestCase):
    
    def setUp(self):
        self.fixture = self._Fixture()
        self.product = Product()
        self.line_items = LineItems()
        self.transaction = Transaction()
        
    def test_add_line_items(self):
        product = [{'code': '123', 'peanut_butter': 3, 'price': 500}]
        self.fixture.given_a_product_that_is_added_to_line_item(product, 2) 
        self.fixture.when_add_to_line_item_is_called()
        self.fixture.then_result_should_be(2)
        
    def test_subtract_line_items(self):
        product = [{'code': '123', 'peanut_butter': 3, 'price': 500}]
        self.fixture.given_a_product_that_is_in_line_item(product, 1)
        self.fixture.when_subtract_from_line_item_is_called()
        self.fixture.then_result_should_be(1)
        
    def test_display_line_items_list_when_transaction_is_made(self):
        self.fixture.given_the_transaction_is_made(self.transaction)
        self.fixture.when_display_line_items_is_called()
        self.fixture.then_result_should_be(self.transaction.display_line_items())
    
    def test_update_quantity_of_line_item(self):
        self.fixture.given_line_items(self.line_items.line_items())   
        self.fixture.when_update_quantity_of_line_item_is_called()
        self.fixture.then_result_should_be(True)
     
    def test_calculate_total_balance_of_line_items(self):
        self.fixture.given_line_items(self.line_items.line_items())   
        self.fixture.when_calculate_total_balance_is_called()
        self.fixture.then_result_should_be(self.line_items.calculate_total())
     
    def test_display_total_balance_of_line_items(self):
        self.fixture.given_line_items(self.line_items.line_items())   
        self.fixture.when_display_total_balance_is_called()
        self.fixture.then_result_should_be(self.line_items.total())
        
    def test_void_the_line_item(self):
        self.fixture.given_line_items(self.line_items.line_items())
        self.fixture.when_void_the_line_item_is_called()
        self.fixture.then_result_should_be(product = False)
    
    def test_display_all_voided_and_non_voided_line_items(self):
        self.fixture.given_all_line_items(self.line_items.all_line_items())
        self.fixture.when_display_all_line_items_is_called()
        self.fixture.then_result_should_be(self.line_items.all_line_items())    

                 
    class _Fixture(unittest.TestCase):
        
        def __init__(self, methodName: str = ...) -> None:
            super().__init__(methodName)
            self.product = Product()
            self.line_items = LineItems()
        
        def given_a_product_that_is_added_to_line_item(self, product):
            self._product = product
            
        def given_a_product_that_is_in_line_item(self, product):
            self._product = product
            
        def given_line_items(self, line_items):
            self._line_items = line_items
            
        def given_all_line_items(self, all_line_items):
            self.all_line_items = all_line_items
        
        def when_add_to_line_item_is_called(self):
            self.result = self.line_items.add_item(self._product, 2)
            
            
        def when_subtract_from_line_item_is_called(self):
            pass
            
        def given_the_transaction_is_made(self):
            pass
            
        def when_display_line_items_is_called(self):
            pass
            
        def when_update_quantity_of_line_item_is_called(self):
            pass
            
        def when_calculate_total_balance_is_called(self):
            pass
            
        def when_display_total_balance_is_called(self):
            pass
        
        def when_void_the_line_item_is_called(self):
            pass
        
        def when_display_all_line_items_is_called(self):
            pass
                  
        def then_result_should_be(self):
            pass
        
        def then_result_should_be(self):
            pass
            
                    
if __name__ == '__main__':
    unittest.main()     