"""
📌 القائمة الجانبية - Sidebar Component (كامل ومعدل بدون أخطاء استيراد)
"""

import streamlit as st
from typing import Optional, Dict, Any

# ============================================================
# الصفحات والأيقونات المحدثة
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
# 1. القائمة الجانبية الرئيسية
# ============================================================

def render_sidebar(
    stats: Optional[Dict[str, Any]] = None,
    show_theme_toggle: bool = True,
    show_stats: bool = True,
    show_navigation: bool = True
) -> str:
    """عرض القائمة الجانبية الكاملة وإرجاع اسم الصفحة المحددة."""
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = DEFAULT_PAGE

    with st.sidebar:
        # ✅ الشعار والهوية البصرية المحسنة
        st.markdown("""
        <div style="text-align: center; padding: 0.5rem 0 1rem 0;">
            <div style="font-size: 2.2rem; margin-bottom: 0.2rem;">⚡</div>
            <div style="font-size: 1.3rem; font-weight: 800; letter-spacing: -0.5px;">
                SmartRetriever <span style="font-size: 0.65rem; background: #2563EB; color: white; padding: 2px 6px; border-radius: 6px; vertical-align: middle;">Auto</span>
            </div>
            <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 0.2rem;">
                نظام استرجاع ذكي وإدارة البيانات
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")

        # ✅ زر تبديل الوضع (ليلي/فاتح) بدون تكرار أو أخطاء
        if show_theme_toggle:
            if "dark_mode" not in st.session_state:
                st.session_state.dark_mode = True

            mode_text = "☀️ الوضع الفاتح" if st.session_state.dark_mode else "🌙 الوضع الداكن"
            
            if st.button(mode_text, use_container_width=True, key="theme_toggle_btn"):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()

            st.markdown("---")

        # ✅ التنقل بين الصفحات
        if show_navigation:
            st.markdown("""
            <div style="margin-bottom: 0.6rem;">
                <span style="font-size: 0.7rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">
                    📍 التنقل الرئيسي
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            for page_name, icon in PAGES.items():
                is_active = (st.session_state.current_page == page_name)
                
                # استخدام أزرار Streamlit الرسمية لضمان الاستجابة السريعة
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
            _render_stats(stats)

        # ✅ تذييل القائمة
        st.markdown("""
        <div style="
            margin-top: 1.5rem;
            padding-top: 0.75rem;
            border-top: 1px solid rgba(148, 163, 184, 0.2);
            text-align: center;
            font-size: 0.7rem;
            color: #64748B;
        ">
            <div>🚀 الإصدار 1.0.0 Pro</div>
            <div style="margin-top: 0.2rem;">© 2026 SmartRetriever Auto</div>
        </div>
        """, unsafe_allow_html=True)

    return st.session_state.get("current_page", DEFAULT_PAGE)


# ============================================================
# 2. إحصائيات فقط (تمت إعادتها للسلامة)
# ============================================================

def render_stats_only(stats: Dict[str, Any]) -> None:
    with st.sidebar:
        _render_stats(stats)


# ============================================================
# 3. تنقل فقط (تمت إعادتها للسلامة)
# ============================================================

def render_navigation_only() -> str:
    if "current_page" not in st.session_state:
        st.session_state.current_page = DEFAULT_PAGE
        
    with st.sidebar:
        st.markdown("""
        <div style="margin-bottom: 0.6rem;">
            <span style="font-size: 0.7rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">
                📍 التنقل
            </span>
        </div>
        """, unsafe_allow_html=True)
        
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
# 5. شريط تقدم في السايدبار (تمت إعادته)
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
# helper داخلي - الإحصائيات بتصميم شبكي احترافي
# ============================================================

def _render_stats(stats: Optional[Dict[str, Any]]) -> None:
    st.markdown("""
    <div style="margin-bottom: 0.6rem;">
        <span style="font-size: 0.7rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">
            📊 الإحصائيات
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
        <div style="background: rgba(30, 41, 59, 0.5); border-radius: 10px; padding: 0.5rem; text-align: center; border: 1px solid rgba(255,255,255,0.08); margin-bottom: 0.4rem;">
            <div style="font-size: 0.65rem; color: #94A3B8;">📄 مستندات</div>
            <div style="font-size: 1.1rem; font-weight: 700;">{stats.get('documents', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: rgba(30, 41, 59, 0.5); border-radius: 10px; padding: 0.5rem; text-align: center; border: 1px solid rgba(255,255,255,0.08); margin-bottom: 0.4rem;">
            <div style="font-size: 0.65rem; color: #94A3B8;">🏢 موردين</div>
            <div style="font-size: 1.1rem; font-weight: 700;">{stats.get('suppliers', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col1:
        st.markdown(f"""
        <div style="background: rgba(30, 41, 59, 0.5); border-radius: 10px; padding: 0.5rem; text-align: center; border: 1px solid rgba(255,255,255,0.08);">
            <div style="font-size: 0.65rem; color: #94A3B8;">📝 عقود</div>
            <div style="font-size: 1.1rem; font-weight: 700;">{stats.get('contracts', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        quality = stats.get('quality', 0)
        st.markdown(f"""
        <div style="background: rgba(30, 41, 59, 0.5); border-radius: 10px; padding: 0.5rem; text-align: center; border: 1px solid rgba(255,255,255,0.08);">
            <div style="font-size: 0.65rem; color: #94A3B8;">⭐ جودة</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #10B981;">{quality:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")


# ============================================================
# تصدير كل الدوال لتجنب أي ImportError في __init__.py
# ============================================================

__all__ = [
    'render_sidebar',
    'render_stats_only',
    'render_navigation_only',
    'render_user_info',
    'render_progress_in_sidebar',
    'render_system_status',
]
