from base_operation import CalculatorOperation


class SubtractOperation(CalculatorOperation):
    def calculate(self, num1: float, num2: float) -> float:
        """Subtract b from a and return the result."""
        return num1 - num2
