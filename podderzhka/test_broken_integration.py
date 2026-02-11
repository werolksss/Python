import unittest
from calculator_with_broken_history import CalculatorWithBrokenHistory

class TestBrokenIntegration(unittest.TestCase):

    def test_addition_with_broken_history_raises_exception(self):
        calc = CalculatorWithBrokenHistory()
        with self.assertRaises(Exception) as context:
            calc.perform_addition(5, 3)

        self.assertEqual(str(context.exception), "Database error")

    def test_history_empty_when_broken(self):
        calc = CalculatorWithBrokenHistory()
        # Пытаемся выполнить операцию, но она падает
        try:
            calc.perform_addition(5, 3)
        except Exception:
            pass

        history = calc.get_operation_history()
        self.assertEqual(history, [])

if __name__ == "__main__":
    unittest.main()