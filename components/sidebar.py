"""
📌 القائمة الجانبية - Modern Sidebar Component (Streamlit Ready)
"""

from typing import Any, Dict, Optional
import streamlit as st

# ============================================================
# ⚙️ إعدادات الصفحات والأيقونات (محدثة بمسميات احترافية)
# ============================================================
PAGES = {
    "📱 مركز التطبيقات (APP Hub)": "📱",
    "💬 مساعد الذكاء الاصطناعي": "🤖",
    "🚘 كراجي الرقمي": "🚗",
    "📄 صندوق القفازات الرقمي": "📁",
    "📊 تحليلات الأسطول": "📈",
}

DEFAULT_PAGE = "💬 مساعد الذكاء الاصطناعي"


# ============================================================
# 🎨 حقن التنسيقات البصرية (Custom CSS)
# ============================================================
def _inject_custom_styles(is_dark: bool) -> None:
    """حقن CSS مخصص للحصول على مظهر احترافي ديناميكي"""
    bg_card = "#1E293B" if is_dark else "#F8FAFC"
    border_color = "#334155" if is_dark else "#E2E8F0"
    text_primary = "#F8FAFC" if is_dark else "#0F172A"
    text_secondary = "#94A3B8" if is_dark else "#64748B"

    st.markdown(
        f"""
        <style>
        /* تحسين مظهر البطاقات الخاصة بالإحصائيات */
        .stat-card {{
            background-color: {bg_card};
            border: 1px solid {border_color};
            border-radius: 12px;
            padding: 0.75rem;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
        }}
        .stat-card:hover {{
            transform: translateY(-2px);
        }}
        .stat-label {{
            font-size: 0.75rem;
            color: {text_secondary};
            font-weight: 600;
            margin-bottom: 0.2rem;
        }}
        .stat-value {{
            font-size: 1.25rem;
            font-weight: 800;
            color: {text_primary};
        }}
        .stat-value-success {{
            font-size: 1.25rem;
            font-weight: 800;
            color: #10B981;
        }}
        </style>
    """,
        unsafe_allow_html=True,
    )


# ============================================================
# 1. القائمة الجانبية الرئيسية
# ============================================================
def render_sidebar(
    stats: Optional[Dict[str, Any]] = None,
    show_theme_toggle: bool = True,
    show_stats: bool = True,
    show_navigation: bool = True,
) -> str:
    """عرض القائمة الجانبية الكاملة وإرجاع اسم الصفحة المحددة."""

    # تهيئة حالة الجلسة
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True

    if "current_page" not in st.session_state:
        st.session_state.current_page = DEFAULT_PAGE

    # تطبيق التنسيقات بناءً على الوضع الحالي
    _inject_custom_styles(st.session_state.dark_mode)

    with st.sidebar:
        # ✅ 1. الشعار والهوية البصرية
        st.markdown(
            """
            <div style="text-align: center; padding: 0.5rem 0 1rem 0;">
                <div style="font-size: 2.2rem; margin-bottom: 0.2rem;">⚡</div>
                <div style="font-size: 1.3rem; font-weight: 800; letter-spacing: -0.5px;">
                    SmartRetriever <span style="font-size: 0.65rem; background: #2563EB; color: white; padding: 2px 6px; border-radius: 6px; vertical-align: middle;">Auto</span>
                </div>
                <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 0.2rem;">
                    منصة إدارة واسترجاع بيانات الأسطول
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # ✅ 2. زر تبديل الوضع (ليلي/فاتح) - خالي من الأخطاء
        if show_theme_toggle:
            mode_label = (
                "☀️ التبديل للوضع الفاتح"
                if st.session_state.dark_mode
                else "🌙 التبديل للوضع الداكن"
            )

            if st.button(mode_label, use_container_width=True, key="theme_toggle_btn"):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()

            st.markdown("---")

        # ✅ 3. روابط التنقل بين الصفحات
        if show_navigation:
            st.markdown(
                """
                <div style="margin-bottom: 0.5rem;">
                    <span style="font-size: 0.7rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">
                        📍 التنقل الرئيسي
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            for page_name, icon in PAGES.items():
                is_selected = st.session_state.current_page == page_name

                # أزرار التنقل مع تمييز الصفحة النشطة
                if st.button(
                    page_name,
                    key=f"nav_btn_{page_name}",
                    use_container_width=True,
                    type="primary" if is_selected else "secondary",
                ):
                    st.session_state.current_page = page_name
                    st.rerun()

            st.markdown("---")

        # ✅ 4. بطاقات الإحصائيات (KPI Cards)
        if show_stats:
            _render_stats(stats)

        # ✅ 5. التذييل (Footer)
        st.markdown(
            """
            <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid rgba(148, 163, 184, 0.2); text-align: center; font-size: 0.7rem; color: #94A3B8;">
                <div>🚀 الإصدار 1.0.0 Pro</div>
                <div style="margin-top: 0.2rem;">© 2026 SmartRetriever Auto</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    return st.session_state.get("current_page", DEFAULT_PAGE)


# ============================================================
# 2. مكونات مساعدة (Sub-Components)
# ============================================================
def _render_stats(stats: Optional[Dict[str, Any]]) -> None:
    """عرض الإحصائيات بتصميم شبكي مميز"""
    st.markdown(
        """
        <div style="margin-bottom: 0.6rem;">
            <span style="font-size: 0.7rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">
                📊 مؤشرات الأسطول
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if stats is None:
        stats = {
            "documents": 17,
            "suppliers": 5,
            "contracts": 5,
            "quality": 90.2,
        }

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-label">📄 المستندات</div>
                <div class="stat-value">{stats.get('documents', 0)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div style='margin-bottom: 8px;'></div>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-label">📝 العقود</div>
                <div class="stat-value">{stats.get('contracts', 0)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-label">🏢 الموردين</div>
                <div class="stat-value">{stats.get('suppliers', 0)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div style='margin-bottom: 8px;'></div>", unsafe_allow_html=True)
        quality = stats.get("quality", 0)
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-label">⭐ الجودة</div>
                <div class="stat-value-success">{quality:.1f}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)


def render_user_info(
    username: Optional[str] = None, email: Optional[str] = None
) -> None:
    """عرض بيانات المستخدم وإمكانية تسجيل الخروج"""
    with st.sidebar:
        st.markdown("---")
        st.markdown("**👤 حساب المستخدم**")
        if username:
            st.text(f"المستخدم: {username}")
        if email:
            st.caption(email)

        if st.button("🚪 تسجيل الخروج", use_container_width=True, key="logout_btn"):
            st.session_state.clear()
            st.rerun()


def render_system_status(
    status: str = "🟢 متصل", uptime: str = "99.9%"
) -> None:
    """عرض حالة السيرفر"""
    with st.sidebar:
        st.markdown(
            f"""
            <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10B981; padding: 0.5rem; border-radius: 8px; font-size: 0.75rem; text-align: center; margin-top: 0.5rem;">
                <div>حالة النظام: <b>{status}</b></div>
                <div style="color: #64748B;">جاهزية التشغيل: {uptime}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# تصدير الدوال النظيفة
# ============================================================
__all__ = [
    "render_sidebar",
    "render_user_info",
    "render_system_status",
]
