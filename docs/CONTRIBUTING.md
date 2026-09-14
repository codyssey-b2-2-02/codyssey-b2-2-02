# Contributing Guide

## 브랜치 전략 (GitHub Flow)
- `main`: 항상 배포 가능한 상태 (= 팀 기준에서 "깨지지 않는 상태")
- `feature/*`: 작업 단위 브랜치
- 우리 팀이 GitHub Flow를 선택한 이유 (3줄 이내):
  - [ ]
  - [ ]
  - [ ]

## 브랜치 네이밍 규칙
- 형식: `feature/<이름>-<작업내용>`
- 예: `feature/kim-math-utils`, `feature/lee-string-utils`

## 커밋 메시지 컨벤션
- 형식: `feat: <요약>` / `fix: <요약>` / `docs: <요약>` / `refactor: <요약>`
- 금지 (의미없는 메시지로 간주):
  - 변경 대상을 유추할 수 없는 단어만 있는 경우 — `update`, `fix`, `temp`, `wip`, `final` 등
  - 무엇을/왜 바꿨는지 드러나지 않는 경우 — `bug fix`, `edit file` 등

## PR 규칙
- 모든 `feature/*` 브랜치는 PR을 통해서만 `main`에 병합
- 병합 조건: 리뷰어 최소 1명 승인(approve)
- PR 본문 필수 항목:
  ```
  ## 연결 이슈
  - Closes #<issue_number>

  ## 변경 사항 (What)
  -

  ## 변경 이유 (Why)
  -

  ## 테스트/검증 방법 (How)
  - [ ] 로컬 실행/간단 테스트
  - [ ] 충돌 가능성 체크(필요 시)
  ```

## 코드 리뷰 규칙
- "LGTM/좋아요"만 있는 리뷰 금지 — 라인/파일 근거의 실질 코멘트 1개 이상 필수
  - 예: 특정 라인 기반 질문, 대안 제안, 리스크 지적, 개선 제안
- 리뷰어-작성자 간 최소 1회 이상 상호작용(답글/수정 반영) 기록 남기기

## 충돌 대응 흐름
1. 충돌 발생 → 팀 채널에 공유
2. 원인 파악 (같은 hunk 수정 / 파일 이동·삭제 vs 내용 수정 등)
3. 해결 (keep both / choose one / refactor 중 택)
4. `docs/conflict-resolution.md`에 기록

## 팀원별 담당 (필요 시 작성)
| 이름 | GitHub ID | 담당 영역 |
|---|---|---|
| | | |
