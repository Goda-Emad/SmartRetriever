# app/core/config.py
"""
⚙️ إعدادات التطبيق - Application Configuration

يقرأ الإعدادات من ملف .env ويوفرها للتطبيق
"""

import os
from pathlib import Path
from typing import List, Optional, Dict, Any
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()


class Settings:
    """
    إعدادات التطبيق
    
    يتم قراءة جميع الإعدادات من متغيرات البيئة
    """
    
    # ============================================================
    # 🔑 مفاتيح API
    # ============================================================
    
    # Grok API (xAI)
    GROK_API_KEY: str = os.getenv("GROK_API_KEY", "")
    GROK_MODEL: str = os.getenv("GROK_MODEL", "grok-1")
    GROK_API_URL: str = os.getenv(
        "GROK_API_URL",
        "https://api.x.ai/v1/chat/completions"
    )
    
    # ============================================================
    # 📁 مسارات الملفات
    # ============================================================
    
    # المسار الأساسي للمشروع
    BASE_DIR: Path = Path(__file__).parent.parent.parent
    
    # مجلدات التطبيق
    KNOWLEDGE_BASE_PATH: Path = Path(
        os.getenv("KNOWLEDGE_BASE_PATH", "./knowledge_base")
    )
    FAISS_INDEX_PATH: Path = Path(
        os.getenv("FAISS_INDEX_PATH", "./faiss_index")
    )
    DATA_PATH: Path = Path(
        os.getenv("DATA_PATH", "./data")
    )
    LOGS_PATH: Path = Path(
        os.getenv("LOGS_PATH", "./data/logs")
    )
    
    # ============================================================
    # 📊 إعدادات RAG
    # ============================================================
    
    DEFAULT_TOP_K: int = int(os.getenv("DEFAULT_TOP_K", "10"))
    DEFAULT_MAX_SOURCES: int = int(os.getenv("DEFAULT_MAX_SOURCES", "5"))
    DEFAULT_TEMPERATURE: float = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
    MIN_CONFIDENCE_SCORE: float = float(os.getenv("MIN_CONFIDENCE_SCORE", "0.3"))
    
    # إعدادات التقسيم (Chunking)
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "500"))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", "50"))
    MIN_CHUNK_SIZE: int = int(os.getenv("MIN_CHUNK_SIZE", "50"))
    
    # ============================================================
    # 🧬 إعدادات المتجهات (Embeddings)
    # ============================================================
    
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "paraphrase-multilingual-MiniLM-L12-v2"
    )
    EMBEDDING_DEVICE: str = os.getenv("EMBEDDING_DEVICE", "cpu")
    EMBEDDING_BATCH_SIZE: int = int(os.getenv("EMBEDDING_BATCH_SIZE", "32"))
    EMBEDDING_DIMENSION: int = int(os.getenv("EMBEDDING_DIMENSION", "384"))
    
    # ============================================================
    # 🖥️ إعدادات التطبيق
    # ============================================================
    
    APP_NAME: str = os.getenv("APP_NAME", "ProcureMind-AI")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # ============================================================
    # 📝 إعدادات التسجيل (Logging)
    # ============================================================
    
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = os.getenv(
        "LOG_FORMAT",
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )
    LOG_FILE: str = os.getenv("LOG_FILE", "data/logs/app.log")
    LOG_MAX_SIZE: int = int(os.getenv("LOG_MAX_SIZE", "10485760"))  # 10MB
    LOG_BACKUP_COUNT: int = int(os.getenv("LOG_BACKUP_COUNT", "5"))
    
    # ============================================================
    # 📄 إعدادات المستندات
    # ============================================================
    
    MAX_FILE_SIZE: int = int(os.getenv("MAX_FILE_SIZE", "10485760"))  # 10MB
    ALLOWED_EXTENSIONS: List[str] = os.getenv(
        "ALLOWED_EXTENSIONS",
        ".txt,.docx,.pdf"
    ).split(",")
    
    # ============================================================
    # 🔒 إعدادات الأمان (اختياري)
    # ============================================================
    
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    
    # معدل الطلبات (اختياري)
    RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", "100"))
    RATE_LIMIT_PERIOD: int = int(os.getenv("RATE_LIMIT_PERIOD", "60"))
    
    # ============================================================
    # 🧪 إعدادات الاختبار (اختياري)
    # ============================================================
    
    TESTING: bool = os.getenv("TESTING", "False").lower() == "true"
    
    # ============================================================
    # طرق مساعدة
    # ============================================================
    
    def is_production(self) -> bool:
        """التحقق من أن البيئة إنتاجية"""
        return self.ENVIRONMENT.lower() == "production"
    
    def is_development(self) -> bool:
        """التحقق من أن البيئة تطويرية"""
        return self.ENVIRONMENT.lower() == "development"
    
    def is_testing(self) -> bool:
        """التحقق من أن البيئة اختبارية"""
        return self.TESTING or self.ENVIRONMENT.lower() == "testing"
    
    def get_allowed_extensions(self) -> List[str]:
        """الحصول على قائمة الامتدادات المسموحة"""
        return [ext.strip().lower() for ext in self.ALLOWED_EXTENSIONS if ext.strip()]
    
    def get_embedding_config(self) -> Dict[str, Any]:
        """الحصول على إعدادات المتجهات"""
        return {
            "model_name": self.EMBEDDING_MODEL,
            "device": self.EMBEDDING_DEVICE,
            "batch_size": self.EMBEDDING_BATCH_SIZE,
            "dimension": self.EMBEDDING_DIMENSION
        }
    
    def get_rag_config(self) -> Dict[str, Any]:
        """الحصول على إعدادات RAG"""
        return {
            "top_k": self.DEFAULT_TOP_K,
            "max_sources": self.DEFAULT_MAX_SOURCES,
            "temperature": self.DEFAULT_TEMPERATURE,
            "min_confidence": self.MIN_CONFIDENCE_SCORE,
            "chunk_size": self.CHUNK_SIZE,
            "chunk_overlap": self.CHUNK_OVERLAP
        }
    
    def get_llm_config(self) -> Dict[str, Any]:
        """الحصول على إعدادات النموذج اللغوي"""
        return {
            "api_key": self.GROK_API_KEY,
            "model": self.GROK_MODEL,
            "api_url": self.GROK_API_URL
        }
    
    def get_paths(self) -> Dict[str, Path]:
        """الحصول على جميع مسارات الملفات"""
        return {
            "base": self.BASE_DIR,
            "knowledge_base": self.KNOWLEDGE_BASE_PATH,
            "faiss_index": self.FAISS_INDEX_PATH,
            "data": self.DATA_PATH,
            "logs": self.LOGS_PATH
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل جميع الإعدادات إلى قاموس"""
        return {
            # مفاتيح API
            "GROK_API_KEY": "***" if self.GROK_API_KEY else "",
            "GROK_MODEL": self.GROK_MODEL,
            "GROK_API_URL": self.GROK_API_URL,
            
            # المسارات
            "KNOWLEDGE_BASE_PATH": str(self.KNOWLEDGE_BASE_PATH),
            "FAISS_INDEX_PATH": str(self.FAISS_INDEX_PATH),
            "DATA_PATH": str(self.DATA_PATH),
            "LOGS_PATH": str(self.LOGS_PATH),
            
            # إعدادات RAG
            "DEFAULT_TOP_K": self.DEFAULT_TOP_K,
            "DEFAULT_MAX_SOURCES": self.DEFAULT_MAX_SOURCES,
            "DEFAULT_TEMPERATURE": self.DEFAULT_TEMPERATURE,
            "MIN_CONFIDENCE_SCORE": self.MIN_CONFIDENCE_SCORE,
            "CHUNK_SIZE": self.CHUNK_SIZE,
            "CHUNK_OVERLAP": self.CHUNK_OVERLAP,
            
            # إعدادات المتجهات
            "EMBEDDING_MODEL": self.EMBEDDING_MODEL,
            "EMBEDDING_DEVICE": self.EMBEDDING_DEVICE,
            "EMBEDDING_BATCH_SIZE": self.EMBEDDING_BATCH_SIZE,
            "EMBEDDING_DIMENSION": self.EMBEDDING_DIMENSION,
            
            # إعدادات التطبيق
            "APP_NAME": self.APP_NAME,
            "APP_VERSION": self.APP_VERSION,
            "ENVIRONMENT": self.ENVIRONMENT,
            "DEBUG": self.DEBUG,
            
            # إعدادات المستندات
            "MAX_FILE_SIZE": self.MAX_FILE_SIZE,
            "ALLOWED_EXTENSIONS": self.ALLOWED_EXTENSIONS,
            
            # إعدادات التسجيل
            "LOG_LEVEL": self.LOG_LEVEL,
            "LOG_FILE": self.LOG_FILE,
        }


# ============================================================
# إنشاء كائن الإعدادات
# ============================================================

settings = Settings()


# ============================================================
# التحقق من الإعدادات عند بدء التشغيل
# ============================================================

def validate_settings():
    """
    التحقق من صحة الإعدادات عند بدء التشغيل
    """
    # التحقق من وجود مفتاح Grok
    if not settings.GROK_API_KEY:
        print("⚠️ تحذير: GROK_API_KEY غير موجود في ملف .env")
        print("   يرجى إضافة المفتاح لتشغيل النموذج اللغوي")
    
    # التحقق من وجود مجلدات
    directories = [
        settings.KNOWLEDGE_BASE_PATH,
        settings.FAISS_INDEX_PATH,
        settings.DATA_PATH,
        settings.LOGS_PATH
    ]
    
    for dir_path in directories:
        if not dir_path.exists():
            print(f"📁 إنشاء مجلد: {dir_path}")
            dir_path.mkdir(parents=True, exist_ok=True)
    
    # التحقق من بيئة التشغيل
    if settings.is_production():
        print("🚀 تشغيل في بيئة إنتاجية")
    elif settings.is_development():
        print("🛠️ تشغيل في بيئة تطويرية")
    elif settings.is_testing():
        print("🧪 تشغيل في بيئة اختبارية")
    
    print(f"📦 {settings.APP_NAME} v{settings.APP_VERSION}")


# تشغيل التحقق عند بدء التشغيل
validate_settings()
