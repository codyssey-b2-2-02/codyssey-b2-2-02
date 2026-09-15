from base_operation import CalculatorOperation


class AddOperation(CalculatorOperation):
    def calculate(self, num1: float, num2: float) -> float:
        """두 개의 실수를 더한 결과를 반환합니다.

        Args:
            num1 (float): 첫 번째 실수 입력값
            num2 (float): 두 번째 실수 입력값

        Returns:
            float: num1과 num2의 합

        Example:
            >>> AddOperation().calculate(1.0, 2.0)
            3.0

        """
        return num1 + num2

if __name__ == "__main__":
    op = AddOperation()

    assert op.calculate(1.0, 2.0) == 3.0
    assert op.calculate(-1.0, -2.0) == -3.0
    assert op.calculate(0.0, 5.0) == 5.0
    assert op.calculate(1.5, 2.3) == 3.8

    print("모든 테스트 통과")
    print(op.calculate(1.0, 2.0))  # 3.0
