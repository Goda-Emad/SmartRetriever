import streamlit as st
from pathlib import Path

# ============================================================
# 🌐 قاموس اللغات (قاموس النصوص المترجمة)
# ============================================================
TRANSLATIONS = {
    "ar": {
        "home": "الصفحة الرئيسية",
        "chat": "المساعد الذكي",
        "docs": "المستندات",
        "analytics": "التحليلات",
        "theme_light": "☀️ وضع فاتح",
        "theme_dark": "🌙 وضع داكن",
        "lang_btn": "🌐 English",
        "brand_subtitle": "منصة التحليل والذكاء الاصطناعي",
        "stats_title": "📊 الإحصائيات",
        "docs_count": "المستندات",
        "suppliers_count": "الموردين",
        "contracts_count": "العقود",
        "quality_rate": "الجودة"
    },
    "en": {
        "home": "Home",
        "chat": "AI Assistant",
        "docs": "Documents",
        "analytics": "Analytics",
        "theme_light": "☀️ Light Mode",
        "theme_dark": "🌙 Dark Mode",
        "lang_btn": "🌐 العربية",
        "brand_subtitle": "AI Analytics Platform",
        "stats_title": "📊 Statistics",
        "docs_count": "Documents",
        "suppliers_count": "Suppliers",
        "contracts_count": "Contracts",
        "quality_rate": "Quality"
    }
}

# ============================================================
# 🎨 حقن CSS للوضع الفاتح والداكن تلقائياً
# ============================================================
def apply_dynamic_theme():
    """تطبيق الثيم المطلوب (فاتح/داكن) فورياً عبر CSS"""
    if st.session_state.get("dark_mode", True):
        # 🌙 CSS الوضع الداكن
        st.markdown("""
        <style>
            .stApp { background-color: #0B0F19 !important; color: #E2E8F0 !important; }
            [data-testid="stSidebar"] { background-color: #111827 !important; }
            .stChatMessage, .hero-banner, .chat-header {
                background-color: #1E293B !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                color: #FFFFFF !important;
            }
        </style>
        """, unsafe_allow_html=True)
    else:
        # ☀️ CSS الوضع الفاتح
        st.markdown("""
        <style>
            .stApp { background-color: #F8FAFC !important; color: #0F172A !important; }
            [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid #E2E8F0 !important; }
            .stChatMessage, .hero-banner, .chat-header, .metric-card {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border: 1px solid #CBD5E1 !important;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
            }
            h1, h2, h3, h4, h5, h6, p, span, label, div { color: #0F172A !important; }
            .stButton > button { background-color: #F1F5F9 !important; color: #0F172A !important; border: 1px solid #CBD5E1 !important; }
        </style>
        """, unsafe_allow_html=True)

# ============================================================
# 🖥️ مكون القائمة الجانبية الرئيسي
# ============================================================
def render_sidebar(stats=None, show_theme_toggle=True, show_stats=True, show_navigation=True):
    """عرض السايدبار الموحد مع التوجيه واللغات والثيمات"""
    
    # 1. تهيئة متغيرة الجلسة للثيم واللغة
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    if "lang" not in st.session_state:
        st.session_state.lang = "ar"

    # تطبيق الثيم الحالي
    apply_dynamic_theme()
    
    # جلب النصوص المترجمة للغة الحالية
    lang_code = st.session_state.lang
    T = TRANSLATIONS.get(lang_code, TRANSLATIONS["ar"])

    with st.sidebar:
        # Branding / الهوية
        st.markdown(f"""
        <div style="text-align: center; padding: 10px 0 15px 0;">
            <h2 style="margin: 0; font-weight: 800; font-size: 1.4rem;">🧠 SmartRetriever</h2>
            <span style="font-size: 0.75rem; color: #94A3B8;">{T['brand_subtitle']}</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # 2. 🔀 التنقل الفعلي السلس بين الصفحات (بدون مشاكل التعليق)
        if show_navigation:
            st.page_link("app.py", label=T["home"], icon="🏠")
            st.page_link("pages/1_Chat.py", label=T["chat"], icon="💬")
            st.page_link("pages/2_Documents.py", label=T["docs"], icon="📁")
            st.page_link("pages/3_Analytics.py", label=T["analytics"], icon="📊")
            st.markdown("---")

        # 3. 📊 عرض الإحصائيات (إن وجدت)
        if show_stats and stats:
            st.markdown(f"##### {T['stats_title']}")
            st.caption(f"📄 {T['docs_count']}: {stats.get('documents', 0)}")
            st.caption(f"🏢 {T['suppliers_count']}: {stats.get('suppliers', 0)}")
            st.caption(f"📝 {T['contracts_count']}: {stats.get('contracts', 0)}")
            st.caption(f"⭐ {T['quality_rate']}: {stats.get('quality', 0)}%")
            st.markdown("---")

        # 4. ⚙️ أزرار التحكم بالثيم واللغة
        col_theme, col_lang = st.columns(2)

        with col_theme:
            if show_theme_toggle:
                theme_btn_label = T["theme_light"] if st.session_state.dark_mode else T["theme_dark"]
                if st.button(theme_btn_label, key="toggle_theme_btn", use_container_width=True):
                    st.session_state.dark_mode = not st.session_state.dark_mode
                    st.rerun()

        with col_lang:
            if st.button(T["lang_btn"], key="toggle_lang_btn", use_container_width=True):
                st.session_state.lang = "en" if st.session_state.lang == "ar" else "ar"
                st.rerun()

        # روابط التواصل الاجتماعية السفليّة
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size: 0.75rem; color: #64748B; text-align: center;">
            📦 AutoData · 2024-2026<br>
            <a href="https://github.com" target="_blank" style="color: #38BDF8; text-decoration: none;">GitHub</a> | 
            <a href="https://linkedin.com" target="_blank" style="color: #38BDF8; text-decoration: none;">LinkedIn</a>
        </div>
        """, unsafe_allow_html=True)

    return st.session_state.lang
