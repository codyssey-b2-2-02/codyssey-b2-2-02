# Troubleshooting Log

> 팀 전체가 아래 4가지 시나리오를 모두 수행. 팀원별 최소 1개 시나리오에는 참여(이름/역할 명시) 필수.

## 시나리오: git commit --amend (최근 커밋 메시지 수정)
### 참여자
- <name>

### 상황
- 무엇이 문제였는지 (재현 가능한 설명)

### 시도한 명령/절차
- `git commit --amend ...`

### 결과
- 무엇이 어떻게 해결됐는지
- 주의할 점 (특히 원격 히스토리/협업 영향)

### 왜 이 방법을 선택했는가 (Why)
-

---

## 시나리오: git reset --soft HEAD~1 (로컬 커밋 취소 + 변경 유지)
### 참여자
- <name>

### 상황
-

### 시도한 명령/절차
- `git reset --soft HEAD~1`

### 결과
-

### 왜 이 방법을 선택했는가 (Why)
-

---

## 시나리오: git revert (원격에 push된 커밋 취소)
### 참여자
- <name>

### 상황
-

### 시도한 명령/절차
- `git revert <commit>`

### 결과
-

### 왜 이 방법을 선택했는가 (Why)
- reset 대신 revert를 선택한 이유 등

---

## 시나리오: git stash / git stash pop (작업 보관 후 전환)
### 참여자
- 이아인

### 상황
- 로컬 feature/sum 브랜치에서 sum.py 파일을 개발중에 팀원의 .github/CODEOWNERS 수정으로 인한 new commit & push가 발생하면서 공통 적용 요청 받으면서 작업하던 내용을 임시 저장하고 로컬 main 브랜치를 업데이트해야 하는 상황.

### 시도한 명령/절차
- `git stash` → `git stash pop`
```shell
# 임시 저장
git stash

# main 브랜치 업데이트(팀원의 변경사항 반영)
git siwtch main
git fetch origin main
git pull origin main

# 본래 브랜치로 복귀
git switch feature/sum
# 임시저장했던 내용 불러오고 목록에서 제거
git stash pop
```

### 결과
-
임시저장해두었던 코드 변경사항이 잘 원복되어 작업을 이어서 할 수 있었음. 
main 브랜치의 최신 변경사항도 독립적으로 로컬에 업데이트 되어 있음을 확인함.

### 왜 이 방법을 선택했는가 (Why)
-
작업중이던 코드의 변경사항이 완료되지 않아 커밋을 하기에는 적절하지 않은 상황이었으므로 git stash로 임시저장 함.
