#!/usr/bin/env python3
"""
Bug Hunt Game (course/mini_labs/day03_multi_agent_game/run_bug_hunt_game.py) — Day 3 Mini Lab

목표: 멀티에이전트가 "모델을 여러 개 쓰는 것"이 아니라
      "역할(Planner/Hunter/Reviewer/Reporter)을 나누는 것"임을 체감한다.

- 외부 API 호출 없음 / LLM 호출 없음 / Python 표준 라이브러리만 사용
- 각 역할은 실제 Agent 가 아니라 함수로 구현한다
- bug_snippet.py 를 텍스트로 읽어 일부러 심어 둔 버그 후보를 찾는다

실행:  python course/mini_labs/day03_multi_agent_game/run_bug_hunt_game.py
산출물: reports/bug_hunt_report.md
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SNIPPET = os.path.join(HERE, "bug_snippet.py")
OUT = "reports/bug_hunt_report.md"


# ── Planner: 어떤 관점으로 볼지 계획 ──
def planner():
    return [
        {"id": "off-by-one", "관점": "리스트 인덱스가 범위를 벗어나는가?"},
        {"id": "divide-by-zero", "관점": "0 으로 나눌 가능성이 있는가?"},
        {"id": "empty-input", "관점": "빈 입력/누락된 반환을 처리하는가?"},
    ]


# ── Hunter: 계획에 따라 버그 후보를 텍스트 패턴으로 탐색 ──
_PATTERNS = {
    "off-by-one": re.compile(r"\[\s*len\([^)]*\)\s*\]"),         # items[len(items)]
    "divide-by-zero": re.compile(r"/\s*len\([^)]*\)"),           # x / len(nums)
    "empty-input": re.compile(r"for\s+\w+\s+in\s+\w+:"),         # 루프 후 명시적 반환 점검 대상
}


def hunter(plan, source_lines):
    candidates = []
    for step in plan:
        rx = _PATTERNS[step["id"]]
        for i, line in enumerate(source_lines, start=1):
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            if rx.search(line):
                candidates.append({
                    "id": step["id"], "line": i,
                    "code": stripped, "관점": step["관점"],
                })
    return candidates


# ── Reviewer: 후보가 진짜 문제인지 검증(간단 규칙) ──
def reviewer(candidates, source_text, source_lines):
    confirmed, rejected = [], []
    for c in candidates:
        verdict, reason = _judge(c, source_text, source_lines)
        record = {**c, "판정": verdict, "사유": reason}
        (confirmed if verdict == "진짜 버그" else rejected).append(record)
    return confirmed, rejected


def _loop_has_inner_return(source_lines, for_line):
    """for 루프 본문(더 깊은 들여쓰기) 안에 조건부 return 이 있는지 검사."""
    base_indent = len(source_lines[for_line - 1]) - len(source_lines[for_line - 1].lstrip())
    for line in source_lines[for_line:]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= base_indent:      # 루프 블록을 벗어남
            break
        if line.strip().startswith("return"):
            return True
    return False


def _judge(c, source_text, source_lines):
    if c["id"] == "off-by-one":
        # len(x) 가 인덱스로 쓰이면 항상 범위 초과
        return "진짜 버그", "len() 결과를 인덱스로 사용 → IndexError 발생"
    if c["id"] == "divide-by-zero":
        # 나누기 전에 빈 리스트 가드가 없으면 위험
        if "if not nums" in source_text or "len(nums) == 0" in source_text:
            return "오탐", "빈 리스트 가드가 존재함"
        return "진짜 버그", "분모 검사 없이 len() 으로 나눔 → ZeroDivisionError 가능"
    if c["id"] == "empty-input":
        # 루프 안에 조건부 return 이 있어야 '매칭 실패 시 반환 누락' 버그가 성립한다.
        # 단순 누적 루프(average 의 for)는 빈 입력 버그가 아니므로 Reviewer 가 기각한다.
        if not _loop_has_inner_return(source_lines, c["line"]):
            return "오탐", "루프 내부 조건부 return 이 없음 → 빈 입력 반환 누락 아님(단순 누적)"
        if "return None" in source_text:
            return "오탐", "명시적 return None 존재"
        return "진짜 버그", "루프가 매칭 없이 끝나면 반환값이 암묵적 None(의도 불명확)"
    return "오탐", "알 수 없는 패턴"


# ── Reporter: 결과를 리포트로 정리 ──
def reporter(plan, candidates, confirmed, rejected):
    lines = ["# Bug Hunt Game 리포트 (Day 3 Mini Lab)", ""]
    lines.append("> 역할 분리: Planner → Hunter → Reviewer → Reporter")
    lines.append("")

    lines.append("## 1) Planner — 점검 계획")
    for p in plan:
        lines.append(f"- [{p['id']}] {p['관점']}")
    lines.append("")

    lines.append(f"## 2) Hunter — 버그 후보 {len(candidates)}건")
    for c in candidates:
        lines.append(f"- L{c['line']} `{c['code']}`  ([{c['id']}])")
    lines.append("")

    lines.append(f"## 3) Reviewer — 확정 {len(confirmed)}건 / 기각 {len(rejected)}건")
    for c in confirmed:
        lines.append(f"- ✅ L{c['line']} [{c['id']}] {c['사유']}")
    for c in rejected:
        lines.append(f"- ❌ L{c['line']} [{c['id']}] (기각) {c['사유']}")
    lines.append("")

    lines.append("## 4) Reporter — 최종 결론")
    lines.append(f"- 확정된 진짜 버그: **{len(confirmed)}건**")
    lines.append("- 권장: off-by-one, divide-by-zero, 빈 입력 처리에 가드 추가")
    lines.append("")
    lines.append("> 연결: 이 4역할 구조가 Day 3 본 실습의")
    lines.append("> SAST/Secret/Dependency/Threat/Report Agent 오케스트레이션으로 확장됩니다.")
    lines.append("")
    return "\n".join(lines)


def main():
    with open(SNIPPET, encoding="utf-8") as f:
        source_text = f.read()
    source_lines = source_text.splitlines()

    plan = planner()
    candidates = hunter(plan, source_lines)
    confirmed, rejected = reviewer(candidates, source_text, source_lines)
    report = reporter(plan, candidates, confirmed, rejected)

    os.makedirs("reports", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"[BugHunt] Planner {len(plan)} 관점 → Hunter {len(candidates)} 후보 "
          f"→ Reviewer 확정 {len(confirmed)} / 기각 {len(rejected)}")
    print(f"[BugHunt] 산출물 저장 → {OUT}")


if __name__ == "__main__":
    main()
