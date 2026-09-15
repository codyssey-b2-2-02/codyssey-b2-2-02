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

- 작성자: <name>
- 상대: <name>

### 상황 (What happened)

-

### 충돌 내용 (Conflict markers)

```txt
<<<<<<< HEAD
...
=======
...
>>>>>>> feature/...
```

### 해결 과정 (How)

-

### 결과 (Outcome)

-

### 배운 점 (Learnings)

-
