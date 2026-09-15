from abc import ABC, abstractmethod


class CalculatorOperation(ABC):
    @abstractmethod
    def calculate(self, num1: float, num2: float) -> float:
        """두 개의 실수를 입력받아 계산된 실수 결과를 반환합니다.

        Args:
            num1 (float): 첫 번째 실수 입력값
            num2 (float): 두 번째 실수 입력값

        Returns:
            float: 사칙연산 결과값
        """
        pass
