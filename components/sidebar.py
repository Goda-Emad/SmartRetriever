import streamlit as st
from pathlib import Path

# ============================================================
# 🌐 قاموس اللغات (Translations Dictionary)
# ============================================================
TRANSLATIONS = {
    "ar": {
        "home": "الصفحة الرئيسية",
        "about": "عن الفريق",
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

        # نصوص صفحة "عن الفريق"
        "about_title": "👥 فريق SmartRetriever",
        "about_subtitle": "نظام استرجاع ذكي للمستندات القانونية والعقود",
        "stat_docs_label": "📂 مستندات",
        "stat_docs_delta": "✅ تم تحميلها",
        "stat_embed_label": "🔍 نموذج التضمين",
        "stat_embed_delta": "🌍 متعدد اللغات",
        "stat_llm_label": "🤖 نموذج المحادثة",
        "stat_llm_delta": "⚡ Groq Cloud",
        "about_project_title": "📖 عن المشروع",
        "about_project_p1": "هو نظام ذكي لاسترجاع المستندات القانونية وإدارة العقود. يستخدم تقنيات RAG (Retrieval-Augmented Generation) و ChromaDB لتوفير إجابات دقيقة على استفسارات المستخدمين بناءً على محتوى المستندات المخزنة.",
        "about_project_p2": "🚀 تم بناء المشروع باستخدام Streamlit مع واجهة سهلة الاستخدام، ويتكامل مع Groq API لتوليد إجابات سريعة وذكية.",
        "instructions_title": "📸 كيفية إضافة صور الفريق",
        "instructions_hint": "💡 المقاسات الموصى بها: 500 × 500 بكسل (مربع)",
        "about_footer": "👥 فريق SmartRetriever | © 2026 | جميع الحقوق محفوظة",
        "image_placeholder_hint": "💡 ضع الصورة هنا:",
    },
    "en": {
        "home": "Home",
        "about": "About Team",
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

        # About page strings
        "about_title": "👥 SmartRetriever Team",
        "about_subtitle": "An intelligent retrieval system for legal documents and contracts",
        "stat_docs_label": "📂 Documents",
        "stat_docs_delta": "✅ Loaded",
        "stat_embed_label": "🔍 Embedding Model",
        "stat_embed_delta": "🌍 Multilingual",
        "stat_llm_label": "🤖 Chat Model",
        "stat_llm_delta": "⚡ Groq Cloud",
        "about_project_title": "📖 About the Project",
        "about_project_p1": "is an intelligent system for retrieving legal documents and managing contracts. It uses Retrieval-Augmented Generation (RAG) and ChromaDB to provide accurate answers based on the content of stored documents.",
        "about_project_p2": "🚀 Built with Streamlit for a smooth user experience, and integrates with the Groq API for fast, smart responses.",
        "instructions_title": "📸 How to Add Team Photos",
        "instructions_hint": "💡 Recommended size: 500 × 500 px (square)",
        "about_footer": "👥 SmartRetriever Team | © 2026 | All rights reserved",
        "image_placeholder_hint": "💡 Place the image here:",
    }
}


# ============================================================
# 🚫 إخفاء قائمة التنقل التلقائية بتاعة Streamlit
# ============================================================
def hide_default_nav():
    """
    يخفي [data-testid="stSidebarNav"] التلقائي بتاع Streamlit.
    مركزية هنا في sidebar.py بدل ما كل صفحة تكررها لوحدها،
    عشان تتطبق بشكل مضمون وموحد على كل الصفحات من غير تكرار.
    """
    st.markdown("""
        <style>
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)


# ============================================================
# 🎨 تطبيق التنسيق الديناميكي للثيم (Dynamic Theme Injector)
# ============================================================
def apply_dynamic_theme():
    """تطبيق الثيم (فاتح/داكن) مع ضبط تباين الألوان لكافة العناصر والبطاقات"""
    if st.session_state.get("dark_mode", True):
        # 🌙 الوضع الداكن (Dark Mode)
        st.markdown("""
        <style>
            /* خلفية التطبيق والسايدبار */
            .stApp { background-color: #0B0F19 !important; color: #F8FAFC !important; }
            [data-testid="stSidebar"] { background-color: #111827 !important; border-right: 1px solid rgba(255, 255, 255, 0.08) !important; }
            [data-testid="stSidebar"] * { color: #CBD5E1 !important; }

            /* الهيدر والبانر الرئيسي (بما فيها هيدر صفحة الفريق) */
            .doc-header, .chat-header, .hero-banner, .about-header {
                background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%) !important;
                border: 1px solid rgba(99, 102, 241, 0.3) !important;
                color: #FFFFFF !important;
            }
            .doc-header h2, .doc-header p, .chat-header h2, .chat-header p,
            .hero-banner h1, .hero-banner p, .about-header h1, .about-header p {
                color: #FFFFFF !important;
            }
            .about-header p { color: #94A3B8 !important; }

            /* بطاقات الإحصائيات والكروت (بما فيها بطاقات صفحة الفريق) */
            .metric-card, .doc-card, div[data-testid="stMetric"],
            .member-card, .stat-card, .project-info, .instructions-box {
                background-color: #1E293B !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                border-radius: 12px !important;
                padding: 12px !important;
            }
            div[data-testid="stMetricValue"] { color: #38BDF8 !important; }
            div[data-testid="stMetricLabel"] { color: #94A3B8 !important; }

            /* عناصر بطاقة العضو تحديدًا */
            .member-name { color: #FFFFFF !important; }
            .member-role { color: #38BDF8 !important; }
            .member-bio { color: #94A3B8 !important; }
            .skill-badge {
                background: #0F172A !important;
                color: #CBD5E1 !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
            }
            .member-avatar-placeholder {
                background: #1E293B !important;
                border: 4px dashed #38BDF8 !important;
                color: #38BDF8 !important;
            }
            .stat-card .stat-number { color: #38BDF8 !important; }
            .stat-card .stat-label { color: #94A3B8 !important; }
            .stat-card .stat-delta { color: #34D399 !important; }
            .project-info h3, .instructions-box h4 { color: #FFFFFF !important; }
            .project-info p, .instructions-box p { color: #94A3B8 !important; }
            .instructions-box code { background: #0F172A !important; color: #38BDF8 !important; }

            /* المدخلات والقوائم المنسدلة */
            .stTextInput input, div[data-baseweb="select"] > div {
                background-color: #182232 !important;
                color: #FFFFFF !important;
                border-color: rgba(255, 255, 255, 0.1) !important;
            }

            /* الأزرار العامة */
            .stButton > button {
                background-color: #1E293B !important;
                color: #F8FAFC !important;
                border: 1px solid rgba(255, 255, 255, 0.15) !important;
            }
            .stButton > button:hover {
                border-color: #38BDF8 !important;
                color: #38BDF8 !important;
            }
        </style>
        """, unsafe_allow_html=True)
    else:
        # ☀️ الوضع الفاتح (Light Mode)
        st.markdown("""
        <style>
            /* خلفية التطبيق والسايدبار */
            .stApp { background-color: #F8FAFC !important; color: #0F172A !important; }
            [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid #E2E8F0 !important; }
            [data-testid="stSidebar"] * { color: #334155 !important; }

            /* الهيدر والبانر الرئيسي (بما فيها هيدر صفحة الفريق) */
            .doc-header, .chat-header, .hero-banner, .about-header {
                background: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%) !important;
                border: 1px solid #C7D2FE !important;
                color: #1E1B4B !important;
            }
            .doc-header h2, .chat-header h2, .hero-banner h1, .about-header h1 { color: #1E1B4B !important; }
            .doc-header p, .chat-header p, .hero-banner p, .about-header p { color: #3730A3 !important; }

            /* بطاقات الإحصائيات والكروت (بما فيها بطاقات صفحة الفريق) */
            .metric-card, .doc-card, div[data-testid="stMetric"],
            .member-card, .stat-card, .project-info, .instructions-box {
                background-color: #FFFFFF !important;
                border: 1px solid #E2E8F0 !important;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.03) !important;
                border-radius: 12px !important;
                padding: 12px !important;
            }
            div[data-testid="stMetricValue"] { color: #0284C7 !important; }
            div[data-testid="stMetricLabel"] { color: #64748B !important; }

            /* عناصر بطاقة العضو تحديدًا */
            .member-name { color: #1E1B4B !important; }
            .member-role { color: #0284C7 !important; }
            .member-bio { color: #475569 !important; }
            .skill-badge {
                background: #F1F5F9 !important;
                color: #334155 !important;
                border: 1px solid #E2E8F0 !important;
            }
            .member-avatar-placeholder {
                background: #F1F5F9 !important;
                border: 4px dashed #0284C7 !important;
                color: #0284C7 !important;
            }
            .stat-card .stat-number { color: #0284C7 !important; }
            .stat-card .stat-label { color: #64748B !important; }
            .stat-card .stat-delta { color: #059669 !important; }
            .project-info h3, .instructions-box h4 { color: #1E1B4B !important; }
            .project-info p, .instructions-box p { color: #475569 !important; }
            .instructions-box code { background: #F1F5F9 !important; color: #0284C7 !important; }

            /* المدخلات والقوائم المنسدلة */
            .stTextInput input, div[data-baseweb="select"] > div {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border-color: #CBD5E1 !important;
            }

            /* الأزرار العامة */
            .stButton > button {
                background-color: #FFFFFF !important;
                color: #1E293B !important;
                border: 1px solid #CBD5E1 !important;
            }
            .stButton > button:hover {
                background-color: #F1F5F9 !important;
                border-color: #0284C7 !important;
                color: #0284C7 !important;
            }

            /* العناوين والنصوص الإضافية */
            h1, h2, h3, h4, h5, h6, p, span, label, div {
                color: #0F172A;
            }
        </style>
        """, unsafe_allow_html=True)


# ============================================================
# 🖥️ المكون الرئيسي للسايدبار (Render Sidebar)
# ============================================================
def render_sidebar(stats=None, show_theme_toggle=True, show_stats=True, show_navigation=True):
    """
    عرض القائمة الجانبية الموحدة للتطبيق

    Returns:
        كود اللغة الحالي ("ar" أو "en") - ملحوظة: القيمة المرجعة
        هي كود اللغة، مش اسم الصفحة المختارة. الصفحات بتتنقل
        مباشرة عن طريق st.page_link مفيش داعي لأي منطق توجيه إضافي.
    """
    # 1. تهيئة حالة الجلسة للثيم واللغة
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    if "lang" not in st.session_state:
        st.session_state.lang = "ar"

    # 2. إخفاء الـ nav التلقائي (مركزيًا هنا، مش لازم تتكرر في كل صفحة)
    hide_default_nav()

    # 3. تطبيق الثيم الديناميكي حسب الاختيار الحالي
    apply_dynamic_theme()

    # 4. جلب النصوص المترجمة
    lang_code = st.session_state.lang
    T = TRANSLATIONS.get(lang_code, TRANSLATIONS["ar"])

    with st.sidebar:
        # 🏷️ الهوية واللوجو
        st.markdown(f"""
        <div style="text-align: center; padding: 10px 0 15px 0;">
            <h2 style="margin: 0; font-weight: 800; font-size: 1.4rem;">🧠 SmartRetriever</h2>
            <span style="font-size: 0.75rem; color: #94A3B8;">{T['brand_subtitle']}</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # 🔀 التنقل الفوري بين الصفحات
        if show_navigation:
            st.page_link("app.py", label=T["home"], icon="🏠")
            st.page_link("pages/1_Chat.py", label=T["chat"], icon="💬")
            st.page_link("pages/2_Documents.py", label=T["docs"], icon="📁")
            st.page_link("pages/3_Analytics.py", label=T["analytics"], icon="📊")
            st.page_link("pages/0_About.py", label=T["about"], icon="👥")
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
            <a href="https://github.com" target="_blank" style="color: #38BDF8; text-decoration: none;">GitHub</a> |
            <a href="https://linkedin.com" target="_blank" style="color: #38BDF8; text-decoration: none;">LinkedIn</a>
        </div>
        """, unsafe_allow_html=True)

    return st.session_state.lang
