# QA-MEDI-PLUGIN v2.0

QA AI 에이전트 팀 운영 시스템 — Orchestrator 기반 자율 협업 (12개 에이전트)

## 설치

### 1. 마켓플레이스 등록

```bash
/plugin marketplace add MediSolveAIDev/QA-MEDI-PLUGIN
```

### 2. 플러그인 설치

```bash
/plugin install qa-medi-plugin@qa-medi-plugin
```

### 프로젝트 자동 설정 (선택)

`.claude/settings.json`에 추가하면 팀원이 프로젝트 폴더를 trust할 때 자동 등록됩니다:

```json
{
  "extraKnownMarketplaces": {
    "qa-medi-plugin": {
      "source": {
        "source": "github",
        "repo": "MediSolveAIDev/QA-MEDI-PLUGIN"
      }
    }
  },
  "enabledPlugins": {
    "qa-medi-plugin@qa-medi-plugin": true
  }
}
```

## 에이전트 구성 (12개)

| # | 에이전트 | 스킬 커맨드 | 역할 |
|---|----------|-------------|------|
| 1 | Orchestrator | `/run-pipeline` | 파이프라인 관리, 에이전트 간 핸드오프 |
| 2 | Scenario Writer | `/write-scenario` | 시나리오 작성 |
| 3 | TC Writer | `/write-tc` | TC 작성 |
| 4 | Project Reporter | `/report-project` | 프로젝트별 현황 보고 |
| 5 | Bug Reporter | `/report-bug` | JIRA 버그 리포팅 |
| 6 | Format Checker | `/check-format` | TC 양식 검토 |
| 7 | Content Reviewer | `/review-tc` | 시나리오/TC 내용 리뷰 |
| 8 | Impact Analyzer | `/analyze-impact` | 크로스 프로젝트 영향도 분석 |
| 9 | Rule Learner | `/learn-rules` | 리뷰 패턴 학습 |
| 10 | Automation Assessor | `/assess-automation` | 자동화 사전 검토 |
| 11 | Test Coder | `/write-test-code` | 자동화 코드 작성 |
| 12 | Fail Analyzer | `/analyze-fail` | FAIL 원인 분석 |

## 파일 구조

```
qa_agent/
├── .claude-plugin/          ← 플러그인 설정
├── .claude/
│   ├── CLAUDE.md            ← 프로젝트 지침
│   └── skills/              ← 12개 에이전트 스킬
├── agents/                  ← 에이전트 프로필
├── config/projects/         ← 프로젝트별 설정 (SAY, BAY, SSO)
├── data/                    ← 에이전트 산출물
├── docs/                    ← 아키텍처 문서
├── templates/               ← 산출물 템플릿
└── tests/                   ← 자동화 테스트
```

## 아키텍처

상세 내용은 [docs/qa_agent_architecture.md](docs/qa_agent_architecture.md) 참조.

```
팀장 지시 → Orchestrator → 에이전트 자율 협업 → 승인 요청 → 최종 보고
```

- **7개 승인 포인트**: 계획 확인, 시나리오 리뷰, Figma 검수, TC 확정, 자동화 결정, FAIL 분석, 영향도
- **Phase 1-A**: 시나리오 확정 (Scenario Writer → Content Reviewer)
- **Phase 1-B**: TC 확정 (TC Writer → Format Checker → Content Reviewer)
- **Phase 3**: 자동화 (Automation Assessor → Test Coder → Fail Analyzer)
