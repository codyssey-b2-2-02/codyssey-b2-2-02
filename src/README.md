# 구현 목록

> 각자 구현한 연산을 아래 표에 한 줄씩 추가합니다.
> **여러 명이 비슷한 시점에 같은 위치(표 맨 아래)에 행을 추가하도록 하면 자연스럽게 병합 충돌이 발생합니다** — 충돌 해결 실습 요건을 이 파일에서 채우는 용도.

| 연산 | 파일             | 설명           | 담당자 |
| ---- | ---------------- | -------------- | ------ |
| add  | add_operation.py | 두 실수를 더함 | 김문정 |
| mul  | mul.py           | 두 실수를 곱함 | 김상원 |
| sub  | sub.py           | 두 실수를 뺌   | 이아인 |

## 실행 예시

```bash
python3
>>> from add_operation import AddOperation
>>> AddOperation().calculate(1.0, 2.0)
3.0
>>> from sub import SubtractOperation
>>> SubtractOperation().calculate(5.0, 3.0)
2.0
```
