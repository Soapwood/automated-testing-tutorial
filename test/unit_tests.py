import unittest
from business_logic import perform_calculation, calculate_discounted_price, is_prime_number, get_average

class BusinessLogicTestCase(unittest.TestCase):
    def test_addition(self):
        result = perform_calculation(2, 3)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = perform_calculation(-5, 10)
        self.assertEqual(result, 5)

    def test_zero(self):
        result = perform_calculation(0, 10)
        self.assertEqual(result, 10)

    def test_decimal_numbers(self):
        result = perform_calculation(3.5, 2.5)
        self.assertEqual(result, 6.0)

    def test_large_numbers(self):
        result = perform_calculation(1000000, 2000000)
        self.assertEqual(result, 3000000)

class BusinessLogicTestCase(unittest.TestCase):
    def test_calculate_discounted_price(self):
        # Test case 1: Positive discount rate
        result = calculate_discounted_price(100, 10)
        self.assertEqual(result, 90)

        # Test case 2: Zero discount rate
        result = calculate_discounted_price(200, 0)
        self.assertEqual(result, 200)

        # Test case 3: Negative discount rate
        result = calculate_discounted_price(150, -20)
        self.assertEqual(result, 180)

    def test_is_prime_number(self):
        # Test case 1: Prime number
        result = is_prime_number(7)
        self.assertTrue(result)

        # Test case 2: Non-prime number
        result = is_prime_number(10)
        self.assertFalse(result)

        # Test case 3: Negative number
        result = is_prime_number(-5)
        self.assertFalse(result)

    def test_get_average(self):
        # Test case 1: List with positive numbers
        result = get_average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3)

        # Test case 2: Empty list
        result = get_average([])
        self.assertIsNone(result)

        # Test case 3: List with negative numbers
        result = get_average([-10, -5, 0, 5, 10])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()