import unittest

def calculate_total_price(unit_price, quantity, tax_rate):
    total_price = (unit_price * quantity) * (1 + tax_rate)
    return total_price

class TestCalculateTotalPrice(unittest.TestCase):

    def test_calculate_total_price(self):
        self.assertEqual(calculate_total_price(10, 5, 0.1), 55.0)
        self.assertEqual(calculate_total_price(15.5, 2, 0.05), 32.475)
        self.assertEqual(calculate_total_price(100, 1, 0.0), 100.0)
    
    def test_calculate_total_price_with_zero_quantity(self):
        self.assertEqual(calculate_total_price(20, 0, 0.15), 0.0)

if __name__ == '__main__':
    unittest.main()
