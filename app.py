import streamlit as st
import sys
import os
import uuid
from pathlib import Path

# إدراج المسار الرئيسي للترويد
sys.path.append(str(Path(__file__).parent))

from components.sidebar import render_sidebar
from core.config import settings
from utils.logger import logger

# ============================================================
# ⚙️ إعدادات الصفحة الرئيسية
# ============================================================
st.set_page_config(
    page_title="SmartRetriever Auto | AI Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# 🎨 تحسين التنسيقات وإخفاء قائمة Streamlit الافتراضية
# ============================================================
def load_css():
    """تحميل التنسيقات مع إخفاء قائمة التنقل الافتراضية لـ Streamlit"""
    st.markdown("""
        <style>
        /* 🚫 إخفاء قائمة التنقل الافتراضية التي يولدها Streamlit للملفات داخل pages/ */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        
        /* تحسين مظهر البطاقات الإحصائية الرئيسية */
        .metric-card {
            background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 1.2rem;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }
        .metric-card:hover {
            border-color: #38BDF8;
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(56, 189, 248, 0.15);
        }
        .metric-value {
            font-size: 1.8rem;
            font-weight: 800;
            color: #38BDF8;
            margin-top: 0.2rem;
        }
        .metric-label {
            font-size: 0.85rem;
            color: #94A3B8;
            font-weight: 600;
        }
        
        /* Hero Section Styling */
        .hero-banner {
            background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%);
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        }
        </style>
    """, unsafe_allow_html=True)

    css_file = Path(__file__).parent / "styles" / "custom.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ============================================================
# 🔄 تهيئة حالة الجلسة (Session State)
# ============================================================
def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    if "is_processing" not in st.session_state:
        st.session_state.is_processing = False
    if "current_page" not in st.session_state:
        st.session_state.current_page = "HOME"
    if "stats" not in st.session_state:
        st.session_state.stats = {
            "documents": 17,
            "suppliers": 5,
            "contracts": 5,
            "quality": 90.2
        }

init_session_state()

# ============================================================
# ⚡ بناء الفهرس الذكي تلقائياً
# ============================================================
@st.cache_resource(show_spinner="⏳ جاري فحص وبناء فهرس المستندات...")
def build_index_if_needed():
    import asyncio
    
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
# 🔀 التعامل مع التنقل التفاعلي بين الصفحات
# ============================================================
def handle_routing(selected_page: str):
    """ربط خيارات السايدبار بملفات الصفحات الحقيقية في التطبيق"""
    page_routes = {
        "المساعد الذكي": "pages/1_Chat.py",
        "المستندات": "pages/2_Documents.py",
        "التحليلات": "pages/3_Analytics.py",
    }
    
    if selected_page in page_routes:
        target_file = page_routes[selected_page]
        if Path(target_file).exists():
            st.switch_page(target_file)

# ============================================================
# 🏠 الصفحة الرئيسية - Modern SaaS Dashboard UI
# ============================================================
def show_home():
    """عرض الواجهة الرئيسية العصرية للتطبيق"""
    
    # ✅ عرض السايدبار وحفظ الصفحة المختارة
    current_selected = render_sidebar(
        stats=st.session_state.stats,
        show_theme_toggle=True,
        show_stats=False,
        show_navigation=True
    )
    
    # تنفيذ التوجيه إذا تم الضغط على صفحة أخرى غير الصفحة الرئيسية
    if current_selected != "HOME":
        handle_routing(current_selected)

    # 1. Hero Banner ترحيبي
    st.markdown("""
    <div class="hero-banner">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
            <span style="background: rgba(56, 189, 248, 0.15); color: #38BDF8; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.3);">
                ⚡ AI RETRIEVAL SYSTEM V2.5
            </span>
        </div>
        <h1 style="color: #FFFFFF; font-weight: 800; font-size: 2.2rem; margin: 0 0 10px 0;">
            مرحباً بك في منصة SmartRetriever Auto 🧠
        </h1>
        <p style="color: #94A3B8; font-size: 1rem; line-height: 1.6; margin: 0;">
            مساعدك الذكي لاسترجاع وتصنيف البيانات، تحليل العقود والسياسات، والإجابة الدقيقة بناءً على قاعدة معرفتك الخاصة.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 2. بطاقات الإحصائيات (Metrics Bar)
    stats = st.session_state.stats
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📄 إجمالي المستندات</div>
            <div class="metric-value">{stats.get('documents', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">🏢 الموردين المعتمدين</div>
            <div class="metric-value">{stats.get('suppliers', 0)}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📝 العقود النشطة</div>
            <div class="metric-value">{stats.get('contracts', 0)}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">⭐ دقة الإجابات</div>
            <div class="metric-value">{stats.get('quality', 0):.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. قسم خيارات الوصول السريع والتوجيه
    col_main, col_side = st.columns([2, 1])

    with col_main:
        st.markdown("""
        ### 🚀 الدليل السريع للبدء
        """)
        
        st.markdown("""
        * **💬 المساعد الذكي:** يمكنك البدء فوراً بطرح الأسئلة حول عقودك وسياسات الشركة للحصول على إجابات معززة بالمصادر.
        * **📁 أرشيف المستندات:** استعراض ومعاينة كافة الملفات والمستندات الموجودة بالفهرس.
        * **📊 لوحة التحليلات:** الاطلاع على تحليلات دقيقة وإحصائيات الموردين والعقود بشكل بياني.
        """)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("💬 الانتقال للمساعد الذكي الآن", use_container_width=True, type="primary"):
            handle_routing("المساعد الذكي")

    with col_side:
        st.markdown("### ✨ ميزات المنصة")
        
        st.markdown("""
        - 🔍 **البحث الدلالي (Semantic Search)**
        - ⚡ **معالجة فائقة السرعة مع Groq API**
        - 🔒 **حماية وأمان كامل للبيانات**
        - 🌙 **دعم كلي للوضع الليلي المتقدم**
        """)

    st.markdown("---")

    # 4. تفاصيل ومعلومات النظام (System Status)
    with st.expander("⚙️ معلومات وبيئة التشغيل", expanded=False):
        ec1, ec2 = st.columns(2)
        with ec1:
            st.code(f"مسار الفهرس: {settings.FAISS_INDEX_PATH}", language="text")
            st.code(f"قاعدة المعرفة: {settings.KNOWLEDGE_BASE_PATH}", language="text")
        with ec2:
            st.code(f"نموذج الذكاء: {settings.GROQ_MODEL}", language="text")
            st.code(f"نموذج المتجهات: {settings.EMBEDDING_MODEL}", language="text")


# ============================================================
# 🚀 تشغيل التطبيق
# ============================================================
if __name__ == "__main__":
    show_home()
