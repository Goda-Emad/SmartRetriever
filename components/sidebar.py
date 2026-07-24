"""
📌 القائمة الجانبية - Modern Dark Sidebar Component (Matching Saudi Tourism Intelligence UI)
"""

import streamlit as st
from typing import Optional, Dict, Any

# ============================================================
# ⚙️ إعدادات الصفحات والأيقونات
# ============================================================
PAGES = {
    "Overview": ("🏠", "الرئيسية"),
    "Chat Assistant": ("💬", "مساعد الذكاء"),
    "Fleet Analytics": ("📈", "تحليلات الأسطول"),
    "Documents Vault": ("📁", "أرشيف المستندات"),
    "Digital Garage": ("🚗", "كراجي الرقمي"),
    "APP Hub": ("📱", "مركز التطبيقات"),
}

DEFAULT_PAGE = "Overview"


# ============================================================
# 🎨 حقن التنسيقات البصرية CSS لتطابق التصميم 100%
# ============================================================
def _inject_custom_css():
    st.markdown("""
        <style>
        /* خلفية القائمة الجانبية داكنة وعميقة */
        [data-testid="stSidebar"] {
            background-color: #0E1717 !important;
        }
        
        /* إعادة تنسيق كافة أزرار Streamlit داخل السايدبار لتصبح كاردات دائرية */
        [data-testid="stSidebar"] div.stButton > button {
            width: 100% !important;
            background-color: #232D32 !important;
            color: #E2E8F0 !important;
            border: 1px solid #334148 !important;
            border-radius: 10px !important;
            padding: 0.55rem 1rem !important;
            font-size: 0.9rem !important;
            font-weight: 600 !important;
            transition: all 0.2s ease-in-out !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.15) !important;
            margin-bottom: 2px !important;
        }
        
        /* تأثير عند تحريك الماوس فوق الزر (Hover) */
        [data-testid="stSidebar"] div.stButton > button:hover {
            background-color: #2D3A40 !important;
            border-color: #475569 !important;
            color: #38BDF8 !important;
            transform: translateY(-1px) !important;
        }
        
        /* تنسيق الزر النشط / المالي (Primary) */
        [data-testid="stSidebar"] div.stButton > button[kind="primary"] {
            background-color: #1E293B !important;
            border: 1px solid #38BDF8 !important;
            color: #38BDF8 !important;
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.2) !important;
        }

        /* خطوط الفصل الناعمة */
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
    """عرض القائمة الجانبية المطابقة لتصميم الواجهة المرفقة."""
    
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
        # ✅ 1. الهيدر (الشعار + الاسم + الوصف الفرعي)
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px; padding: 0.2rem 0;">
            <div style="
                background: linear-gradient(135deg, #1E3A8A, #0284C7);
                width: 42px;
                height: 42px;
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
                border: 1px solid rgba(255,255,255,0.15);
                box-shadow: 0 2px 6px rgba(0,0,0,0.3);
            ">
                ⚡
            </div>
            <div>
                <div style="font-size: 1.05rem; font-weight: 800; color: #FFFFFF; line-height: 1.2;">
                    SmartRetriever Auto
                </div>
                <div style="font-size: 0.65rem; font-weight: 700; color: #38BDF8; letter-spacing: 1.2px; margin-top: 2px;">
                    AI ANALYTICS PLATFORM
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # ✅ 2. الأزرار العلوية للتحكم (Theme & Language Switches)
        if show_theme_toggle:
            theme_icon = "☀️" if st.session_state.dark_mode else "🌙"
            theme_label = f"{theme_icon} Light" if st.session_state.dark_mode else f"{theme_icon} Dark"
            
            if st.button(theme_label, use_container_width=True, key="btn_theme_toggle"):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()

            lang_label = "🌐 العربية" if st.session_state.current_language == "English" else "🌐 English"
            if st.button(lang_label, use_container_width=True, key="btn_lang_toggle"):
                st.session_state.current_language = "English" if st.session_state.current_language == "العربية" else "العربية"
                st.rerun()

            st.markdown("---")

        # ✅ 3. زر الرئيسية (Home Card)
        home_is_active = (st.session_state.current_page == "Overview")
        if st.button(
            "🏠 Home",
            use_container_width=True,
            key="btn_home_nav",
            type="primary" if home_is_active else "secondary"
        ):
            st.session_state.current_page = "Overview"
            st.rerun()

        st.markdown("---")

        # ✅ 4. قائمة الصفحات المتبقية (Navigation Cards)
        if show_navigation:
            for page_key, (icon, ar_title) in PAGES.items():
                if page_key == "Overview":
                    continue  # عُرِض بالخارج كـ Home
                
                is_active = (st.session_state.current_page == page_key)
                
                # إظهار العنوان حسب اللغة المختارة
                display_title = ar_title if st.session_state.current_language == "العربية" else page_key
                
                if st.button(
                    f"{icon} {display_title}",
                    use_container_width=True,
                    key=f"nav_{page_key}",
                    type="primary" if is_active else "secondary"
                ):
                    st.session_state.current_page = page_key
                    st.rerun()

            st.markdown("---")

        # ✅ 5. الفوتر (روابط ومعلومات المشروع)
        st.markdown("""
        <div style="padding-top: 0.2rem; font-size: 0.72rem; color: #94A3B8;">
            <div style="margin-bottom: 0.4rem; display: flex; align-items: center; gap: 6px;">
                <span>📦</span> <b>AutoData</b> · 2024–2026
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
# 2. الدوال المساعدة المساندة (لتفادي أي ImportErrors)
# ============================================================

def render_stats_only(stats: Dict[str, Any]) -> None:
    pass

def render_navigation_only() -> str:
    return render_sidebar(show_theme_toggle=False, show_stats=False)

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
