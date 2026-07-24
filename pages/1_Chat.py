"""
💬 صفحة المحادثة - Chat Page

الصفحة الرئيسية للمحادثة مع الذكاء الاصطناعي
"""

import streamlit as st
import sys
from pathlib import Path

# إضافة المجلد الحالي إلى المسار
sys.path.append(str(Path(__file__).parent.parent))

# استيراد الخدمات والمكونات
from services.chat_service import ChatService
from components.chat_utils import (
    render_sources,
    render_suggested_questions,
    render_error,
    render_loading_indicator
)
from core.config import settings
from utils.logger import logger


# ============================================================
# 1. تهيئة خدمة المحادثة
# ============================================================

@st.cache_resource
def get_chat_service():
    """تهيئة خدمة المحادثة (مرة واحدة)"""
    return ChatService()

chat_service = get_chat_service()


# ============================================================
# 2. تهيئة حالة الجلسة
# ============================================================

def init_session_state():
    """تهيئة حالة الجلسة"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "session_id" not in st.session_state:
        import uuid
        st.session_state.session_id = str(uuid.uuid4())
    
    if "is_processing" not in st.session_state:
        st.session_state.is_processing = False


# ============================================================
# 3. عرض الرسائل
# ============================================================

def display_messages():
    """عرض جميع الرسائل في المحادثة"""
    for message in st.session_state.messages:
        role = message.get("role", "user")
        content = message.get("content", "")
        sources = message.get("sources", [])
        
        with st.chat_message(role):
            st.markdown(content)
            
            # عرض المصادر إذا كانت موجودة
            if sources and role == "assistant":
                render_sources(sources)


# ============================================================
# 4. معالجة السؤال
# ============================================================

def process_question(question: str):
    """
    معالجة سؤال المستخدم
    
    Args:
        question: سؤال المستخدم
    """
    # إضافة رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": question})
    
    # عرض رسالة المستخدم
    with st.chat_message("user"):
        st.markdown(question)
    
    # توليد الرد
    with st.chat_message("assistant"):
        with st.spinner("🤔 جاري البحث والتفكير..."):
            try:
                # ✅ استدعاء الدالة المتزامنة بدلاً من غير المتزامنة
                response = chat_service.process_question_sync(
                    question=question,
                    session_id=st.session_state.session_id
                )
                
                # حفظ session_id
                if not st.session_state.session_id:
                    st.session_state.session_id = response["session_id"]
                
                # عرض الإجابة
                st.markdown(response["answer"])
                
                # عرض المصادر
                if response.get("sources"):
                    render_sources(response["sources"])
                
                # حفظ الرسالة
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response["answer"],
                    "sources": response.get("sources", [])
                })
                
            except Exception as e:
                error_msg = f"❌ حدث خطأ: {str(e)}"
                st.error(error_msg)
                logger.error(f"Error processing question: {str(e)}")
                
                # حفظ رسالة الخطأ
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })


# ============================================================
# 5. عرض الأسئلة المقترحة
# ============================================================

def display_suggested_questions():
    """عرض الأسئلة المقترحة"""
    if len(st.session_state.messages) > 0:
        return
    
    st.markdown("---")
    
    suggestions = [
        "ما هي شروط عقد Alpha Inc؟",
        "مين أفضل مورد حسب تقارير الجودة؟",
        "إيه سياسة تقييم الموردين؟",
        "قارن بين عروض أسعار Alpha Inc و Beta Supplies",
        "ما هي قيمة عقد Gamma Co؟",
        "تقرير جودة Delta Logistics"
    ]
    
    st.markdown("### 💡 أسئلة مقترحة")
    
    cols = st.columns(2)
    for i, suggestion in enumerate(suggestions):
        with cols[i % 2]:
            if st.button(suggestion, use_container_width=True, key=f"suggested_{i}"):
                process_question(suggestion)
                st.rerun()


# ============================================================
# 6. الصفحة الرئيسية
# ============================================================

def show():
    """عرض صفحة المحادثة"""
    
    # تهيئة حالة الجلسة
    init_session_state()
    
    # ============================================================
    # رأس الصفحة
    # ============================================================
    
    st.title("💬 محادثة ProcureMind")
    st.caption("اسأل عن أي شيء في المستندات (عقود، موردين، سياسات، تقارير جودة)")
    
    # أزرار التحكم
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col2:
        if st.button("🗑️ مسح المحادثة", use_container_width=True):
            st.session_state.messages = []
            st.session_state.session_id = None
            st.rerun()
    
    with col3:
        if st.button("🔄 تحديث", use_container_width=True):
            st.rerun()
    
    st.divider()
    
    # ============================================================
    # عرض الرسائل
    # ============================================================
    
    display_messages()
    
    # ============================================================
    # مدخل النص
    # ============================================================
    
    if prompt := st.chat_input("اكتب سؤالك هنا..."):
        process_question(prompt)
        st.rerun()
    
    # ============================================================
    # الأسئلة المقترحة
    # ============================================================
    
    display_suggested_questions()


# ============================================================
# 7. تشغيل الصفحة (إذا كانت مستقلة)
# ============================================================

if __name__ == "__main__":
    show()
