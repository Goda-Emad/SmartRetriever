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
        # ✅ الشعار المحسن
        st.markdown("""
        <div style="text-align: center; padding: 0.5rem 0 1rem 0;">
            <div style="font-size: 3rem; margin-bottom: -0.5rem;">🧠</div>
            <div style="font-size: 1.5rem; font-weight: 800; color: #F8FAFC; letter-spacing: -0.5px;">
                SmartRetriever
            </div>
            <div style="font-size: 0.8rem; color: #94A3B8; margin-top: 0.25rem;">
                نظام استرجاع ذكي للمستندات
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")

        # ✅ تبديل الوضع (زر محسن)
        if show_theme_toggle:
            if "dark_mode" not in st.session_state:
                st.session_state.dark_mode = False

            current_mode = "🌙 ليلي" if st.session_state.dark_mode else "☀️ فاتح"
            icon = "🌙" if st.session_state.dark_mode else "☀️"
            
            # ✅ زر تبديل الوضع بتصميم أنيق
            st.markdown(f"""
            <div style="text-align: center; margin: 0.5rem 0;">
                <button onclick="document.querySelector('[data-testid=\"baseButton-secondary\"]').click()" 
                        style="
                            background: {'#1E293B' if st.session_state.dark_mode else '#E2E8F0'};
                            color: {'#F8FAFC' if st.session_state.dark_mode else '#1E293B'};
                            border: 1px solid {'#334155' if st.session_state.dark_mode else '#CBD5E1'};
                            border-radius: 12px;
                            padding: 0.6rem 1.2rem;
                            font-size: 0.9rem;
                            font-weight: 600;
                            cursor: pointer;
                            width: 100%;
                            transition: all 0.3s ease;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            gap: 0.5rem;
                        "
                        onmouseover="this.style.transform='scale(1.02)'"
                        onmouseout="this.style.transform='scale(1)'"
                >
                    {icon} {current_mode}
                </button>
            </div>
            """, unsafe_allow_html=True)
            
            # ✅ زر حقيقي لتشغيل التبديل
            if st.button(current_mode, use_container_width=True, key="theme_toggle"):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()

            st.markdown("---")

        # ✅ التنقل المحسن (بأيقونات بارزة)
        if show_navigation:
            st.markdown("""
            <div style="margin-bottom: 0.75rem;">
                <span style="font-size: 0.75rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">
                    📍 التنقل
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            # ✅ صفحات مخصصة مع أيقونات بارزة
            page_icons = {
                "💬 المحادثة": "💬",
                "📄 المستندات": "📄",
                "📊 التحليلات": "📊"
            }
            
            # ✅ استخدام أزرار بدلاً من راديو للحصول على تصميم أفضل
            selected = DEFAULT_PAGE
            cols = st.columns(1)
            
            for i, page_name in enumerate(PAGES):
                icon = page_icons.get(page_name, "📌")
                # تحديد ما إذا كانت الصفحة محددة
                is_selected = (page_name == page)
                
                # ✅ زر الصفحة بتصميم احترافي
                if st.button(
                    f"{icon}  {page_name}",
                    use_container_width=True,
                    key=f"nav_{i}",
                    type="primary" if is_selected else "secondary"
                ):
                    selected = page_name
                    st.rerun()
            
            page = selected
            st.markdown("---")

        # ✅ الإحصائيات المحسنة
        if show_stats:
            _render_stats(stats)

        # ✅ معلومات التذييل المحسنة
        st.markdown("""
        <div style="
            margin-top: 1.5rem;
            padding-top: 0.75rem;
            border-top: 1px solid #334155;
            text-align: center;
            font-size: 0.7rem;
            color: #64748B;
        ">
            <div>🚀 الإصدار 1.0.0</div>
            <div style="margin-top: 0.2rem;">© 2026 SmartRetriever</div>
        </div>
        """, unsafe_allow_html=True)

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
        st.markdown("""
        <div style="margin-bottom: 0.75rem;">
            <span style="font-size: 0.75rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">
                📍 التنقل
            </span>
        </div>
        """, unsafe_allow_html=True)
        
        page = DEFAULT_PAGE
        for i, page_name in enumerate(PAGES):
            icon = {"💬 المحادثة": "💬", "📄 المستندات": "📄", "📊 التحليلات": "📊"}.get(page_name, "📌")
            if st.button(f"{icon}  {page_name}", use_container_width=True, key=f"nav_only_{i}"):
                page = page_name
                st.rerun()
    
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
        st.markdown("""
        <div style="margin-bottom: 0.5rem;">
            <span style="font-weight: 600; color: #F8FAFC;">👤 المستخدم</span>
        </div>
        """, unsafe_allow_html=True)

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
        st.markdown("""
        <div style="margin-bottom: 0.5rem;">
            <span style="font-weight: 600; color: #F8FAFC;">🔧 حالة النظام</span>
        </div>
        """, unsafe_allow_html=True)
        st.caption(f"الحالة: {status}")
        st.caption(f"مدة التشغيل: {uptime}")


# ============================================================
# helper داخلي - الإحصائيات المحسنة
# ============================================================

def _render_stats(stats: Optional[Dict[str, Any]]) -> None:
    """دالة داخلية لعرض الإحصائيات بتصميم محسن"""
    st.markdown("""
    <div style="margin-bottom: 0.75rem;">
        <span style="font-size: 0.75rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">
            📊 إحصائيات
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

    # ✅ إحصائيات بتصميم بطاقات مصغرة
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style="
            background: #1E293B;
            border-radius: 10px;
            padding: 0.5rem 0.75rem;
            text-align: center;
            border: 1px solid #334155;
            margin-bottom: 0.3rem;
        ">
            <div style="font-size: 0.65rem; color: #94A3B8;">📄 مستندات</div>
            <div style="font-size: 1.2rem; font-weight: 700; color: #F8FAFC;">{stats.get('documents', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: #1E293B;
            border-radius: 10px;
            padding: 0.5rem 0.75rem;
            text-align: center;
            border: 1px solid #334155;
            margin-bottom: 0.3rem;
        ">
            <div style="font-size: 0.65rem; color: #94A3B8;">🏢 موردين</div>
            <div style="font-size: 1.2rem; font-weight: 700; color: #F8FAFC;">{stats.get('suppliers', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: #1E293B;
            border-radius: 10px;
            padding: 0.5rem 0.75rem;
            text-align: center;
            border: 1px solid #334155;
            margin-bottom: 0.3rem;
        ">
            <div style="font-size: 0.65rem; color: #94A3B8;">📝 عقود</div>
            <div style="font-size: 1.2rem; font-weight: 700; color: #F8FAFC;">{stats.get('contracts', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        quality = stats.get('quality', 0)
        st.markdown(f"""
        <div style="
            background: #1E293B;
            border-radius: 10px;
            padding: 0.5rem 0.75rem;
            text-align: center;
            border: 1px solid #334155;
            margin-bottom: 0.3rem;
        ">
            <div style="font-size: 0.65rem; color: #94A3B8;">⭐ جودة</div>
            <div style="font-size: 1.2rem; font-weight: 700; color: #10B981;">{quality:.1f}%</div>
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
