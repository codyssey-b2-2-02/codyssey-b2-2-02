from base_operation import CalculatorOperation


class SumOperation(CalculatorOperation):
    def calculate(self, num1: float, num2: float) -> float:
        return num1 + num2
