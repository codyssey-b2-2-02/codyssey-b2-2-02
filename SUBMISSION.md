# Submission — 팀원별 Issue / PR 현황

## 김문정 (팀장)

- Issue: [#4](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/issues/4), [#12](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/issues/12), [#14](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/issues/14)
- PR: [#5](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/5)(병합됨) — add 구현, [#13](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/13)(병합됨) — test_add, [#15](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/15)(병합됨) — docstring 보강
- 코드 리뷰 작성: mul PR [#2](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/2) — 1차 리뷰(Request changes: calculate 메서드명·파라미터명 지적), 2차 리뷰(Approve: MultiplyOperation→MulOperation 클래스명 지적) / mul PR [#10](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/10) — 클래스명(MultiplyOperation→MulOperation) 지적 후 Approve
- 리뷰 반영 경험: add PR [#5](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/5) — 이아인님이 지적한 파라미터명(a,b→num1,num2)·DocString 누락을 커밋(fix: add: 리뷰 반영...)으로 반영

## 김상원

- Issue: [#2](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/issues/2), [#10](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/issues/10)
- PR: [#2](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/2)(병합됨) — feat mul(곱함수 구현), [#10](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/10)(병합됨) — fix mul.py (독스트링 부족한 점과 이름이 잘못된 점을 해결)
- 코드 리뷰 작성: [#7](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/7)(Feature/sum) — 1차 리뷰, 정상적으로 프로그램이 목표대로 작성됨을 확인했으나 문서 설명이 부족한 것을 확인하고 안내함. [#11](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/11)(fix: sub_operation.py -> sub.py) — 그 후 수정된 부분이 잘 작성되어 완성된 피드백을 안내함
- 리뷰 반영 경험: feat:mul [#2](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/2) — 함수의 이름과 내용이 맞지 않아서 수정을 요청받았고 완성함

## 이아인

- Issue: [#3](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/issues/3)(feat: sum 구현), [#6](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/issues/6)(feat: sub 구현), [#9](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/issues/9)(fix: sub_operation.py: sub.py)
- PR: [#7](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/7)(Feature/sum), [#11](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/11)(fix: sub_operation.py -> sub.py), [#16](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/16)(refactor: add: 파일명을 add_operation.py로 변경)
- 코드 리뷰 작성: [#5](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/5)(feat: add 구현), [#13](https://github.com/codyssey-b2-2-02/codyssey-b2-2-02/pull/13)(feat: add 테스트 추가)
- 리뷰 반영 경험: 김상원님이 지적해주신 파일명 수정, Doc string 추가를 반영함

---

## Git 히스토리 증빙

- 전체 로그가 길어 별도 파일로 관리합니다.
- 전체 내역: [gitlog.txt](./gitlog.txt)

### 요약 (PR 병합 순서)

```
8c49895  docs: 저장소 구조 및 협업 템플릿 추가
7428c65  feat: 사칙연산 프로젝트 초기 구조 정리
ec53c30  feat: CODEOWNERS 설정
#2   feat/mul              → mul 연산 구현
#5   feature/add           → add 연산 구현
#7   feature/sum           → sub 연산 구현
#11  fix/sub               → sub_operation.py -> sub.py 파일명 정리
#10  fix/mul               → mul.py 클래스명/docstring 리뷰 반영
#13  feature/add-test      → add 단위 테스트 추가
#15  feature/add-comment   → add docstring 보강 (→ #16과 충돌 발생 지점)
#16  feature/rename-add    → add.py rename + 비자명 충돌 해결 (기록 #1)
#18  docs/conflict-log     → 충돌 해결 기록 문서화
#20  docs/mission-logs     → 트러블슈팅/인터페이스 문서 정리
#22  docs/submission-leeaain → 이아인 활동 기록
#25  docs/submit           → 김상원 PR/리뷰/충돌(기록 #2)/트러블슈팅(reset) 기록
```

## 간단한 결과물 (택 1) — 완성 기준 확인

- [x] 선택한 유형: A (유틸 함수 모음)
- [x] 팀원별 최소 1건 기여 커밋 확인 (add_operation.py: 김문정 / mul.py: 김상원 / sub.py: 이아인)
- [x] 사용 예시: `src/README.md`의 구현 목록 표 + 실행 예시로 증빙
