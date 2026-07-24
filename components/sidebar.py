"""
📌 القائمة الجانبية - Modern SaaS Sidebar Component (Fixed UnboundLocalError)
"""

import streamlit as st
from typing import Optional, Dict, Any

# ============================================================
# ⚙️ إعدادات الصفحات
# ============================================================
PAGES = {
    "💬 المساعد الذكي": "💬",
    "📁 أرشيف المستندات": "📄",
    "📊 مؤشرات الأداء": "📊",
    "🚘 كراجي الرقمي": "🚗",
}

DEFAULT_PAGE = "💬 المساعد الذكي"


# ============================================================
# 1. القائمة الجانبية الرئيسية
# ============================================================

def render_sidebar(
    stats: Optional[Dict[str, Any]] = None,
    show_theme_toggle: bool = True,
    show_stats: bool = True,
    show_navigation: bool = True
) -> str:
    """عرض القائمة الجانبية الكاملة وإرجاع اسم الصفحة المحددة."""
    
    # 1. تهيئة حالة الجلسة
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True

    if "current_page" not in st.session_state:
        st.session_state.current_page = DEFAULT_PAGE

    is_dark = st.session_state.dark_mode

    # ✅ حل المشكلة: تعريف المتغيرات في البداية لتكون متاحة للدالة بالكامل
    card_bg = "rgba(30, 41, 59, 0.7)" if is_dark else "rgba(241, 245, 249, 0.9)"
    card_border = "rgba(255, 255, 255, 0.1)" if is_dark else "rgba(0, 0, 0, 0.08)"
    text_sub = "#94A3B8" if is_dark else "#64748B"

    with st.sidebar:
        # ✅ الشعار وهوية التطبيق
        st.markdown("""
        <div style="text-align: center; padding: 0.2rem 0 0.8rem 0;">
            <div style="font-size: 2.2rem; margin-bottom: 0.1rem;">⚡</div>
            <div style="font-size: 1.3rem; font-weight: 800; letter-spacing: -0.5px; color: inherit;">
                SmartRetriever <span style="font-size: 0.65rem; background: #2563EB; color: white; padding: 2px 6px; border-radius: 6px; vertical-align: middle;">Auto</span>
            </div>
            <div style="font-size: 0.75rem; opacity: 0.7; margin-top: 0.2rem;">
                نظام استرجاع ذكي للمستندات والأسطول
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")

        # ✅ زر تبديل الوضع (ليلي / فاتح)
        if show_theme_toggle:
            btn_label = "☀️ الوضع الفاتح" if is_dark else "🌙 الوضع الداكن"
            
            if st.button(btn_label, use_container_width=True, key="theme_toggle_btn"):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()

            st.markdown("---")

        # ✅ بطاقة مساحة العمل + الصفحات
        if show_navigation:
            st.markdown(f"""
            <div style="
                background: {card_bg};
                border: 1px solid {card_border};
                border-radius: 12px;
                padding: 0.6rem 0.8rem;
                margin-bottom: 0.8rem;
                display: flex;
                align-items: center;
                justify-content: space-between;
            ">
                <div style="display: flex; align-items: center; gap: 0.6rem;">
                    <div style="background: #2563EB; width: 10px; height: 10px; border-radius: 50%;"></div>
                    <div>
                        <div style="font-size: 0.85rem; font-weight: 700;">مساحة العمل | APP</div>
                        <div style="font-size: 0.65rem; color: {text_sub};">SmartRetriever Hub</div>
                    </div>
                </div>
                <span style="font-size: 0.7rem; background: rgba(37, 99, 235, 0.2); color: #3B82F6; padding: 2px 6px; border-radius: 4px;">نشط</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="margin-bottom: 0.4rem;">
                <span style="font-size: 0.7rem; font-weight: 700; color: {text_sub}; text-transform: uppercase; letter-spacing: 1px;">
                    📍 الصفحات الرئيسية
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            for page_name, icon in PAGES.items():
                is_active = (st.session_state.current_page == page_name)
                
                if st.button(
                    f"{icon}  {page_name}",
                    use_container_width=True,
                    key=f"nav_btn_{page_name}",
                    type="primary" if is_active else "secondary"
                ):
                    st.session_state.current_page = page_name
                    st.rerun()
            
            st.markdown("---")

        # ✅ الإحصائيات
        if show_stats:
            _render_stats(stats, is_dark)

        # ✅ تذييل القائمة (كان يسبب الخطأ بسبب card_border)
        st.markdown(f"""
        <div style="
            margin-top: 1.5rem;
            padding-top: 0.75rem;
            border-top: 1px solid {card_border};
            text-align: center;
            font-size: 0.7rem;
            color: {text_sub};
        ">
            <div>🚀 الإصدار 1.0.0 Pro</div>
            <div style="margin-top: 0.1rem;">© 2026 SmartRetriever Auto</div>
        </div>
        """, unsafe_allow_html=True)

    return st.session_state.get("current_page", DEFAULT_PAGE)


# ============================================================
# 2. الدوال المساعدة المساندة
# ============================================================

def render_stats_only(stats: Dict[str, Any]) -> None:
    is_dark = st.session_state.get("dark_mode", True)
    with st.sidebar:
        _render_stats(stats, is_dark)


def render_navigation_only() -> str:
    if "current_page" not in st.session_state:
        st.session_state.current_page = DEFAULT_PAGE
        
    with st.sidebar:
        for page_name, icon in PAGES.items():
            is_active = (st.session_state.current_page == page_name)
            if st.button(
                f"{icon} {page_name}", 
                use_container_width=True, 
                key=f"nav_only_{page_name}",
                type="primary" if is_active else "secondary"
            ):
                st.session_state.current_page = page_name
                st.rerun()
    
    return st.session_state.get("current_page", DEFAULT_PAGE)


def render_user_info(username: Optional[str] = None, email: Optional[str] = None) -> None:
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 👤 المستخدم")
        if username:
            st.markdown(f"**{username}**")
        if email:
            st.caption(email)
        if st.button("🚪 تسجيل الخروج", use_container_width=True, key="logout_btn"):
            st.session_state.clear()
            st.rerun()


def render_progress_in_sidebar(progress: float, label: str = "جاري التحميل...") -> None:
    with st.sidebar:
        st.progress(min(max(progress / 100, 0.0), 1.0))
        st.caption(f"{label} ({int(progress)}%)")


def render_system_status(status: str = "🟢 يعمل", uptime: str = "غير معروف") -> None:
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 🔧 حالة النظام")
        st.caption(f"الحالة: {status}")
        st.caption(f"مدة التشغيل: {uptime}")


# ============================================================
# helper داخلي - بطاقات الإحصائيات
# ============================================================

def _render_stats(stats: Optional[Dict[str, Any]], is_dark: bool = True) -> None:
    card_bg = "rgba(30, 41, 59, 0.6)" if is_dark else "rgba(241, 245, 249, 0.8)"
    card_border = "rgba(255, 255, 255, 0.08)" if is_dark else "rgba(0, 0, 0, 0.06)"
    text_sub = "#94A3B8" if is_dark else "#64748B"

    st.markdown(f"""
    <div style="margin-bottom: 0.6rem;">
        <span style="font-size: 0.7rem; font-weight: 700; color: {text_sub}; text-transform: uppercase; letter-spacing: 1px;">
            📊 مؤشرات الأداء
        </span>
    </div>
    """, unsafe_allow_html=True)

    if stats is None:
        stats = {
            "documents": 17,
            "suppliers": 5,
            "contracts": 5,
            "quality": 90.2,
        }

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style="background: {card_bg}; border-radius: 10px; padding: 0.5rem; text-align: center; border: 1px solid {card_border}; margin-bottom: 0.4rem;">
            <div style="font-size: 0.65rem; color: {text_sub};">📄 مستندات</div>
            <div style="font-size: 1.1rem; font-weight: 700;">{stats.get('documents', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: {card_bg}; border-radius: 10px; padding: 0.5rem; text-align: center; border: 1px solid {card_border}; margin-bottom: 0.4rem;">
            <div style="font-size: 0.65rem; color: {text_sub};">🏢 موردين</div>
            <div style="font-size: 1.1rem; font-weight: 700;">{stats.get('suppliers', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col1:
        st.markdown(f"""
        <div style="background: {card_bg}; border-radius: 10px; padding: 0.5rem; text-align: center; border: 1px solid {card_border};">
            <div style="font-size: 0.65rem; color: {text_sub};">📝 عقود</div>
            <div style="font-size: 1.1rem; font-weight: 700;">{stats.get('contracts', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        quality = stats.get('quality', 0)
        st.markdown(f"""
        <div style="background: {card_bg}; border-radius: 10px; padding: 0.5rem; text-align: center; border: 1px solid {card_border};">
            <div style="font-size: 0.65rem; color: {text_sub};">⭐ جودة</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #10B981;">{quality:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

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
