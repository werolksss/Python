import unittest
from calculator_with_history import CalculatorWithHistory

class TestCalculatorIntegration(unittest.TestCase):

    def test_addition_with_history(self):
        calc = CalculatorWithHistory()
        result = calc.perform_addition(5, 3)

        self.assertEqual(result, 8)
        history = calc.get_operation_history()
        self.assertIn("5 + 3 -> 8", history)

    def test_subtraction_with_history(self):
        calc = CalculatorWithHistory()
        result = calc.perform_subtraction(10, 4)

        self.assertEqual(result, 6)
        history = calc.get_operation_history()
        self.assertIn("10 - 4 -> 6", history)

    def test_multiple_operations_history(self):
        calc = CalculatorWithHistory()
        calc.perform_addition(1, 1)
        calc.perform_subtraction(5, 2)

        history = calc.get_operation_history()
        expected = ["1 + 1 -> 2", "5 - 2 -> 3"]

        self.assertEqual(len(history), 2)
        self.assertEqual(history, expected)

if __name__ == "__main__":
    unittest.main()