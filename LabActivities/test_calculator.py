import unittest

from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
        
    def tearDown(self):
        del self.calc
    
    def test_add_empty_string_returns_zero(self):
        result = self.calc.add("")
        self.assertEqual(0, result)
    
    def test_add_one_number_returns_number(self):
        result = self.calc.add("1")
        self.assertEqual(1, result)
    
    def test_add_two_positive_numbers(self):
        result = self.calc.add("1,2")
        self.assertEqual(3, result)
    
    def test_add_two_negative_numbers(self):
        result = self.calc.add("-1,-2")
        self.assertEqual(-3, result)
    
    def test_add_one_positive_one_negative_number(self):
        result = self.calc.add("1,-2")
        self.assertEqual(-1, result)
    
    def test_add_input_numbers_instead_of_string(self):
        with self.assertRaises(TypeError):
            self.calc.add(1,2)
    
    def test_subtract_empty_string_returns_zero(self):
        result = self.calc.subtract("")
        self.assertEqual(0, result)
    
    def test_subtract_one_number_returns_number(self):
        result = self.calc.subtract("1")
        self.assertEqual(1, result)
            
    def test_subtract_two_positive_numbers(self):
        result = self.calc.subtract("1,2")
        self.assertEqual(-1, result)
    
    def test_subtract_two_negative_numbers(self):
        result = self.calc.subtract("-1,-2")
        self.assertEqual(1, result)
    
    def test_subtract_one_positive_one_negative_number(self):
        result = self.calc.subtract("1,-2")
        self.assertEqual(3, result)
    
    def test_subtract_input_numbers_instead_of_string(self):
        with self.assertRaises(TypeError):
            self.calc.subtract(1,2)
    
    def test_multiply_empty_string_returns_zero(self):
        result = self.calc.multiply("")
        self.assertEqual(0, result)
    
    def test_multiply_one_number_returns_number(self):
        result = self.calc.multiply("1")
        self.assertEqual(1, result)
            
    def test_multiply_two_positive_numbers(self):
        result = self.calc.multiply("1,2")
        self.assertEqual(2, result)
    
    def test_multiply_two_negative_numbers(self):
        result = self.calc.multiply("-1,-2")
        self.assertEqual(2, result)
    
    def test_multiply_one_positive_one_negative_number(self):
        result = self.calc.multiply("1,-2")
        self.assertEqual(-2, result)
    
    def test_multiply_two_numbers_one_is_zero(self):
        result = self.calc.multiply("0,2")
        self.assertEqual(0, result)
    
    def test_multiply_input_numbers_instead_of_string(self):
        with self.assertRaises(TypeError):
            self.calc.multiply(1,2)
    
    def test_divide_empty_string_returns_zero(self):
        result = self.calc.divide("")
        self.assertEqual(0, result)
    
    def test_divide_one_number_returns_number(self):
        result = self.calc.divide("1")
        self.assertEqual(1, result)
            
    def test_divide_two_positive_numbers(self):
        result = self.calc.divide("4,2")
        self.assertEqual(2, result)
    
    def test_divide_two_negative_numbers(self):
        result = self.calc.divide("-4,-2")
        self.assertEqual(2, result)
    
    def test_divide_one_positive_one_negative_number(self):
        result = self.calc.divide("4,-2")
        self.assertEqual(-2, result)
    
    def test_divide_two_numbers_first_is_zero(self):
        result = self.calc.divide("0,2")
        self.assertEqual(0, result)
        
    def test_divide_result_is_float(self):
        result = self.calc.divide("1,2")
        self.assertEqual(0.5, result)
    
    def test_divide_two_numbers_second_is_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide("1,0")
    
    def test_divide_input_numbers_instead_of_string(self):
        with self.assertRaises(TypeError):
            self.calc.divide(1,2)
    
if __name__ == "__main__":
    # Runs the tests and outputs results:
    unittest.main()