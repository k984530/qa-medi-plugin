# qa-medi-plugin

의료 QA 자동화를 위한 Claude Code 플러그인.

## 구성 요소

| 타입 | 경로 | 설명 |
|------|------|------|
| Agent | `agents/qa-agent.md` | QA 검증 에이전트 |
| Command | `commands/qa.md` | `/qa` 슬래시 커맨드 |
| Skill | `skills/qa-skill/SKILL.md` | QA 검증 스킬 |
| Hook | `hooks/hooks.json` | 파일 수정 감지 훅 |
| MCP Server | `mcp/server.py` | 의료 용어 검증 도구 |

## 설치

```bash
pip install -r mcp/requirements.txt
```
