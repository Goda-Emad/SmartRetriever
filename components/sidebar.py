import streamlit as st
from typing import Dict, Any, Optional

# ============================================================
# 🌐 قاموس اللغات (Translations Dictionary)
# ============================================================
TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "ar": {
        "home": "الصفحة الرئيسية",
        "about": "👥 عن الفريق",
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
        "quality_rate": "الجودة",
    },
    "en": {
        "home": "Home",
        "about": "👥 About Team",
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
        "quality_rate": "Quality",
    }
}


# ============================================================
# 🎨 تطبيق التنسيق الديناميكي للثيم (Dynamic Theme Injector)
# ============================================================
def apply_dynamic_theme() -> None:
    """تطبيق الثيم (فاتح/داكن) واتجاه النص عبر متغيرات CSS موحدة."""
    is_dark = st.session_state.get("dark_mode", True)
    is_rtl = st.session_state.get("lang", "ar") == "ar"

    # تحديد اتجاه الصفحة والمتغيرات اللونية
    direction = "rtl" if is_rtl else "ltr"
    
    if is_dark:
        bg_app = "#0B0F19"
        text_main = "#F8FAFC"
        bg_sidebar = "#111827"
        text_sidebar = "#CBD5E1"
        header_bg = "linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%)"
        header_border = "rgba(99, 102, 241, 0.3)"
        card_bg = "#1E293B"
        card_border = "rgba(255, 255, 255, 0.08)"
        input_bg = "#182232"
        input_text = "#FFFFFF"
        accent_color = "#38BDF8"
    else:
        bg_app = "#F8FAFC"
        text_main = "#0F172A"
        bg_sidebar = "#FFFFFF"
        text_sidebar = "#334155"
        header_bg = "linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%)"
        header_border = "#C7D2FE"
        card_bg = "#FFFFFF"
        card_border = "#E2E8F0"
        input_bg = "#FFFFFF"
        input_text = "#0F172A"
        accent_color = "#0284C7"

    css_code = f"""
    <style>
        /* 🌐 ضبط الاتجاه الأساسي للتطبيق */
        .stApp {{
            direction: {direction};
            background-color: {bg_app} !important;
            color: {text_main} !important;
        }}

        /* 📱 السايدبار */
        [data-testid="stSidebar"] {{
            background-color: {bg_sidebar} !important;
            border-inline-end: 1px solid {card_border} !important;
        }}
        [data-testid="stSidebar"] * {{
            color: {text_sidebar} !important;
        }}

        /* 🏛️ الهيدر والبانر الرئيسي */
        .doc-header, .chat-header, .hero-banner {{
            background: {header_bg} !important;
            border: 1px solid {header_border} !important;
            border-radius: 12px;
            padding: 1rem;
        }}

        /* 📊 البطاقات والمقاييس */
        .metric-card, .doc-card, div[data-testid="stMetric"] {{
            background-color: {card_bg} !important;
            border: 1px solid {card_border} !important;
            border-radius: 12px !important;
            padding: 12px !important;
        }}
        div[data-testid="stMetricValue"] {{ color: {accent_color} !important; }}

        /* ✏️ مدخلات النصوص والقوائم */
        .stTextInput input, div[data-baseweb="select"] > div {{
            background-color: {input_bg} !important;
            color: {input_text} !important;
            border-color: {card_border} !important;
        }}

        /* 🔘 الأزرار العامة */
        .stButton > button {{
            background-color: {card_bg} !important;
            color: {text_main} !important;
            border: 1px solid {card_border} !important;
            border-radius: 8px;
            transition: all 0.2s ease-in-out;
        }}
        .stButton > button:hover {{
            border-color: {accent_color} !important;
            color: {accent_color} !important;
        }}
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)


# ============================================================
# 🖥️ المكون الرئيسي للسايدبار (Render Sidebar)
# ============================================================
def render_sidebar(
    stats: Optional[Dict[str, Any]] = None,
    show_theme_toggle: bool = True,
    show_stats: bool = True,
    show_navigation: bool = True,
) -> str:
    """عرض القائمة الجانبية الموحدة للتطبيق وترجيع رمز اللغة الحالية."""
    
    # 1. تهيئة حالة الجلسة للثيم واللغة
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    if "lang" not in st.session_state:
        st.session_state.lang = "ar"

    # 2. تطبيق الثيم والاتجاه الديناميكي
    apply_dynamic_theme()
    
    # 3. جلب النصوص المترجمة
    lang_code = st.session_state.lang
    T = TRANSLATIONS.get(lang_code, TRANSLATIONS["ar"])

    with st.sidebar:
        # 🏷️ الهوية واللوجو
        st.markdown(
            f"""
            <div style="text-align: center; padding: 10px 0 15px 0;">
                <h2 style="margin: 0; font-weight: 800; font-size: 1.4rem;">🧠 SmartRetriever</h2>
                <span style="font-size: 0.75rem; opacity: 0.8;">{T['brand_subtitle']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # 🔀 التنقل الفوري بين الصفحات
        if show_navigation:
            st.page_link("app.py", label=T["home"], icon="🏠")
            st.page_link("pages/0_About.py", label=T["about"], icon="👥")
            st.page_link("pages/1_Chat.py", label=T["chat"], icon="💬")
            st.page_link("pages/2_Documents.py", label=T["docs"], icon="📁")
            st.page_link("pages/3_Analytics.py", label=T["analytics"], icon="📊")
            st.markdown("---")

        # 📊 عرض الإحصائيات (إن وجدت)
        if show_stats and stats:
            st.markdown(f"##### {T['stats_title']}")
            st.caption(f"📄 {T['docs_count']}: {stats.get('documents', 0)}")
            st.caption(f"🏢 {T['suppliers_count']}: {stats.get('suppliers', 0)}")
            st.caption(f"📝 {T['contracts_count']}: {stats.get('contracts', 0)}")
            st.caption(f"⭐ {T['quality_rate']}: {stats.get('quality', 0)}%")
            st.markdown("---")

        # ⚙️ أزرار التحكم بالثيم واللغة
        col_theme, col_lang = st.columns(2)

        with col_theme:
            if show_theme_toggle:
                theme_btn_label = (
                    T["theme_light"]
                    if st.session_state.dark_mode
                    else T["theme_dark"]
                )
                if st.button(
                    theme_btn_label, key="toggle_theme_btn", use_container_width=True
                ):
                    st.session_state.dark_mode = not st.session_state.dark_mode
                    st.rerun()

        with col_lang:
            if st.button(
                T["lang_btn"], key="toggle_lang_btn", use_container_width=True
            ):
                st.session_state.lang = (
                    "en" if st.session_state.lang == "ar" else "ar"
                )
                st.rerun()

        # 🔗 روابط التواصل والتحقوق السفليّة
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="font-size: 0.75rem; text-align: center; opacity: 0.7;">
                📦 AutoData · 2024-2026<br>
                <a href="https://github.com" target="_blank" style="color: inherit; text-decoration: underline;">GitHub</a> | 
                <a href="https://linkedin.com" target="_blank" style="color: inherit; text-decoration: underline;">LinkedIn</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    return st.session_state.lang
