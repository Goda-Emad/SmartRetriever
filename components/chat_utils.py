# app/components/chat_utils.py
"""
💬 أدوات المحادثة - Chat Utilities

تحتوي على دوال مساعدة لعرض مكونات المحادثة في Streamlit
"""

import streamlit as st
from typing import List, Dict, Any, Optional
import time


# ============================================================
# 1. عرض رسالة في المحادثة
# ============================================================

def render_chat_message(
    message: Dict[str, Any],
    is_last: bool = False,
    show_sources: bool = True
) -> None:
    """
    عرض رسالة واحدة في المحادثة
    
    Args:
        message: بيانات الرسالة (role, content, sources)
        is_last: هل هي آخر رسالة
        show_sources: عرض المصادر
    """
    role = message.get("role", "user")
    content = message.get("content", "")
    sources = message.get("sources", [])
    
    # عرض الرسالة في فقاعة المحادثة
    with st.chat_message(role):
        st.markdown(content)
        
        # عرض المصادر
        if show_sources and sources and role == "assistant":
            render_sources(sources)


def render_messages(
    messages: List[Dict[str, Any]],
    show_sources: bool = True
) -> None:
    """
    عرض جميع الرسائل في المحادثة
    
    Args:
        messages: قائمة الرسائل
        show_sources: عرض المصادر
    """
    for i, message in enumerate(messages):
        is_last = (i == len(messages) - 1)
        render_chat_message(message, is_last, show_sources)


# ============================================================
# 2. عرض المصادر
# ============================================================

def render_sources(sources: List[Dict[str, Any]]) -> None:
    """
    عرض المصادر المستخدمة في الإجابة
    
    Args:
        sources: قائمة المصادر
    """
    if not sources:
        return
    
    with st.expander(f"📎 المصادر ({len(sources)})"):
        for i, source in enumerate(sources, 1):
            # معلومات المصدر
            filename = source.get("filename", "مصدر غير معروف")
            score = source.get("relevance_score", 0)
            content = source.get("content", "")
            category = source.get("category", "غير مصنف")
            
            # عرض بطاقة المصدر
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"**{i}. {filename}**")
                st.caption(f"📂 {category}")
                if content:
                    preview = content[:200] + "..." if len(content) > 200 else content
                    st.text(preview)
            
            with col2:
                # درجة المطابقة
                score_percent = int(score * 100)
                if score_percent >= 80:
                    color = "🟢"
                elif score_percent >= 50:
                    color = "🟡"
                else:
                    color = "🔴"
                st.metric("المطابقة", f"{color} {score_percent}%")
            
            st.divider()


# ============================================================
# 3. عرض الأسئلة المقترحة
# ============================================================

def render_suggested_questions(
    questions: List[str],
    on_click: Optional[callable] = None,
    cols: int = 2
) -> None:
    """
    عرض الأسئلة المقترحة
    
    Args:
        questions: قائمة الأسئلة
        on_click: دالة عند النقر على سؤال
        cols: عدد الأعمدة
    """
    if not questions:
        return
    
    st.markdown("### 💡 أسئلة مقترحة")
    
    # تقسيم الأسئلة على أعمدة
    columns = st.columns(cols)
    
    for i, question in enumerate(questions):
        with columns[i % cols]:
            if st.button(question, use_container_width=True, key=f"suggested_{i}"):
                if on_click:
                    on_click(question)


# ============================================================
# 4. عرض مدخل النص
# ============================================================

def render_chat_input(
    placeholder: str = "اكتب سؤالك هنا...",
    disabled: bool = False,
    key: str = "chat_input"
) -> Optional[str]:
    """
    عرض مدخل النص للمحادثة
    
    Args:
        placeholder: النص الظاهر في المدخل
        disabled: تعطيل المدخل
        key: مفتاح فريد للمدخل
        
    Returns:
        النص المدخل أو None
    """
    return st.chat_input(
        placeholder=placeholder,
        disabled=disabled,
        key=key
    )


# ============================================================
# 5. عرض مؤشر التحميل
# ============================================================

def render_loading_indicator(message: str = "🤔 جاري البحث والتفكير...") -> None:
    """
    عرض مؤشر التحميل
    
    Args:
        message: رسالة التحميل
    """
    with st.spinner(message):
        time.sleep(0.5)  # لإعطاء تأثير بصري


# ============================================================
# 6. عرض حالة خطأ
# ============================================================

def render_error(message: str) -> None:
    """
    عرض رسالة خطأ
    
    Args:
        message: رسالة الخطأ
    """
    st.error(f"❌ {message}")


# ============================================================
# 7. عرض حالة نجاح
# ============================================================

def render_success(message: str) -> None:
    """
    عرض رسالة نجاح
    
    Args:
        message: رسالة النجاح
    """
    st.success(f"✅ {message}")


# ============================================================
# 8. عرض حالة تحذير
# ============================================================

def render_warning(message: str) -> None:
    """
    عرض رسالة تحذير
    
    Args:
        message: رسالة التحذير
    """
    st.warning(f"⚠️ {message}")


# ============================================================
# 9. عرض معلومات
# ============================================================

def render_info(message: str) -> None:
    """
    عرض رسالة معلومات
    
    Args:
        message: رسالة المعلومات
    """
    st.info(f"ℹ️ {message}")


# ============================================================
# 10. عرض بطاقة المصدر (نسخة مبسطة)
# ============================================================

def render_source_card(source: Dict[str, Any]) -> None:
    """
    عرض بطاقة مصدر واحدة (نسخة مبسطة)
    
    Args:
        source: بيانات المصدر
    """
    filename = source.get("filename", "مصدر غير معروف")
    score = source.get("relevance_score", 0)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**{filename}**")
    with col2:
        st.caption(f"{int(score * 100)}% مطابقة")


# ============================================================
# 11. عرض تقدم المعالجة
# ============================================================

def render_progress(progress: float, text: str = "جاري المعالجة...") -> None:
    """
    عرض شريط تقدم
    
    Args:
        progress: نسبة التقدم (0-100)
        text: نص التقدم
    """
    st.progress(progress / 100)
    st.caption(f"{text} ({int(progress)}%)")


# ============================================================
# 12. تنسيق النص
# ============================================================

def format_message_content(content: str) -> str:
    """
    تنسيق محتوى الرسالة (إضافة تنسيقات Markdown)
    
    Args:
        content: النص الأصلي
        
    Returns:
        النص المنسق
    """
    if not content:
        return ""
    
    # إضافة تنسيق للعناوين
    lines = content.split("\n")
    formatted = []
    
    for line in lines:
        # العناوين
        if line.startswith("## "):
            formatted.append(f"### {line[3:]}")
        elif line.startswith("### "):
            formatted.append(f"#### {line[4:]}")
        # النقاط
        elif line.startswith("- "):
            formatted.append(f"• {line[2:]}")
        elif line.startswith("* "):
            formatted.append(f"• {line[2:]}")
        # الأرقام
        elif line[0].isdigit() and "." in line[:3]:
            formatted.append(line)
        else:
            formatted.append(line)
    
    return "\n".join(formatted)


# ============================================================
# 13. تصدير الدوال
# ============================================================

__all__ = [
    'render_chat_message',
    'render_messages',
    'render_sources',
    'render_suggested_questions',
    'render_chat_input',
    'render_loading_indicator',
    'render_error',
    'render_success',
    'render_warning',
    'render_info',
    'render_source_card',
    'render_progress',
    'format_message_content'
]
