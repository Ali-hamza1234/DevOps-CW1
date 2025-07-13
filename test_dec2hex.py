import unittest
from Dec2Hex import decimal_to_hex

class TestDec2Hex(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(decimal_to_hex(10), "A")

    def test_zero(self):
        self.assertEqual(decimal_to_hex(0), "0")

    def test_max_case(self):
        self.assertEqual(decimal_to_hex(255), "FF")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex("abc")

if __name__ == '__main__':
    unittest.main()
