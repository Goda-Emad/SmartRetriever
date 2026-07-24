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

# ============================================================
# 🏠 الصفحة الرئيسية - محتوى ترحيبي
# ============================================================

def show_home():
    """عرض المحتوى الترحيبي في الصفحة الرئيسية"""
    
    # ✅ عرض القائمة الجانبية (مع الإحصائيات)
    page = render_sidebar(
        stats=st.session_state.stats,
        show_theme_toggle=True,
        show_stats=True,
        show_navigation=False  # إخفاء التنقل لأنه سيكون في الصفحة الرئيسية
    )
    
    # ✅ المحتوى الرئيسي
    st.title("🧠 مرحباً بك في SmartRetriever")
    st.markdown("---")
    
    # ✅ أعمدة المحتوى
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## 📋 نظام استرجاع ذكي للمستندات
        
        هذا التطبيق يساعدك في:
        - 🔍 **البحث في المستندات** (عقود، سياسات، تقارير الجودة، عروض الأسعار)
        - 💬 **المحادثة مع الذكاء الاصطناعي** للحصول على إجابات دقيقة
        - 📊 **تحليل البيانات** وعرض الإحصائيات والمخططات
        
        ### 🚀 كيف تبدأ؟
        1. انتقل إلى صفحة **💬 المحادثة** لطرح الأسئلة
        2. استخدم صفحة **📄 المستندات** لعرض الملفات
        3. افتح صفحة **📊 التحليلات** لرؤية الإحصائيات
        """)
        
        # ✅ زر الانتقال إلى المحادثة
        if st.button("💬 ابدأ المحادثة الآن", use_container_width=True, type="primary"):
            st.switch_page("pages/1_Chat.py")
    
    with col2:
        st.markdown("""
        ### 📊 نظرة سريعة
        """)
        
        # ✅ عرض الإحصائيات في بطاقات
        stats = st.session_state.stats
        
        st.metric("📄 المستندات", stats.get("documents", 0))
        st.metric("🏢 الموردين", stats.get("suppliers", 0))
        st.metric("📝 العقود", stats.get("contracts", 0))
        st.metric("⭐ جودة", f"{stats.get('quality', 0):.1f}%")
    
    st.markdown("---")
    
    # ✅ ميزات التطبيق
    st.markdown("""
    ## ✨ الميزات
    
    | الميزة | الوصف |
    |--------|-------|
    | 🔍 **بحث دلالي** | استرجاع المستندات الأكثر تشابهاً مع سؤالك |
    | 🧠 **ذكاء اصطناعي** | استخدام Groq API لتوليد إجابات دقيقة |
    | 📊 **تحليلات** | عرض إحصائيات ومخططات عن المستندات والموردين |
    | 🌙 **وضع ليلي** | تبديل بين الوضع الفاتح والداكن |
    """)
    
    # ✅ معلومات النظام
    with st.expander("⚙️ معلومات النظام", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**📁 مسار الفهرس:** `{settings.FAISS_INDEX_PATH}`")
            st.markdown(f"**📁 مسار المستندات:** `{settings.KNOWLEDGE_BASE_PATH}`")
        with col2:
            st.markdown(f"**🤖 نموذج LLM:** `{settings.GROQ_MODEL}`")
            st.markdown(f"**🧬 نموذج المتجهات:** `{settings.EMBEDDING_MODEL}`")

# ============================================================
# 🚀 تشغيل الصفحة
# ============================================================

if __name__ == "__main__":
    show_home()
else:
    # ✅ عند تشغيل التطبيق عبر Streamlit، استخدم show_home()
    show_home()
