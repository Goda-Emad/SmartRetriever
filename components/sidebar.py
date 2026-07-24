"""
📌 القائمة الجانبية - Professional Sidebar Component
تصميم عصري مستوحى من Saudi Tourism Intelligence UI
"""

import streamlit as st
from typing import Optional, Dict, Any

# ============================================================
# ⚙️ إعدادات الصفحات والأيقونات (SVG)
# ============================================================

# SVG Icons (بدون إيموجي)
ICONS = {
    "dashboard": """
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="3" y="3" width="7" height="7" rx="1"/>
        <rect x="14" y="3" width="7" height="7" rx="1"/>
        <rect x="3" y="14" width="7" height="7" rx="1"/>
        <rect x="14" y="14" width="7" height="7" rx="1"/>
    </svg>
    """,
    "documents": """
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
        <line x1="16" y1="13" x2="8" y2="13"/>
        <line x1="16" y1="17" x2="8" y2="17"/>
        <polyline points="10 9 9 9 8 9"/>
    </svg>
    """,
    "contracts": """
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
        <line x1="16" y1="13" x2="8" y2="13"/>
        <line x1="16" y1="17" x2="8" y2="17"/>
        <polyline points="10 9 9 9 8 9"/>
    </svg>
    """,
    "suppliers": """
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
        <circle cx="9" cy="7" r="4"/>
        <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
        <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
    </svg>
    """,
    "quality": """
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
    </svg>
    """,
    "chat": """
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
    </svg>
    """,
    "analytics": """
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
    </svg>
    """,
    "settings": """
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="3"/>
        <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>
    </svg>
    """,
}

# الصفحات
PAGES = {
    "dashboard": {"ar": "لوحة التحكم", "icon": "dashboard"},
    "documents": {"ar": "المستندات", "icon": "documents"},
    "contracts": {"ar": "العقود", "icon": "contracts"},
    "suppliers": {"ar": "الموردين", "icon": "suppliers"},
    "quality": {"ar": "تقارير الجودة", "icon": "quality"},
    "chat": {"ar": "المحادثات", "icon": "chat"},
    "analytics": {"ar": "التحليلات", "icon": "analytics"},
}
DEFAULT_PAGE = "dashboard"


# ============================================================
# 🎨 تنسيقات CSS
# ============================================================

def _inject_css():
    """حقن التنسيقات المخصصة"""
    st.markdown("""
    <style>
    /* ============================================================
       SIDEBAR MAIN
       ============================================================ */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0c0f1e 0%, #0f172a 50%, #0c0f1e 100%) !important;
        border-right: 1px solid rgba(255,255,255,0.04) !important;
        padding: 1.2rem 0.5rem !important;
    }
    
    /* ============================================================
       SIDEBAR BUTTONS (Nav Items)
       ============================================================ */
    .stSidebar .stButton button {
        width: 100% !important;
        background: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 1rem !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        text-align: right !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        gap: 0.8rem !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
        position: relative !important;
    }
    
    .stSidebar .stButton button:hover {
        background: rgba(255,255,255,0.05) !important;
        color: #f1f5f9 !important;
    }
    
    .stSidebar .stButton button[kind="primary"] {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(124, 58, 237, 0.10)) !important;
        color: #60a5fa !important;
        border: 1px solid rgba(59, 130, 246, 0.2) !important;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.05) !important;
    }
    
    .stSidebar .stButton button[kind="primary"]::before {
        content: '';
        position: absolute;
        right: -0.5rem;
        top: 50%;
        transform: translateY(-50%);
        width: 3px;
        height: 24px;
        background: linear-gradient(180deg, #3b82f6, #8b5cf6);
        border-radius: 0 4px 4px 0;
    }
    
    .stSidebar .stButton button[kind="primary"]:hover {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.25), rgba(124, 58, 237, 0.18)) !important;
        box-shadow: 0 0 30px rgba(59, 130, 246, 0.10) !important;
    }
    
    /* ============================================================
       SVG ICONS in buttons
       ============================================================ */
    .stSidebar .stButton button svg {
        width: 18px !important;
        height: 18px !important;
        flex-shrink: 0 !important;
        stroke-width: 1.8 !important;
    }
    
    .stSidebar .stButton button[kind="primary"] svg {
        stroke: #60a5fa !important;
    }
    
    .stSidebar .stButton button:hover svg {
        stroke: #f1f5f9 !important;
    }
    
    /* ============================================================
       APP HEADER
       ============================================================ */
    .sidebar-header {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        padding: 0.3rem 0.5rem 1rem 0.5rem;
        border-bottom: 1px solid rgba(255,255,255,0.04);
        margin-bottom: 0.8rem;
    }
    
    .sidebar-header .logo {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        font-weight: 800;
        color: white;
        flex-shrink: 0;
    }
    
    .sidebar-header .title {
        font-size: 1rem;
        font-weight: 800;
        color: #f1f5f9;
        letter-spacing: -0.3px;
        line-height: 1.2;
    }
    
    .sidebar-header .badge {
        font-size: 0.5rem;
        font-weight: 700;
        color: #94a3b8;
        background: rgba(255,255,255,0.06);
        padding: 0.1rem 0.5rem;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.06);
        letter-spacing: 0.5px;
    }
    
    .sidebar-header .subtitle {
        font-size: 0.6rem;
        color: #38bdf8;
        font-weight: 600;
        letter-spacing: 1px;
    }
    
    /* ============================================================
       THEME TOGGLE
       ============================================================ */
    .theme-toggle-container {
        display: flex;
        background: rgba(255,255,255,0.04);
        border-radius: 12px;
        padding: 0.2rem;
        margin-bottom: 0.8rem;
        border: 1px solid rgba(255,255,255,0.05);
    }
    
    .theme-toggle-container .toggle-btn {
        flex: 1;
        padding: 0.35rem 0.3rem;
        border: none;
        border-radius: 10px;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.7rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        color: #94a3b8;
        background: transparent;
        text-align: center;
    }
    
    .theme-toggle-container .toggle-btn.active {
        background: #1e293b;
        color: #f1f5f9;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    
    .theme-toggle-container .toggle-btn:hover:not(.active) {
        color: #f1f5f9;
    }
    
    /* ============================================================
       KPI CARDS
       ============================================================ */
    .kpi-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.4rem;
        margin: 0.8rem 0 0.3rem 0;
        padding: 0.5rem;
        background: rgba(255,255,255,0.02);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.04);
    }
    
    .kpi-card {
        text-align: center;
        padding: 0.3rem 0.1rem;
        border-radius: 8px;
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.04);
    }
    
    .kpi-card .label {
        font-size: 0.5rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.3px;
    }
    
    .kpi-card .value {
        font-size: 1rem;
        font-weight: 800;
        color: #f1f5f9;
        line-height: 1.3;
    }
    
    .kpi-card .value.highlight {
        color: #10b981;
    }
    
    /* ============================================================
       FOOTER
       ============================================================ */
    .sidebar-footer {
        margin-top: auto;
        padding-top: 0.8rem;
        border-top: 1px solid rgba(255,255,255,0.04);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .sidebar-footer .footer-text {
        font-size: 0.55rem;
        color: #475569;
    }
    
    .sidebar-footer .footer-links {
        display: flex;
        gap: 0.5rem;
        align-items: center;
    }
    
    .sidebar-footer .footer-links a {
        font-size: 0.6rem;
        color: #475569;
        text-decoration: none;
        transition: color 0.2s;
    }
    
    .sidebar-footer .footer-links a:hover {
        color: #94a3b8;
    }
    
    /* ============================================================
       SCROLLBAR
       ============================================================ */
    [data-testid="stSidebar"]::-webkit-scrollbar {
        width: 3px;
    }
    [data-testid="stSidebar"]::-webkit-scrollbar-track {
        background: transparent;
    }
    [data-testid="stSidebar"]::-webkit-scrollbar-thumb {
        background: #334155;
        border-radius: 10px;
    }
    [data-testid="stSidebar"]::-webkit-scrollbar-thumb:hover {
        background: #3b82f6;
    }
    </style>
    """, unsafe_allow_html=True)


# ============================================================
# 🏗️ دالة عرض القائمة الجانبية
# ============================================================

def render_sidebar(
    stats: Optional[Dict[str, Any]] = None,
    show_theme_toggle: bool = True,
    show_stats: bool = True,
    show_navigation: bool = True
) -> str:
    """عرض القائمة الجانبية الاحترافية"""
    
    # حقن التنسيقات
    _inject_css()
    
    # تهيئة حالة الجلسة
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = DEFAULT_PAGE
    
    if "current_lang" not in st.session_state:
        st.session_state.current_lang = "ar"
    
    with st.sidebar:
        
        # ============================================================
        # 1. الهيدر (الشعار + الاسم)
        # ============================================================
        st.markdown(f"""
        <div class="sidebar-header">
            <div class="logo">S</div>
            <div>
                <div class="title">SmartRetriever</div>
                <div style="display: flex; align-items: center; gap: 0.4rem; margin-top: 1px;">
                    <span class="badge">v1.0.0 Pro</span>
                    <span class="subtitle">● {st.session_state.current_lang.upper()}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # ============================================================
        # 2. زر تبديل الوضع (Theme Toggle)
        # ============================================================
        if show_theme_toggle:
            st.markdown(f"""
            <div class="theme-toggle-container">
                <button class="toggle-btn {'active' if st.session_state.dark_mode else ''}" 
                        onclick="(function(){{ 
                            var btn = this; 
                            var val = {'false' if st.session_state.dark_mode else 'true'};
                            btn.closest('.theme-toggle-container').querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
                            btn.classList.add('active');
                        }})()" 
                        style="cursor:pointer;">
                    🌙 داكن
                </button>
                <button class="toggle-btn {'active' if not st.session_state.dark_mode else ''}" 
                        onclick="(function(){{ 
                            var btn = this; 
                            var val = {'false' if not st.session_state.dark_mode else 'true'};
                            btn.closest('.theme-toggle-container').querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
                            btn.classList.add('active');
                        }})()"
                        style="cursor:pointer;">
                    ☀️ فاتح
                </button>
            </div>
            """, unsafe_allow_html=True)
            
            # زر Streamlit الفعلي للتبديل (مخفي)
            theme_label = "dark" if st.session_state.dark_mode else "light"
            if st.button(f"🌙 {theme_label}", key="_theme_hidden", use_container_width=True, type="secondary"):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()
            
            # إخفاء زر Streamlit الأصلي
            st.markdown("""
            <style>
            .stSidebar .stButton button[key="_theme_hidden"] {
                display: none !important;
            }
            </style>
            """, unsafe_allow_html=True)
        
        # ============================================================
        # 3. قائمة التنقل
        # ============================================================
        if show_navigation:
            for page_key, page_info in PAGES.items():
                is_active = (st.session_state.current_page == page_key)
                label = page_info["ar"]
                icon_svg = ICONS.get(page_info["icon"], "")
                
                # زر الصفحة مع SVG
                if st.button(
                    f"{icon_svg} {label}",
                    use_container_width=True,
                    key=f"nav_{page_key}",
                    type="primary" if is_active else "secondary"
                ):
                    st.session_state.current_page = page_key
                    st.rerun()
        
        # ============================================================
        # 4. KPI الإحصائيات
        # ============================================================
        if show_stats and stats:
            st.markdown('<div class="kpi-grid">', unsafe_allow_html=True)
            
            kpis = [
                ("📄 مستندات", stats.get("documents", 0), ""),
                ("🏢 موردين", stats.get("suppliers", 0), ""),
                ("📝 عقود", stats.get("contracts", 0), ""),
                ("⭐ جودة", stats.get("quality", 0), "highlight"),
            ]
            
            for label, value, cls in kpis:
                st.markdown(f"""
                <div class="kpi-card">
                    <div class="label">{label}</div>
                    <div class="value {cls}">{value}{'%' if 'جودة' in label else ''}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # ============================================================
        # 5. الفوتر
        # ============================================================
        st.markdown("""
        <div class="sidebar-footer">
            <span class="footer-text">© 2026 SmartRetriever</span>
            <div class="footer-links">
                <a href="#">GitHub</a>
                <span style="color:#334155;">·</span>
                <a href="#">LinkedIn</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    return st.session_state.get("current_page", DEFAULT_PAGE)


# ============================================================
# ✅ دوال مساعدة (للتوافق مع الكود القديم)
# ============================================================

def render_stats_only(stats: Dict[str, Any]) -> None:
    """عرض الإحصائيات فقط في السايدبار"""
    with st.sidebar:
        _inject_css()
        st.markdown("### 📊 الإحصائيات")
        for k, v in stats.items():
            st.metric(k, v)


def render_navigation_only() -> str:
    """عرض التنقل فقط"""
    return render_sidebar(show_stats=False, show_theme_toggle=False)


def render_user_info(username: Optional[str] = None, email: Optional[str] = None) -> None:
    """عرض معلومات المستخدم"""
    with st.sidebar:
        _inject_css()
        if username:
            st.markdown(f"### 👤 {username}")
        if email:
            st.caption(email)


def render_progress_in_sidebar(progress: float, label: str = "جاري التحميل...") -> None:
    """عرض شريط تقدم في السايدبار"""
    with st.sidebar:
        st.progress(min(max(progress / 100, 0.0), 1.0))
        st.caption(f"{label} ({int(progress)}%)")


def render_system_status(status: str = "🟢 يعمل", uptime: str = "غير معروف") -> None:
    """عرض حالة النظام"""
    with st.sidebar:
        st.caption(f"الحالة: {status} | مدة التشغيل: {uptime}")


# ============================================================
# 📤 التصدير
# ============================================================

__all__ = [
    'render_sidebar',
    'render_stats_only',
    'render_navigation_only',
    'render_user_info',
    'render_progress_in_sidebar',
    'render_system_status',
]
