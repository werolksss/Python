from calculator_service import CalculatorService
from broken_history_service import BrokenHistoryService

class CalculatorWithBrokenHistory:
    def __init__(self):
        self.calculator = CalculatorService()
        self.history = BrokenHistoryService()

    def perform_addition(self, a: int, b: int) -> int:
        result = self.calculator.add(a, b)
        self.history.save_record(f"{a} + {b}", result)  # Здесь будет исключение!
        return result

    def perform_subtraction(self, a: int, b: int) -> int:
        result = self.calculator.subtract(a, b)
        self.history.save_record(f"{a} - {b}", result)  # Здесь будет исключение!
        return result

    def get_operation_history(self) -> list:
        return self.history.get_history()