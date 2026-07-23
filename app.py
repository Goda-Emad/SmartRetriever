# app/app.py
"""
🚀 تطبيق ProcureMind-AI - نقطة الدخول الرئيسية

هذا هو الملف الذي سيتم تشغيله عند بدء التطبيق
"""

import streamlit as st
import sys
import os
from pathlib import Path

# إضافة المجلد الحالي إلى المسار
sys.path.append(str(Path(__file__).parent))

# استيراد المكونات
from components.sidebar import render_sidebar
from components.chat_utils import render_info
from core.config import settings
from utils.logger import logger, setup_logging


# ============================================================
# 1. إعدادات الصفحة
# ============================================================

st.set_page_config(
    page_title="ProcureMind-AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# 2. تحميل التنسيقات
# ============================================================

def load_css():
    """تحميل ملف التنسيقات المخصصة"""
    css_file = Path(__file__).parent / "styles" / "custom.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()


# ============================================================
# 3. تهيئة الجلسة
# ============================================================

def init_session_state():
    """تهيئة جميع متغيرات الجلسة"""
    
    # رسائل المحادثة
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # معرف الجلسة
    if "session_id" not in st.session_state:
        import uuid
        st.session_state.session_id = str(uuid.uuid4())
    
    # الوضع الداكن
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    
    # حالة المعالجة
    if "is_processing" not in st.session_state:
        st.session_state.is_processing = False
    
    # إحصائيات (للعرض)
    if "stats" not in st.session_state:
        st.session_state.stats = {
            "documents": 17,
            "suppliers": 5,
            "contracts": 5,
            "quality": 90.2
        }


init_session_state()


# ============================================================
# 4. إعداد التسجيل
# ============================================================

setup_logging()
logger.info("🚀 Starting ProcureMind-AI application")


# ============================================================
# 5. عرض القائمة الجانبية
# ============================================================

page = render_sidebar(
    stats=st.session_state.stats,
    show_theme_toggle=True,
    show_stats=True,
    show_navigation=True
)


# ============================================================
# 6. التنقل بين الصفحات
# ============================================================

try:
    if page == "💬 المحادثة":
        from app.pages.chat import show as show_chat
        show_chat()
    
    elif page == "📄 المستندات":
        from app.pages.documents import show as show_documents
        show_documents()
    
    elif page == "📊 التحليلات":
        from app.pages.analytics import show as show_analytics
        show_analytics()
    
    else:
        # صفحة افتراضية (المحادثة)
        from app.pages.chat import show as show_chat
        show_chat()

except Exception as e:
    logger.error(f"❌ Error loading page: {str(e)}")
    st.error(f"❌ حدث خطأ في تحميل الصفحة: {str(e)}")
    
    # عرض معلومات إضافية في وضع التطوير
    if settings.DEBUG:
        st.code(f"Error: {str(e)}", language="python")
        st.code(f"Page: {page}", language="python")


# ============================================================
# 7. معلومات التطبيق في التذييل
# ============================================================

st.markdown("---")
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    st.caption(f"🧠 {settings.APP_NAME} v{settings.APP_VERSION}")

with col2:
    st.caption(f"📊 البيئة: {settings.ENVIRONMENT}")

with col3:
    st.caption("© 2026 ProcureMind-AI")


# ============================================================
# 8. تشغيل التطبيق (للاختبار المحلي)
# ============================================================

if __name__ == "__main__":
    # هذا الكود يعمل فقط عند تشغيل الملف مباشرة
    # Streamlit يدير التشغيل بشكل مختلف
    
    logger.info("✅ Application is running")
    logger.info(f"🔗 Open: http://localhost:8501")
