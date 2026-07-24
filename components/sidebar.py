"""
📌 القائمة الجانبية - Modern SaaS Colored Cards Sidebar
"""

import streamlit as st
from typing import Optional, Dict, Any

# ============================================================
# ⚙️ إعدادات الصفحات بالترتيب المعتمد
# ============================================================
PAGES = {
    "HOME": "🏠",
    "المساعد الذكي": "💬",
    "المستندات": "📁",
    "التحليلات": "📊",
}

DEFAULT_PAGE = "HOME"


# ============================================================
# 🎨 حقن CSS المطور للكاردات الملونة
# ============================================================
def _inject_custom_css():
    st.markdown("""
        <style>
        /* خلفية السايدبار الداكنة */
        [data-testid="stSidebar"] {
            background-color: #0B1120 !important;
        }
        
        /* تصميم الأزرار العادية لتصبح كاردات أنيقة */
        [data-testid="stSidebar"] div.stButton > button {
            width: 100% !important;
            background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%) !important;
            color: #F1F5F9 !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 12px !important;
            padding: 0.7rem 1rem !important;
            font-size: 0.95rem !important;
            font-weight: 700 !important;
            transition: all 0.25s ease-in-out !important;
            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2) !important;
            margin-bottom: 4px !important;
        }
        
        /* تأثير عند تمرير الماوس فوق الكارد */
        [data-testid="stSidebar"] div.stButton > button:hover {
            background: linear-gradient(135deg, #334155 0%, #1E293B 100%) !important;
            border-color: #38BDF8 !important;
            color: #38BDF8 !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 12px -2px rgba(56, 189, 248, 0.2) !important;
        }
        
        /* تصميم الكارد الملون للصفحة النشطة (Active Page) */
        [data-testid="stSidebar"] div.stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #4F46E5 0%, #2563EB 100%) !important;
            color: #FFFFFF !important;
            border: 1px solid #818CF8 !important;
            box-shadow: 0 0 15px rgba(99, 102, 241, 0.4) !important;
        }

        /* أزرار التحكم العلوية (Dark/English) */
        .control-btn div.stButton > button {
            background: #1E293B !important;
            border-radius: 10px !important;
            padding: 0.4rem !important;
            font-size: 0.85rem !important;
        }

        /* الفواصل الناعمة */
        [data-testid="stSidebar"] hr {
            border-color: rgba(255, 255, 255, 0.08) !important;
            margin: 0.9rem 0 !important;
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
    """عرض السايدبار بتصميم الكاردات الملونة بدون تكرار."""
    
    # تطبيق التنسيقات
    _inject_custom_css()

    # تهيئة حالة الجلسة
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True

    if "current_language" not in st.session_state:
        st.session_state.current_language = "العربية"

    if "current_page" not in st.session_state:
        st.session_state.current_page = DEFAULT_PAGE

    with st.sidebar:
        # ✅ 1. الهيدر (الشعار واسم المنصة)
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px; padding: 0.2rem 0 0.5rem 0;">
            <div style="
                background: linear-gradient(135deg, #2563EB, #0284C7);
                width: 44px;
                height: 44px;
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 22px;
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

        # ✅ 2. أدوات التحكم العلوي (Dark Mode & Language)
        if show_theme_toggle:
            theme_icon = "🌙" if st.session_state.dark_mode else "☀️"
            theme_label = f"{theme_icon} Dark" if st.session_state.dark_mode else f"{theme_icon} Light"
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(theme_label, use_container_width=True, key="btn_theme_toggle"):
                    st.session_state.dark_mode = not st.session_state.dark_mode
                    st.rerun()

            with col2:
                lang_label = "🌐 English" if st.session_state.current_language == "العربية" else "🌐 العربية"
                if st.button(lang_label, use_container_width=True, key="btn_lang_toggle"):
                    st.session_state.current_language = "English" if st.session_state.current_language == "العربية" else "العربية"
                    st.rerun()

            st.markdown("---")

        # ✅ 3. التنقل الرئيسي - كاردات ملونة احترافية (HOME, المساعد الذكي, المستندات, التحليلات)
        if show_navigation:
            st.markdown("""
            <div style="margin-bottom: 0.6rem;">
                <span style="font-size: 0.7rem; font-weight: 800; color: #64748B; text-transform: uppercase; letter-spacing: 1.2px;">
                    📌 التنقل الرئيسي
                </span>
            </div>
            """, unsafe_allow_html=True)

            for page_name, icon in PAGES.items():
                is_active = (st.session_state.current_page == page_name)
                
                # إنشاء الزر داخل كارد
                if st.button(
                    f"{icon}   {page_name}",
                    use_container_width=True,
                    key=f"nav_card_{page_name}",
                    type="primary" if is_active else "secondary"
                ):
                    st.session_state.current_page = page_name
                    st.rerun()

            st.markdown("---")

        # ✅ 4. الفوتر النهائي
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
# 2. الدوال المساعدة (تمنع خطأ Import)
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
# تصدير جميع الدوال
# ============================================================
__all__ = [
    'render_sidebar',
    'render_stats_only',
    'render_navigation_only',
    'render_user_info',
    'render_progress_in_sidebar',
    'render_system_status',
]
