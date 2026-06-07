# 3️⃣ security-agent-lab-day3

**Day 3 · 멀티에이전트 = 역할 분리** — 키 없이 버튼 클릭만으로 돌려보는 Streamlit 실습.

> 5일짜리 `security-agent-lab` 과정 중 **Day 3만** 떼어낸 독립 저장소입니다.
> (다른 Day는 `security-agent-lab-day1` … `day5`, 스캐닝 엔진 코어는 `security-scan-engine` 저장소)

## 무엇을 보여주나
- **Mini Lab** — Bug Hunt Game: Planner → Hunter → Reviewer → Reporter
- 모델을 여러 개 쓴 게 아니라 **역할/책임을 나눈 것**이 멀티에이전트의 핵심
- **보너스** — AI Reviewer: '리뷰어 역할'을 시스템 프롬프트로 부여 (키 없으면 fallback)

## 실행

```bash
pip install -r requirements.txt
streamlit run app.py
```

브라우저가 열리면 위 탭(개요 · 왜 만드나 · Day 3)을 눌러보세요. **AI 키·외부 API 호출 불필요**.

## 구성
- `app.py` / `dashboard_lib.py` — Day 3 Streamlit 대시보드
- `agents/` — 스캐닝 엔진 코어(규칙 기반, 키 불필요)
- `sample_app/`·`policies/` — 점검 대상과 정책
