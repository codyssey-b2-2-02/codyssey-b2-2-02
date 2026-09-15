# 📌 사칙연산 프로젝트 인터페이스 및 구현 규칙 (Python)

이 문서는 팀원 3명이 각자 `add`, `sub`, `mul` 기능을 독립적으로 구현할 때, 파이썬의 `typing` 모듈을 활용하여 엄격한 타입 규격을 맞추기 위한 약속입니다.

## 1. 공통 구현 규칙

- **타입 힌트 필수 적용**: 모든 입력과 출력은 명시적인 타입 힌트(`float`)를 포함해야 합니다.
- **정적 타입 검사(MyPy)**: 코드 작성 후 `mypy` 검사를 통과해야 `main` 브랜치로 병합(Merge)이 가능합니다.
- **담당자 및 브랜치**:
    - ➕ **더하기 (Add)**: `feature/add` 브랜치
    - ➖ **빼기 (Sub)**: `feature/sub` 브랜치
    - ✖️ **곱하기 (Mul)**: `feature/mul` 브랜치

> 브랜치명은 `docs/CONTRIBUTING.md`의 네이밍 규칙(`feature/<작업내용>`)을 그대로 따릅니다.

## 2. 기본 인터페이스 및 추상 클래스 구조

모든 팀원은 `base_operation.py`에 정의된 `CalculatorOperation` 추상 클래스를 상속받아 구현해야 합니다.

```python
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
```
