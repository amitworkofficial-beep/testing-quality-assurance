import unittest
from calculator_service import calculate_total, calculate_average, calculate_bill


class TestCalculatorIntegration(unittest.TestCase):

    def test_calculate_total(self):
        result = calculate_total(100, 5)
        self.assertEqual(result, 500)

    def test_calculate_average(self):
        result = calculate_average(500, 5)
        self.assertEqual(result, 100)

    def test_calculate_bill(self):
        result = calculate_bill(100, 5, 5)

        self.assertEqual(result["total"], 500)
        self.assertEqual(result["average"], 100)


if __name__ == "__main__":
    unittest.main()