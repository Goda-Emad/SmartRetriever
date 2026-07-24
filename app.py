# app.py
import streamlit as st
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from components.sidebar import render_sidebar
from components.chat_utils import render_info
from core.config import settings
from utils.logger import logger, setup_logging

st.set_page_config(
    page_title="SmartRetriever",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    css_file = Path(__file__).parent / "styles" / "custom.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        import uuid
        st.session_state.session_id = str(uuid.uuid4())
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    if "is_processing" not in st.session_state:
        st.session_state.is_processing = False
    if "stats" not in st.session_state:
        st.session_state.stats = {
            "documents": 17,
            "suppliers": 5,
            "contracts": 5,
            "quality": 90.2
        }

init_session_state()
setup_logging()
logger.info("🚀 Starting SmartRetriever application")

# الصفحة الرئيسية فقط - Streamlit يتحكم في الـ multipage تلقائياً
st.title("🧠 SmartRetriever")
st.caption("نظام استرجاع ذكي للمستندات")
st.markdown("---")
render_info("اختر صفحة من القائمة الجانبية للبدء")

st.markdown("---")
col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    st.caption(f"🧠 {settings.APP_NAME} v{settings.APP_VERSION}")
with col2:
    st.caption(f"📊 البيئة: {settings.ENVIRONMENT}")
with col3:
    st.caption("© 2026 SmartRetriever")
