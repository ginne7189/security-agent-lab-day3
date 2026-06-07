import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
import dashboard_lib as L

st.set_page_config(page_title="Day 3 · 멀티에이전트 = 역할 분리", page_icon="3️⃣", layout="wide")
st.title("3️⃣ Day 3 · 멀티에이전트 = 역할 분리")

tabs = st.tabs(["🏠 개요", "🤔 왜 만드나?", "Day 3"])
with tabs[0]:
    L.render_overview()
with tabs[1]:
    L.render_why()
with tabs[2]:
    L.render_day3()
