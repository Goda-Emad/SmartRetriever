import streamlit as st
from pathlib import Path

# ============================================================
# 🌐 قاموس اللغات (Translations Dictionary)
# ============================================================
TRANSLATIONS = {
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
        "quality_rate": "الجودة"
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
        "quality_rate": "Quality"
    }
}

# ============================================================
# 🎨 تطبيق التنسيق الديناميكي للثيم (Dynamic Theme Injector)
# ============================================================
def apply_dynamic_theme():
    """تطبيق الثيم (فاتح/داكن) مع ضبط تباين الألوان لكافة العناصر والبطاقات"""
    if st.session_state.get("dark_mode", False):
        # 🌙 الوضع الداكن (Dark Mode) - مع لمسات Barbie
        st.markdown("""
        <style>
            /* 🎨 Barbie Dark Mode */
            :root {
                --bg-primary: #2D1B2E;
                --bg-secondary: #1A0F1B;
                --primary: #E0218A;
                --primary-dark: #C2185B;
                --text-primary: #FCE4EC;
                --text-secondary: #F8BBD0;
            }
            
            /* خلفية التطبيق */
            .stApp { background-color: #2D1B2E !important; color: #FCE4EC !important; }
            
            /* خلفية السايدبار */
            [data-testid="stSidebar"] { 
                background-color: #1A0F1B !important; 
                border-right: 2px solid #E0218A !important; 
            }
            [data-testid="stSidebar"] * { color: #FCE4EC !important; }
            
            /* الهيدر والبانر الرئيسي */
            .doc-header, .chat-header, .hero-banner {
                background: linear-gradient(135deg, #2D1B2E 0%, #1A0F1B 100%) !important;
                border: 2px solid #E0218A !important;
                color: #FFFFFF !important;
            }
            .doc-header h2, .doc-header p, .chat-header h2, .chat-header p, .hero-banner h1, .hero-banner p { 
                color: #FFFFFF !important; 
            }

            /* بطاقات الإحصائيات والكروت */
            .metric-card, .doc-card, div[data-testid="stMetric"] {
                background-color: #2D1B2E !important;
                border: 2px solid #E0218A !important;
                border-radius: 12px !important;
                padding: 12px !important;
                box-shadow: 0 4px 15px rgba(224, 33, 138, 0.2);
            }
            div[data-testid="stMetricValue"] { color: #E0218A !important; }
            div[data-testid="stMetricLabel"] { color: #F8BBD0 !important; }

            /* المدخلات والقوائم المنسدلة */
            .stTextInput input, div[data-baseweb="select"] > div {
                background-color: #2D1B2E !important;
                color: #FCE4EC !important;
                border: 2px solid #E0218A !important;
                border-radius: 10px !important;
            }
            .stTextInput input:focus, div[data-baseweb="select"] > div:focus {
                border-color: #C2185B !important;
                box-shadow: 0 0 0 3px rgba(224, 33, 138, 0.3);
            }
            
            /* الأزرار العامة */
            .stButton > button {
                background: linear-gradient(135deg, #E0218A 0%, #C2185B 100%) !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: 12px !important;
                font-weight: 700 !important;
                box-shadow: 0 4px 15px rgba(224, 33, 138, 0.3);
            }
            .stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 30px rgba(224, 33, 138, 0.4);
            }
            
            /* العناوين والنصوص الإضافية */
            h1, h2, h3, h4, h5, h6, p, span, label, div {
                color: #FCE4EC;
            }
            
            /* روابط */
            a {
                color: #E0218A !important;
            }
            a:hover {
                color: #F8BBD0 !important;
            }
        </style>
        """, unsafe_allow_html=True)
    else:
        # ☀️ الوضع الفاتح (Light Mode - Barbie Colors)
        st.markdown("""
        <style>
            /* 🎨 Barbie Light Mode */
            :root {
                --bg-primary: #FCE4EC;
                --bg-secondary: #FFFFFF;
                --primary: #E0218A;
                --primary-dark: #C2185B;
                --text-primary: #4A0E2E;
                --text-secondary: #C2185B;
            }
            
            /* خلفية التطبيق */
            .stApp { background-color: #FCE4EC !important; color: #4A0E2E !important; }
            
            /* خلفية السايدبار */
            [data-testid="stSidebar"] { 
                background-color: #FFFFFF !important; 
                border-right: 2px solid #E0218A !important; 
            }
            [data-testid="stSidebar"] * { color: #4A0E2E !important; }

            /* الهيدر والبانر الرئيسي */
            .doc-header, .chat-header, .hero-banner {
                background: linear-gradient(135deg, #FCE4EC 0%, #E0218A 100%) !important;
                border: 2px solid #C2185B !important;
                color: #FFFFFF !important;
            }
            .doc-header h2, .chat-header h2, .hero-banner h1 { color: #FFFFFF !important; }
            .doc-header p, .chat-header p, .hero-banner p { color: #FFFFFF !important; }

            /* بطاقات الإحصائيات والكروت */
            .metric-card, .doc-card, div[data-testid="stMetric"] {
                background-color: #FFFFFF !important;
                border: 2px solid #E0218A !important;
                border-radius: 12px !important;
                padding: 12px !important;
                box-shadow: 0 4px 15px rgba(224, 33, 138, 0.1);
            }
            div[data-testid="stMetricValue"] { color: #E0218A !important; }
            div[data-testid="stMetricLabel"] { color: #4A0E2E !important; }

            /* المدخلات والقوائم المنسدلة */
            .stTextInput input, div[data-baseweb="select"] > div {
                background-color: #FFFFFF !important;
                color: #4A0E2E !important;
                border: 2px solid #E0218A !important;
                border-radius: 10px !important;
            }
            .stTextInput input:focus, div[data-baseweb="select"] > div:focus {
                border-color: #C2185B !important;
                box-shadow: 0 0 0 3px rgba(224, 33, 138, 0.2);
            }

            /* الأزرار العامة */
            .stButton > button {
                background: linear-gradient(135deg, #E0218A 0%, #C2185B 100%) !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: 12px !important;
                font-weight: 700 !important;
                box-shadow: 0 4px 15px rgba(224, 33, 138, 0.3);
            }
            .stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 30px rgba(224, 33, 138, 0.4);
            }

            /* العناوين والنصوص الإضافية */
            h1, h2, h3, h4, h5, h6, p, span, label, div {
                color: #4A0E2E;
            }
            
            /* روابط */
            a {
                color: #E0218A !important;
            }
            a:hover {
                color: #C2185B !important;
            }
        </style>
        """, unsafe_allow_html=True)

# ============================================================
# 🖥️ المكون الرئيسي للسايدبار (Render Sidebar)
# ============================================================
def render_sidebar(stats=None, show_theme_toggle=True, show_stats=True, show_navigation=True):
    """عرض القائمة الجانبية الموحدة للتطبيق"""
    
    # 1. تهيئة حالة الجلسة للثيم واللغة
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False  # ✅ وضع فاتح افتراضياً مع Barbie Colors
    if "lang" not in st.session_state:
        st.session_state.lang = "ar"

    # 2. تطبيق الثيم الديناميكي حسب الاختيار الحالي
    apply_dynamic_theme()
    
    # 3. جلب النصوص المترجمة
    lang_code = st.session_state.lang
    T = TRANSLATIONS.get(lang_code, TRANSLATIONS["ar"])

    with st.sidebar:
        # 🏷️ الهوية واللوجو
        st.markdown(f"""
        <div style="text-align: center; padding: 10px 0 15px 0;">
            <h2 style="margin: 0; font-weight: 800; font-size: 1.4rem; color: #E0218A;">🧠 SmartRetriever</h2>
            <span style="font-size: 0.75rem; color: #C2185B;">{T['brand_subtitle']}</span>
        </div>
        """, unsafe_allow_html=True)

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
                theme_btn_label = T["theme_light"] if st.session_state.dark_mode else T["theme_dark"]
                if st.button(theme_btn_label, key="toggle_theme_btn", use_container_width=True):
                    st.session_state.dark_mode = not st.session_state.dark_mode
                    st.rerun()

        with col_lang:
            if st.button(T["lang_btn"], key="toggle_lang_btn", use_container_width=True):
                st.session_state.lang = "en" if st.session_state.lang == "ar" else "ar"
                st.rerun()

        # 🔗 روابط التواصل والتحقوق السفليّة
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size: 0.75rem; text-align: center; opacity: 0.7;">
            📦 AutoData · 2024-2026<br>
            <a href="https://github.com" target="_blank" style="color: #E0218A; text-decoration: none;">GitHub</a> | 
            <a href="https://linkedin.com" target="_blank" style="color: #E0218A; text-decoration: none;">LinkedIn</a>
        </div>
        """, unsafe_allow_html=True)

    return st.session_state.lang
