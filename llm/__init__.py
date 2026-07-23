# app/llm/__init__.py
"""
🤖 وحدة LLM (Large Language Models)

تحتوي على جميع مكونات التواصل مع النماذج اللغوية الكبيرة
"""

from .grok_client import GrokClient

# تعريف ما يتم تصديره عند استيراد الوحدة
__all__ = [
    'GrokClient'
]

# معلومات الوحدة
__version__ = "1.0.0"
__description__ = "ProcureMind-AI LLM Module - التواصل مع النماذج اللغوية"

# قائمة النماذج المدعومة
SUPPORTED_MODELS = {
    "grok": {
        "name": "Grok",
        "provider": "xAI",
        "default_model": "grok-1",
        "description": "نموذج Grok من xAI"
    }
}

# وصف المكونات
COMPONENTS = {
    "grok_client": "عميل Grok API من xAI"
}
