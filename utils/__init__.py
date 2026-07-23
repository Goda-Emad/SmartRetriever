# app/utils/__init__.py
"""
🛠️ وحدة الأدوات المساعدة - Utils Module

تحتوي على أدوات ووظائف مساعدة تستخدم في جميع أنحاء التطبيق
"""

from .logger import logger, setup_logging
from .file_utils import (
    FileUtils,
    get_file_extension,
    get_file_name,
    get_file_size,
    format_file_size,
    is_file_allowed,
    read_text_file,
    write_text_file,
    create_directory,
    delete_file,
    get_file_hash,
    get_file_info,
    list_files,
    get_available_space,
    safe_filename,
    get_unique_filename
)

# تعريف ما يتم تصديره عند استيراد الوحدة
__all__ = [
    # التسجيل
    'logger',
    'setup_logging',
    
    # أدوات الملفات
    'FileUtils',
    'get_file_extension',
    'get_file_name',
    'get_file_size',
    'format_file_size',
    'is_file_allowed',
    'read_text_file',
    'write_text_file',
    'create_directory',
    'delete_file',
    'get_file_hash',
    'get_file_info',
    'list_files',
    'get_available_space',
    'safe_filename',
    'get_unique_filename'
]

# معلومات الوحدة
__version__ = "1.0.0"
__description__ = "ProcureMind-AI Utils Module - أدوات ووظائف مساعدة"

# قائمة الأدوات المتاحة
UTILS_LIST = {
    "logger": "نظام التسجيل وإدارة السجلات",
    "file_utils": "أدوات التعامل مع الملفات"
}
