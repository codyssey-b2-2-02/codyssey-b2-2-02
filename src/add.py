from base_operation import CalculatorOperation


class AddOperation(CalculatorOperation):
    def calculate(self, num1: float, num2: float) -> float:
        """두 개의 실수를 더한 결과를 반환합니다.

        Args:
            num1 (float): 첫 번째 실수 입력값
            num2 (float): 두 번째 실수 입력값

        Returns:
            float: num1과 num2의 합
        """
        return num1 + num2