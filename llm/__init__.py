"""
🤖 وحدة LLM (Large Language Models)

تحتوي على جميع مكونات التواصل مع النماذج اللغوية الكبيرة
"""

from .groq_client import GroqClient

# تعريف ما يتم تصديره عند استيراد الوحدة
__all__ = [
    'GroqClient'
]

# معلومات الوحدة
__version__ = "1.0.0"
__description__ = "ProcureMind-AI LLM Module - التواصل مع النماذج اللغوية"

# قائمة النماذج المدعومة
SUPPORTED_MODELS = {
    "groq": {
        "name": "Groq",
        "provider": "Groq",
        "default_model": "llama-3.3-70b-versatile",
        "description": "نموذج Llama عبر منصة Groq"
    }
}

# وصف المكونات
COMPONENTS = {
    "groq_client": "عميل Groq API"
}
