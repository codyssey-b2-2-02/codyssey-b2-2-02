# History Cleanup (보너스)

## 대상 브랜치
- docs/history-cleanup-demo (김문정)

## 정리 전 (rebase 전)
```
794f0d4 (HEAD -> docs/history-cleanup-demo) temp~
78581da fix typo
0e6fc2a (origin/main, origin/HEAD, main) Merge pull request #26 from codyssey-b2-2-02/docs/final-check
```

## 정리 방법
```bash
git rebase -i HEAD~2
```
- `fix typo`는 `pick` 유지, `temp~`만 `squash`로 변경
- 커밋 메시지를 컨벤션에 맞게 재작성: `docs: readme: 히스토리 정리 실습용 문구 추가 (rebase -i squash 데모)`
- `git rebase --continue`로 마무리

## 정리 후 (rebase 후)
```
64c31b8 (HEAD -> docs/history-cleanup-demo) docs: readme: 히스토리 정리 실습용 문구 추가 (rebase -i squash 데모)
0e6fc2a (origin/main, origin/HEAD, main) Merge pull request #26 from codyssey-b2-2-02/docs/final-check
ab3b8ea (origin/docs/final-check, docs/final-check) docs: 미션 최종 점검 반영
```

## 배운 점
- `squash`는 여러 커밋을 하나로 합치면서 커밋 메시지도 새로 작성할 수 있어, "의미 없는 중간 커밋(fix typo, temp)"을 정리해 히스토리를 깔끔하게 남길 수 있음
- rebase -i는 아직 merge되지 않은 개인 브랜치에서만 안전하게 사용 가능 — 공유된(main 등) 브랜치에서 쓰면 팀원과 히스토리가 어긋남
- rebase 완료 후에도 `git status`로 "clean" 상태와 `REBASE` 표시가 사라졌는지 확인하는 습관이 필요함 (`git rebase --continue`를 안 치면 중간 상태로 남을 수 있음)
