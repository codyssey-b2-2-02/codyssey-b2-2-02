from base_operation import CalculatorOperation


class AddOperation(CalculatorOperation):
    def calculate(self, a: float, b: float) -> float:
        result = a + b
        return result