# app/services/__init__.py
"""
🔧 وحدة الخدمات - Services Module

تحتوي على جميع خدمات التطبيق (منطق الأعمال)
"""

from .chat_service import ChatService

# تعريف ما يتم تصديره عند استيراد الوحدة
__all__ = [
    'ChatService'
]

# معلومات الوحدة
__version__ = "1.0.0"
__description__ = "ProcureMind-AI Services Module - منطق الأعمال"

# وصف الخدمات
SERVICES = {
    "chat_service": "خدمة المحادثة - إدارة RAG والرد على الأسئلة"
}

# إعدادات الخدمات
SERVICE_DEFAULTS = {
    "chat": {
        "max_history": 50,
        "default_temperature": 0.7,
        "default_top_k": 5
    }
}
