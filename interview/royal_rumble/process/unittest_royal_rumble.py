import unittest
from royal_rumble import string_to_roman_number
from royal_rumble import transform_name

class TestRoyalRumble(unittest.TestCase):
    def test_success(self):
        self.assertEqual(string_to_roman_number("iv"), 4)
        self.assertEqual(string_to_roman_number("XL"), 40)
        self.assertEqual(string_to_roman_number("VII"), 7)
        self.assertEqual(string_to_roman_number("III"), 3)
        self.assertEqual(string_to_roman_number("iii"), 3)
        self.assertEqual(string_to_roman_number("XVII"), 17)
    
    def test_invalidFormat(self):
        with self.assertRaises(ValueError) as context:
            string_to_roman_number("ivii")
            string_to_roman_number("IL")
            self.assertTrue('Invalid Roman character' in context.exception)      

    def test_success_transform_name(self):
        self.assertEqual(transform_name("Abdul IV"), "Abdul 4")
        self.assertEqual(transform_name("Abdul Ghapur IV"), "Abdul Ghapur 4")    

if __name__ == '__main__':
    unittest.main()