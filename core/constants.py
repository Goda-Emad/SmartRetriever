"""
📌 الثوابت الأساسية - Application Constants
"""

APP_NAME = "SmartRetriever"
APP_VERSION = "1.0.0"

SUPPORTED_FILE_TYPES = [".txt", ".docx", ".pdf"]
FILE_EXTENSIONS = SUPPORTED_FILE_TYPES
ALLOWED_EXTENSIONS = SUPPORTED_FILE_TYPES

DEFAULT_CHUNK_SIZE = 500
DEFAULT_TOP_K = 10
DEFAULT_MAX_SOURCES = 5
DEFAULT_TEMPERATURE = 0.7
MIN_CONFIDENCE_SCORE = 0.3

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

CATEGORIES = {
    "contracts": "العقود",
    "policies": "السياسات",
    "quality_reports": "تقارير الجودة",
    "quotations": "عروض الأسعار"
}
