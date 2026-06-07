# Day 3 과제 — 오케스트레이션 (Sub-Agent · Review Loop · State)
> PPT 개념: Sub-Agent · Review Loop · State

## 🎬 시나리오
한 에이전트가 다 하려다 컨텍스트가 터진다.
**역할(서브에이전트)을 나누고**, 후보를 검증하는 **리뷰 루프**를 만들어라.

## 🟢 기본 과제 (5~10분)
1. `course/mini_labs/day03_multi_agent_game/bug_snippet.py` 에 새 버그(예: 빈 `except:` 로 에러 삼킴)를 심고
   `run_bug_hunt_game.py` 의 `hunter` 패턴에 추가 → 잡히는지 확인.
2. `reviewer` 의 판정 규칙을 1개 더 추가(예: 'None 비교에 `==` 사용').

## 🏗 생성형 과제 — '커스텀 서브에이전트 정의' (10~20분)
`.claude/agents/secret-reviewer.md` 를 만들어 **역할/책임을 가진 서브에이전트**를 선언:
```markdown
---
name: secret-reviewer
description: 비밀 마스킹 누락만 집중 검토. 다른 작업은 하지 않는다.
tools: Read, Grep
---
너는 비밀값 마스킹 누락만 찾는 검토자다. reports/ 의 마스킹 누락을 표로 보고하라.
```
👉 오케스트레이터-워커 패턴 / 컨텍스트 격리 (이 repo의 supervisor + 5개 에이전트와 같은 개념).

## 🔥 도전 과제
5번째 역할 **Security Auditor**(보안 관점 재검토)를 추가해
`Planner → Hunter → Reviewer → Auditor → Reporter` 로 흐름을 확장.

## ✅ 완료 체크
- [ ] Hunter/Reviewer 규칙 1개씩 추가
- [ ] 커스텀 서브에이전트 정의 파일 작성
- [ ] `supervisor_graph.py --hitl` 로 오케스트레이션·HITL 재현
