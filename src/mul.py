from src.base_operation import CalculatorOperation


class MultiplyOperation(CalculatorOperation):
    """두 실수의 곱셈 연산을 수행하는 계산기 연산 클래스."""

    def calculate(self, a: float, b: float) -> float:
        """두 실수를 곱한 결과를 반환합니다.

        Args:
            a (float): 첫 번째 피연산자.
            b (float): 두 번째 피연산자.

        Returns:
            float: 두 실수의 곱 결과값 (a * b).
        """
        return a * b