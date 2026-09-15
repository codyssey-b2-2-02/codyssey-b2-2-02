from src.base_operation import CalculatorOperation

class AddOperation(CalculatorOperation):
    def calculate(self, a:float, b:float)->float:
        return a * b