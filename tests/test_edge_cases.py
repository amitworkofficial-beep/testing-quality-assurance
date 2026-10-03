import unittest
from calculator import add, divide, is_even


class TestEdgeCases(unittest.TestCase):

    def test_add_negative_numbers(self):
        self.assertEqual(add(-10, -5), -15)

    def test_add_zero(self):
        self.assertEqual(add(0, 10), 10)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_even_zero(self):
        self.assertTrue(is_even(0))

    def test_even_negative_number(self):
        self.assertTrue(is_even(-4))


if __name__ == "__main__":
    unittest.main()