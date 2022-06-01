import unittest

from tdd_strings import String

class StringTest(unittest.TestCase):
    
    def tearDown(self):
        del self.string
    
    def test_to_upper(self):
        self.string = String("hello")
        result = self.string.to_upper()
        self.assertEqual("HELLO", result)
    
    def test_to_lower(self):
        self.string = String("HELLO")
        result = self.string.to_lower()
        self.assertEqual("hello", result)
        
    def test_reverse(self):
        self.string = String("Hello")
        result = self.string.reverse()
        self.assertEqual("olleH", result)

if __name__ == "__main__":
    unittest.main()