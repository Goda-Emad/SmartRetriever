# components/__init__.py
"""
🧩 مكونات مشتركة - Shared Components
مكونات قابلة لإعادة الاستخدام في جميع أنحاء التطبيق
"""

from .sidebar import (
    render_sidebar,
    render_stats_only,
    render_navigation_only,
    render_user_info,
    render_progress_in_sidebar,
    render_system_status,
)

from .chat_utils import (
    render_chat_message,
    render_messages,
    render_sources,
    render_suggested_questions,
    render_chat_input,
    render_loading_indicator,
    render_error,
    render_success,
    render_warning,
    render_info,
    render_source_card,
    render_progress,
    format_message_content,
)

__all__ = [
    # sidebar
    'render_sidebar',
    'render_stats_only',
    'render_navigation_only',
    'render_user_info',
    'render_progress_in_sidebar',
    'render_system_status',
    # chat_utils
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
    'format_message_content',
]

__version__ = "1.0.0"
__description__ = "SmartRetriever Components - مكونات مشتركة"
