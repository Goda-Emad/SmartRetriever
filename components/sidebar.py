# app/components/sidebar.py
"""
📌 القائمة الجانبية - Sidebar Component

تعرض القائمة الجانبية للتطبيق مع الإحصائيات والتنقل
"""

import streamlit as st
from typing import Optional, Dict, Any


# ============================================================
# 1. عرض القائمة الجانبية الرئيسية
# ============================================================

def render_sidebar(
    stats: Optional[Dict[str, Any]] = None,
    show_theme_toggle: bool = True,
    show_stats: bool = True,
    show_navigation: bool = True
) -> str:
    """
    عرض القائمة الجانبية للتطبيق
    
    Args:
        stats: إحصائيات التطبيق (مستندات، موردين، إلخ)
        show_theme_toggle: عرض زر تبديل الوضع
        show_stats: عرض الإحصائيات
        show_navigation: عرض التنقل
        
    Returns:
        الصفحة المحددة (اسم الصفحة)
    """
    
    with st.sidebar:
        # ============================================================
        # 1. الشعار والاسم
        # ============================================================
        
        st.title("🧠 ProcureMind-AI")
        st.caption("نظام ذكاء اصطناعي للمشتريات")
        st.markdown("---")
        
        # ============================================================
        # 2. تبديل الوضع (داكن/فاتح)
        # ============================================================
        
        if show_theme_toggle:
            # تهيئة حالة الوضع
            if "dark_mode" not in st.session_state:
                st.session_state.dark_mode = False
            
            # زر تبديل الوضع
            current_mode = "🌙 داكن" if st.session_state.dark_mode else "☀️ فاتح"
            if st.button(f"{current_mode}", use_container_width=True):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()
            
            st.markdown("---")
        
        # ============================================================
        # 3. التنقل بين الصفحات
        # ============================================================
        
        if show_navigation:
            st.markdown("## 📍 التنقل")
            
            page = st.radio(
                "اختر الصفحة",
                ["💬 المحادثة", "📄 المستندات", "📊 التحليلات"],
                index=0,
                label_visibility="collapsed"
            )
            
            st.markdown("---")
        
        # ============================================================
        # 4. الإحصائيات
        # ============================================================
        
        if show_stats:
            st.markdown("### 📊 إحصائيات")
            
            # إحصائيات افتراضية إذا لم يتم توفيرها
            if stats is None:
                stats = {
                    "documents": 17,
                    "suppliers": 5,
                    "contracts": 5,
                    "quality": 90.2
                }
            
            # عرض الإحصائيات في شبكة 2x2
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    label="📄 مستندات",
                    value=stats.get("documents", 0),
                    delta=stats.get("documents_delta", "+2")
                )
            
            with col2:
                st.metric(
                    label="🏢 موردين",
                    value=stats.get("suppliers", 0),
                    delta=stats.get("suppliers_delta", "+1")
                )
            
            with col1:
                st.metric(
                    label="📝 عقود",
                    value=stats.get("contracts", 0),
                    delta=stats.get("contracts_delta", "0")
                )
            
            with col2:
                quality = stats.get("quality", 0)
                st.metric(
                    label="⭐ جودة",
                    value=f"{quality:.1f}%",
                    delta=stats.get("quality_delta", "+5%")
                )
            
            st.markdown("---")
        
        # ============================================================
        # 5. معلومات إضافية
        # ============================================================
        
        st.caption("🚀 الإصدار 2.0.0")
        st.caption("© 2026 ProcureMind-AI")
        
        # رابط GitHub (اختياري)
        github_url = "https://github.com/your-username/ProcureMind-AI"
        st.markdown(f"[![GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)]({github_url})")
    
    # ============================================================
    # 6. إرجاع الصفحة المحددة
    # ============================================================
    
    return page if show_navigation else "💬 المحادثة"


# ============================================================
# 2. عرض إحصائيات فقط
# ============================================================

def render_stats_only(stats: Dict[str, Any]) -> None:
    """
    عرض الإحصائيات فقط في القائمة الجانبية
    
    Args:
        stats: إحصائيات التطبيق
    """
    with st.sidebar:
        st.markdown("### 📊 إحصائيات")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("📄 مستندات", stats.get("documents", 0))
        with col2:
            st.metric("🏢 موردين", stats.get("suppliers", 0))
        
        with col1:
            st.metric("📝 عقود", stats.get("contracts", 0))
        with col2:
            st.metric("⭐ جودة", f"{stats.get('quality', 0):.1f}%")


# ============================================================
# 3. عرض التنقل فقط
# ============================================================

def render_navigation_only() -> str:
    """
    عرض التنقل فقط في القائمة الجانبية
    
    Returns:
        الصفحة المحددة
    """
    with st.sidebar:
        st.markdown("## 📍 التنقل")
        
        page = st.radio(
            "اختر الصفحة",
            ["💬 المحادثة", "📄 المستندات", "📊 التحليلات"],
            index=0,
            label_visibility="collapsed"
        )
    
    return page


# ============================================================
# 4. عرض معلومات المستخدم
# ============================================================

def render_user_info(
    username: Optional[str] = None,
    email: Optional[str] = None
) -> None:
    """
    عرض معلومات المستخدم في القائمة الجانبية
    
    Args:
        username: اسم المستخدم
        email: البريد الإلكتروني
    """
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 👤 المستخدم")
        
        if username:
            st.markdown(f"**{username}**")
        if email:
            st.caption(email)
        
        # زر تسجيل الخروج (اختياري)
        if st.button("🚪 تسجيل الخروج", use_container_width=True):
            # مسح الجلسة
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


# ============================================================
# 5. عرض شريط التقدم (Progress Bar)
# ============================================================

def render_progress_in_sidebar(
    progress: float,
    label: str = "جاري التحميل..."
) -> None:
    """
    عرض شريط تقدم في القائمة الجانبية
    
    Args:
        progress: نسبة التقدم (0-100)
        label: نص التقدم
    """
    with st.sidebar:
        st.progress(progress / 100)
        st.caption(f"{label} ({int(progress)}%)")


# ============================================================
# 6. عرض حالة النظام في القائمة الجانبية
# ============================================================

def render_system_status(
    status: str = "🟢 يعمل",
    uptime: str = "غير معروف"
) -> None:
    """
    عرض حالة النظام في القائمة الجانبية
    
    Args:
        status: حالة النظام
        uptime: مدة التشغيل
    """
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 🔧 حالة النظام")
        st.caption(f"الحالة: {status}")
        st.caption(f"مدة التشغيل: {uptime}")


# ============================================================
# 7. تصدير الدوال
# ============================================================

__all__ = [
    'render_sidebar',
    'render_stats_only',
    'render_navigation_only',
    'render_user_info',
    'render_progress_in_sidebar',
    'render_system_status'
]
