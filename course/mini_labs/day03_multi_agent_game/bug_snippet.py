"""
Bug Snippet (course/mini_labs/day03_multi_agent_game/bug_snippet.py) — Day 3 Mini Lab

이 파일에는 일부러 쉬운 버그 3개가 들어 있습니다.
Bug Hunt Game 의 Hunter 가 이 파일을 텍스트로 읽어 버그 후보를 찾습니다.
(실제로 import 해서 실행하지 않으므로, 버그가 있어도 게임은 안전하게 돌아갑니다.)

심어진 버그:
1) get_last(items): off-by-one → items[len(items)] 는 IndexError
2) average(nums): divide-by-zero → 빈 리스트면 ZeroDivisionError
3) first_admin(users): 빈 리스트 처리 누락 → 결과가 없을 때 None 반환 보장 안 됨
"""


def get_last(items):
    # BUG: off-by-one. 마지막 인덱스는 len(items) - 1 이어야 한다.
    return items[len(items)]


def average(nums):
    # BUG: divide-by-zero. nums 가 비어 있으면 0 으로 나눈다.
    total = 0
    for n in nums:
        total += n
    return total / len(nums)


def first_admin(users):
    # BUG: 빈 리스트/admin 없음 처리 누락. 루프가 끝나면 명시적 반환이 없다.
    for u in users:
        if u.get("role") == "admin":
            return u
    # 여기서 명시적으로 None 을 반환해야 의도가 분명하다.
