import unittest
from scratch_pad_001 import squared

class TestSquaredFunction(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(squared(5), 25)

    def test_negative_number(self):
        self.assertEqual(squared(-3), 9)

    def test_zero(self):
        self.assertEqual(squared(0), 0)

    def test_large_number(self):
        self.assertEqual(squared(1000), 1000000)

    def test_float_number(self):
        self.assertEqual(squared(2.5), 6.25)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            squared("hello")

if __name__ == '__main__':
    unittest.main()
