"""
📌 القائمة الجانبية - Modern SaaS Sidebar Component
"""

import streamlit as st
from typing import Optional, Dict, Any

# محاولة استيراد option_menu إذا كانت مثبتة في المشروع
try:
    from streamlit_option_menu import option_menu
    HAS_OPTION_MENU = True
except ImportError:
    HAS_OPTION_MENU = False

# ============================================================
# ⚙️ أسماء الصفحات المعتمدة
# ============================================================
PAGES_MAP = {
    "HOME": "🏠",
    "المساعد الذكي": "💬",
    "المستندات": "📁",
    "التحليلات": "📊",
}

DEFAULT_PAGE = "HOME"


# ============================================================
# 🎨 حقن CSS لتحسين المظهر
# ============================================================
def _inject_custom_css():
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            background-color: #0B1120 !important;
        }
        
        /* تنسيق أزرار Streamlit البديلة */
        [data-testid="stSidebar"] div.stButton > button {
            width: 100% !important;
            background: #1E293B !important;
            color: #F1F5F9 !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 10px !important;
            padding: 0.6rem 1rem !important;
            font-size: 0.95rem !important;
            font-weight: 700 !important;
            transition: all 0.2s ease-in-out !important;
            margin-bottom: 4px !important;
        }
        
        [data-testid="stSidebar"] div.stButton > button:hover {
            border-color: #38BDF8 !important;
            color: #38BDF8 !important;
            transform: translateY(-1px) !important;
        }

        [data-testid="stSidebar"] hr {
            border-color: rgba(255, 255, 255, 0.08) !important;
            margin: 0.8rem 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)


# ============================================================
# 1. القائمة الجانبية الرئيسية
# ============================================================

def render_sidebar(
    stats: Optional[Dict[str, Any]] = None,
    show_theme_toggle: bool = True,
    show_stats: bool = False,
    show_navigation: bool = True
) -> str:
    """عرض القائمة الجانبية بالأسماء الجديدة والكاردات الملونة."""
    
    _inject_custom_css()

    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True

    if "current_language" not in st.session_state:
        st.session_state.current_language = "العربية"

    if "current_page" not in st.session_state:
        st.session_state.current_page = DEFAULT_PAGE

    with st.sidebar:
        # ✅ 1. كاردات التنقل بالأسماء الجديدة
        if show_navigation:
            options_list = ["HOME", "المساعد الذكي", "المستندات", "التحليلات"]
            icons_list = ["house-door-fill", "chat-dots-fill", "file-earmark-text-fill", "bar-chart-line-fill"]

            if HAS_OPTION_MENU:
                # عرض القائمة باستخدام option_menu وتنسيقها داخل كاردات ملونة
                selected_page = option_menu(
                    menu_title=None,
                    options=options_list,
                    icons=icons_list,
                    default_index=options_list.index(st.session_state.current_page) if st.session_state.current_page in options_list else 0,
                    styles={
                        "container": {"padding": "0!important", "background-color": "transparent"},
                        "icon": {"color": "#38BDF8", "font-size": "16px"},
                        "nav-link": {
                            "font-size": "14px",
                            "text-align": "right" if st.session_state.current_language == "العربية" else "left",
                            "margin": "4px 0px",
                            "color": "#94A3B8",
                            "border-radius": "10px",
                            "background-color": "#182232",
                            "border": "1px solid rgba(255, 255, 255, 0.05)",
                        },
                        "nav-link-selected": {
                            "background": "linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%)",
                            "color": "#FFFFFF",
                            "font-weight": "bold",
                            "border": "1px solid #60A5FA",
                            "box-shadow": "0 0 12px rgba(37, 99, 235, 0.4)",
                        },
                    }
                )
                st.session_state.current_page = selected_page
            else:
                # بديل بحالة عدم استخدام option_menu
                for page in options_list:
                    icon = PAGES_MAP[page]
                    is_active = (st.session_state.current_page == page)
                    if st.button(
                        f"{icon}   {page}",
                        use_container_width=True,
                        key=f"nav_card_{page}",
                        type="primary" if is_active else "secondary"
                    ):
                        st.session_state.current_page = page
                        st.rerun()

            st.markdown("---")

        # ✅ 2. الهيدر (SmartRetriever Auto)
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px; padding: 0.2rem 0;">
            <div style="
                background: linear-gradient(135deg, #2563EB, #0284C7);
                width: 42px;
                height: 42px;
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
                border: 1px solid rgba(255,255,255,0.2);
                box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3);
            ">
                ⚡
            </div>
            <div>
                <div style="font-size: 1.05rem; font-weight: 800; color: #FFFFFF; line-height: 1.2;">
                    SmartRetriever Auto
                </div>
                <div style="font-size: 0.65rem; font-weight: 700; color: #38BDF8; letter-spacing: 1px; margin-top: 2px;">
                    AI ANALYTICS PLATFORM
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # ✅ 3. الأزرار العلوية (Dark Mode / Language)
        if show_theme_toggle:
            col1, col2 = st.columns(2)
            with col1:
                theme_label = "🌙 Dark" if st.session_state.dark_mode else "☀️ Light"
                if st.button(theme_label, use_container_width=True, key="btn_theme_toggle"):
                    st.session_state.dark_mode = not st.session_state.dark_mode
                    st.rerun()

            with col2:
                lang_label = "🌐 English" if st.session_state.current_language == "العربية" else "🌐 العربية"
                if st.button(lang_label, use_container_width=True, key="btn_lang_toggle"):
                    st.session_state.current_language = "English" if st.session_state.current_language == "العربية" else "العربية"
                    st.rerun()

            st.markdown("---")

        # ✅ 4. الفوتر
        st.markdown("""
        <div style="padding-top: 0.2rem; font-size: 0.75rem; color: #64748B;">
            <div style="margin-bottom: 0.4rem; display: flex; align-items: center; gap: 6px;">
                <span>📦</span> <b style="color: #94A3B8;">AutoData</b> · 2024–2026
            </div>
            <div style="display: flex; gap: 12px; font-weight: 600;">
                <a href="https://github.com" target="_blank" style="color: #38BDF8; text-decoration: none;">🌺 GitHub</a>
                <span>·</span>
                <a href="https://linkedin.com" target="_blank" style="color: #38BDF8; text-decoration: none;">💼 LinkedIn</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    return st.session_state.get("current_page", DEFAULT_PAGE)


# ============================================================
# 2. الدوال المساعدة المساندة
# ============================================================

def render_stats_only(stats: Dict[str, Any]) -> None:
    pass

def render_navigation_only() -> str:
    return render_sidebar(show_theme_toggle=False)

def render_user_info(username: Optional[str] = None, email: Optional[str] = None) -> None:
    with st.sidebar:
        st.markdown("---")
        if username:
            st.caption(f"👤 {username}")
        if st.button("🚪 Logout", use_container_width=True, key="btn_logout"):
            st.session_state.clear()
            st.rerun()

def render_progress_in_sidebar(progress: float, label: str = "Loading...") -> None:
    with st.sidebar:
        st.progress(min(max(progress / 100, 0.0), 1.0))
        st.caption(f"{label} ({int(progress)}%)")

def render_system_status(status: str = "🟢 Online", uptime: str = "99.9%") -> None:
    with st.sidebar:
        st.caption(f"Status: {status} | Uptime: {uptime}")


# ============================================================
# تصدير كافة الدوال
# ============================================================

__all__ = [
    'render_sidebar',
    'render_stats_only',
    'render_navigation_only',
    'render_user_info',
    'render_progress_in_sidebar',
    'render_system_status',
]
