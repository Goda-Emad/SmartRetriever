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
# ============================================================
# بناء الفهرس تلقائياً لو مش موجود
# ============================================================

@st.cache_resource(show_spinner="⏳ جاري بناء فهرس المستندات...")
def build_index_if_needed():
    import asyncio
    from pathlib import Path
    
    index_path = settings.FAISS_INDEX_PATH / "index.faiss"
    if index_path.exists():
        logger.info("✅ FAISS index already exists")
        return True
    
    logger.info("🔨 Building FAISS index...")
    try:
        from scripts.build_index import build_index
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(build_index())
        return result
    except Exception as e:
        logger.error(f"❌ Index build failed: {e}")
        return False

build_index_if_needed()
