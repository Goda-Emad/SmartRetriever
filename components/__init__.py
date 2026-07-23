# app/components/__init__.py
"""
🧩 مكونات مشتركة - Shared Components

تحتوي على مكونات قابلة لإعادة الاستخدام في جميع أنحاء التطبيق
"""

from .sidebar import render_sidebar
from .chat_utils import (
    render_chat_message,
    render_sources,
    render_suggested_questions,
    render_chat_input
)

# تعريف ما يتم تصديره عند استيراد الوحدة
__all__ = [
    # القائمة الجانبية
    'render_sidebar',
    
    # أدوات المحادثة
    'render_chat_message',
    'render_sources',
    'render_suggested_questions',
    'render_chat_input'
]

# معلومات الوحدة
__version__ = "1.0.0"
__description__ = "ProcureMind-AI Components - مكونات مشتركة للتطبيق"

# قائمة المكونات المتاحة
COMPONENTS = {
    "sidebar": "القائمة الجانبية للتطبيق",
    "chat_message": "عرض رسالة في المحادثة",
    "sources": "عرض المصادر",
    "suggested_questions": "عرض الأسئلة المقترحة",
    "chat_input": "مدخل النص للمحادثة"
}
