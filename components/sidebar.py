# components/sidebar.py
"""
📌 القائمة الجانبية - Sidebar Component
"""

import streamlit as st
from typing import Optional, Dict, Any

# الصفحة الافتراضية
DEFAULT_PAGE = "💬 المحادثة"
PAGES = ["💬 المحادثة", "📄 المستندات", "📊 التحليلات"]


# ============================================================
# 1. القائمة الجانبية الرئيسية
# ============================================================

def render_sidebar(
    stats: Optional[Dict[str, Any]] = None,
    show_theme_toggle: bool = True,
    show_stats: bool = True,
    show_navigation: bool = True
) -> str:
    """
    عرض القائمة الجانبية الكاملة.
    دايمًا بيرجع اسم الصفحة المحددة.
    """
    page = DEFAULT_PAGE  # قيمة آمنة افتراضية

    with st.sidebar:
        # الشعار
        st.title("🧠 SmartRetriever")
        st.caption("نظام استرجاع ذكي للمستندات")
        st.markdown("---")

        # تبديل الوضع
        if show_theme_toggle:
            if "dark_mode" not in st.session_state:
                st.session_state.dark_mode = False

            current_mode = "🌙 داكن" if st.session_state.dark_mode else "☀️ فاتح"
            if st.button(current_mode, use_container_width=True, key="theme_toggle"):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()

            st.markdown("---")

        # التنقل
        if show_navigation:
            st.markdown("## 📍 التنقل")
            page = st.radio(
                "اختر الصفحة",
                PAGES,
                index=0,
                label_visibility="collapsed"
            )
            st.markdown("---")

        # الإحصائيات
        if show_stats:
            _render_stats(stats)

        # معلومات التذييل
        st.caption("🚀 الإصدار 1.0.0")
        st.caption("© 2026 SmartRetriever")

    return page


# ============================================================
# 2. إحصائيات فقط
# ============================================================

def render_stats_only(stats: Dict[str, Any]) -> None:
    with st.sidebar:
        _render_stats(stats)


# ============================================================
# 3. تنقل فقط
# ============================================================

def render_navigation_only() -> str:
    with st.sidebar:
        st.markdown("## 📍 التنقل")
        page = st.radio(
            "اختر الصفحة",
            PAGES,
            index=0,
            label_visibility="collapsed"
        )
    return page


# ============================================================
# 4. معلومات المستخدم
# ============================================================

def render_user_info(
    username: Optional[str] = None,
    email: Optional[str] = None
) -> None:
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 👤 المستخدم")

        if username:
            st.markdown(f"**{username}**")
        if email:
            st.caption(email)

        if st.button("🚪 تسجيل الخروج", use_container_width=True, key="logout_btn"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


# ============================================================
# 5. شريط تقدم في السايدبار
# ============================================================

def render_progress_in_sidebar(progress: float, label: str = "جاري التحميل...") -> None:
    with st.sidebar:
        st.progress(min(max(progress / 100, 0.0), 1.0))
        st.caption(f"{label} ({int(progress)}%)")


# ============================================================
# 6. حالة النظام
# ============================================================

def render_system_status(status: str = "🟢 يعمل", uptime: str = "غير معروف") -> None:
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 🔧 حالة النظام")
        st.caption(f"الحالة: {status}")
        st.caption(f"مدة التشغيل: {uptime}")


# ============================================================
# helper داخلي - الإحصائيات
# ============================================================

def _render_stats(stats: Optional[Dict[str, Any]]) -> None:
    """دالة داخلية لعرض الإحصائيات (بدون with st.sidebar)."""
    st.markdown("### 📊 إحصائيات")

    if stats is None:
        stats = {
            "documents": 17,
            "suppliers": 5,
            "contracts": 5,
            "quality": 90.2,
        }

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📄 مستندات", stats.get("documents", 0),
                  delta=stats.get("documents_delta"))
    with col2:
        st.metric("🏢 موردين", stats.get("suppliers", 0),
                  delta=stats.get("suppliers_delta"))
    with col1:
        st.metric("📝 عقود", stats.get("contracts", 0),
                  delta=stats.get("contracts_delta"))
    with col2:
        quality = stats.get("quality", 0)
        st.metric("⭐ جودة", f"{quality:.1f}%",
                  delta=stats.get("quality_delta"))

    st.markdown("---")


# ============================================================
# تصدير الدوال
# ============================================================

__all__ = [
    'render_sidebar',
    'render_stats_only',
    'render_navigation_only',
    'render_user_info',
    'render_progress_in_sidebar',
    'render_system_status',
]
