# Bug Hunt Game 역할 정의 (course/mini_labs/day03_multi_agent_game/roles.md)

멀티에이전트의 핵심은 "모델 수"가 아니라 "역할과 책임의 분리"입니다.
이 게임은 LLM 없이 함수 4개로 그 구조를 체감합니다.

| 역할 | 책임 | 본 실습 대응 |
|---|---|---|
| **Planner** | 어떤 관점으로 코드를 볼지 점검 계획을 세운다 | Supervisor 의 분석 계획 수립 |
| **Hunter** | 계획에 따라 버그 후보를 찾는다 | SAST / Secret / Dependency Agent |
| **Reviewer** | 후보가 진짜 문제인지 검증한다(오탐 제거) | Threat / 검증 게이트 |
| **Reporter** | 결과를 사람이 읽을 리포트로 정리한다 | Report Agent |

## 규칙
- 각 역할은 자기 책임만 수행한다(Hunter 는 보고서를 쓰지 않는다).
- Reviewer 가 기각한 후보는 최종 리포트에서 제외된다.
- 모든 단계는 결정적(deterministic)이며 외부 호출이 없다.

> 연결: 이 Planner/Hunter/Reviewer/Reporter 구조가
> Day 3 본 실습의 SAST/Secret/Dependency/Threat/Report Agent 오케스트레이션으로 확장됩니다.
