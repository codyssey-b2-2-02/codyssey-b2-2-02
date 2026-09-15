# Conflict Resolution Log

> 팀 전체 최소 2회 이상 기록 (그중 1회 이상은 "비자명 충돌"이어야 함 — 아래 둘 중 하나 충족:
> ① 같은 파일의 같은 hunk를 서로 다르게 수정 / ② 한쪽은 파일 이동·이름변경·삭제, 다른 한쪽은 내용 수정)

## 충돌 기록 #1

### 참여자

- 작성자: 이아인
- 상대: 김문정

### 상황 (What happened)

- src/add.py를 leeaain2025가 add_operation.py로 rename하는 동안, 본인이 같은 파일에 docstring 예시(Example) 블록을 추가하는 PR을 먼저 merge함
- rename PR이 main과 divergent 상태가 되어 pull 시 충돌 발생

### 충돌 내용 (Conflict markers)

```txt
<<<<<<< HEAD:src/add_operation.py
    Example:
        >>> AddOperation().calculate(1.0, 2.0)
        10.0
=======
    Example:
        >>> AddOperation().calculate(1.0, 2.0)
        3.0
>>>>>>> b470b92:src/add.py
```

### 해결 과정 (How)

- `git pull --no-rebase origin main`으로 병합 진행
- 파일명은 rename된 add_operation.py 유지
- 예시값은 실제 계산 결과에 맞는 3.0으로 통일 (10.0은 오기)
- `git add` + `commit`(5a35ad5)으로 병합 커밋 생성 후 push

### 결과 (Outcome)

- PR #16에서 정상적으로 conflict 해소, main에 merge 완료

### 배운 점 (Learnings)

- 파일 rename과 내용 수정이 같은 파일에서 동시에 일어나면 rename/modify 충돌이 남
- 겹치는 부분이 없으면 git이 자동으로 merge하지만, 같은 줄을 건드리면 수동 해결 필요

---

## 충돌 기록 #2

### 참여자

- 작성자: 김상원
- 상대: 김문정

### 상황 (What happened)
main 브랜치의 최신 내역을 반영하기 위해 feature/rebase-test 브랜치에서 git rebase cbb8c9699bcf701c1e3c7a7683b125310d292a84
동일한 파일(src/add_operation.py)의 같은 줄이 Rebase 적용 과정에서 자명한(Textual) 충돌이 발생하여 작업이 일시 정지됨.

### 충돌 내용 (Conflict markers)
from base_operation import CalculatorOperation


class AddOperation(CalculatorOperation):
    def calculate(self, num1: float, num2: float) -> float:
        """두 개의 실수를 더한 결과를 반환합니다.

        Args:
            num1 (float): 첫 번째 실수 입력값
            num2 (float): 두 번째 실수 입력값

        Returns:
            float: num1과 num2의 합
<<<<<<< HEAD

        Example:
=======

    Example:
>>>>>>> 013727e (fix: add_operatino: rename)
AddOperation().calculate(1.0, 2.0)
            3.0
        """
        return num1 + num2

if name == "main":
    op = AddOperation()

    assert op.calculate(1.0, 2.0) == 3.0
    assert op.calculate(-1.0, -2.0) == -3.0
    assert op.calculate(0.0, 5.0) == 5.0
    assert op.calculate(1.5, 2.3) == 3.8

    print("모든 테스트 통과")
    print(op.calculate(1.0, 2.0))  # 3.0

### 해결 과정 (How)

에디터로 srcs/add_operation.py 파일을 열어 <<<<<<<, =======, >>>>>>> 충돌 마커 줄을 완전히 제거하고 최종 남길 코드로 정돈함.

git add srcs/add_operation.py 명령어를 실행하여 충돌 해결 상태를 스테이징 영역(Index)에 등록함.

git rebase --continue 명령어를 실행하여 일시 정지되었던 리베이스 프로세스를 재개하고 끝까지 완료함.

### 결과 (Outcome)

충돌이 정상 해결되고 feature/rebase-test 브랜치의 커밋들이 main 브랜치 최신 커밋 위로 일렬로 성공적으로 재설정됨.

불필요한 머지 커밋(Merge Commit) 없이 깔끔한 선형(Linear) 커밋 히스토리가 완성됨.

### 배운 점 (Learnings)
Rebase 진행 중 HEAD의 의미: Rebase 충돌 시 <<<<<<< HEAD 영역은 내 작업 브랜치가 아니라, 리베이스의 베이스(Base)가 되는 대상 브랜치(main)의 커밋 상태를 가리킴을 이해함.

자명한 충돌 처리 흐름: 동일 라인 수정으로 유발되는 자명한 충돌은 Git이 안전하게 정지해주므로, 마커 정돈 후 git commit이 아닌 git add 및 git rebase --continue로 마무리해야 함을 확인함.