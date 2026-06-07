# Day 3 — Orchestration · HITL · Audit

## 오늘의 목표
- 멀티에이전트가 "모델 수"가 아니라 "역할/책임 분리"임을 이해한다.
- Supervisor 로 여러 Agent 를 조율하고, HITL 승인과 Audit 로그를 적용한다.

---

## Mini Lab — Bug Hunt Game
- **목적**: Planner/Hunter/Reviewer/Reporter 역할 분리를 LLM 없이 함수로 체감
- **실행 명령**
  ```bash
  python course/mini_labs/day03_multi_agent_game/run_bug_hunt_game.py
  ```
- **산출물**: `reports/bug_hunt_report.md`
- **확인 포인트**: 4단계 역할이 구분돼 기록됐는가? Reviewer 가 오탐 1건을 기각했는가?
- **본 실습 연결**: 이 4역할 구조가 본 실습의 **SAST/Secret/Dependency/Threat/Report Agent** 오케스트레이션으로 확장된다.
- 자세히: `course/experiments/day03_bug_hunt_game.md`

---

## Main Lab — Supervisor 오케스트레이션 · HITL · Audit
- **목적**: 중앙 그래프가 Agent 들을 호출·검증하고, 위험 동작은 사람 승인(HITL)으로 통제
- **실행 명령**
  ```bash
  python orchestrator/supervisor_graph.py --target sample_app/          # 기본 오케스트레이션
  python orchestrator/supervisor_graph.py --target sample_app/ --hitl   # 사람 승인 게이트
  ```
- **산출물**: `reports/lab3_report.md`, `memory/audit_log.jsonl`
- **확인 포인트**: 여러 Agent 발견이 하나의 리포트로 통합됐는가? HITL 승인 흐름과 감사 로그가 동작했는가?

---

## 선택 보조: Claude/GPT 저토큰 활용
- 전체 코드베이스를 넣지 않는다.
- `python scripts/make_light_context_pack.py --day 3` 로 `reports/context_pack_day3.md` 만 생성해 복사한다.
- "이 lab3_report.md 에서 빠진 검증 단계 3개만 알려줘" 정도로 가볍게 사용한다.

---

## 완료 체크리스트
- [ ] `reports/bug_hunt_report.md` 생성 (확정/기각 구분 확인)
- [ ] `reports/lab3_report.md` 생성
- [ ] `--hitl` 승인 게이트 동작 확인
- [ ] `memory/audit_log.jsonl` 기록 확인
