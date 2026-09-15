from src.base_operation import CalculatorOperation

class MulOperation(CalculatorOperation):
    def mul(self, a:float, b)->float:
        return a * b