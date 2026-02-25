# /learn-rules - Rule Learner

> 리뷰 패턴을 학습하여 QA 규칙을 강화합니다. 반복되는 리뷰 피드백을 규칙으로 정형화합니다.

---

## 1. 개요

- **역할**: 리뷰 결과에서 반복 패턴을 추출하여 규칙 DB에 저장
- **호출 시점**: 리뷰 완료 후 자동 (Orchestrator 호출), 또는 수동 요청
- **출력**: `data/rules/rule_{id}.json`

---

## 2. 실행

```
사용자: /learn-rules
사용자: /learn-rules list
사용자: /learn-rules disable RULE-001
사용자: /learn-rules add "모달에서 ESC 키 동작 TC 필수"
```

---

## 3. 학습 소스

| 소스 | 경로 | 학습 대상 |
|------|------|-----------|
| Format Checker 결과 | `data/reviews/format_*.json` | 반복 양식 위반 패턴 |
| Spec Reviewer 결과 | `data/reviews/spec_review_*.json` | 반복 누락 항목 |
| QA Reviewer 결과 | `data/reviews/qa_review_*.json` | 반복 엣지케이스 패턴 |
| 팀장 피드백 | 승인 시 코멘트 | 수동 규칙 추가 |

---

## 4. 규칙 형식

```json
{
  "rule_id": "RULE-001",
  "source": "qa_review",
  "category": "edge_case",
  "pattern": "달력/날짜 선택 UI에서 브라우저 뒤로가기 TC 누락",
  "frequency": 3,
  "projects": ["SAY", "BAY"],
  "recommendation": "달력/모달 UI 있는 화면에서 브라우저 뒤로가기 TC 필수 추가",
  "auto_apply": true,
  "severity": "중간",
  "status": "active"
}
```

---

## 5. 학습 프로세스

1. **수집**: `data/reviews/` 리뷰 JSON 스캔
2. **패턴 추출**: 유사 피드백 그룹화
3. **빈도 분석**: 2회 이상 반복 → 규칙 후보
4. **규칙 생성**: `data/rules/`에 저장
5. **적용**: `auto_apply: true` 규칙은 이후 리뷰 시 자동 체크

---

## 6. 리뷰 에이전트 연동

- `/review-spec`, `/review-qa` 실행 시 active 규칙 참조
- `/write-tc` 실행 시 해당 패턴 TC 사전 생성
- 규칙은 누적 (삭제 안 함, status를 inactive로 변경)
- 팀장 수동 추가 규칙은 `source: "manual"`
