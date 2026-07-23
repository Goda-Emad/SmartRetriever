# app/pages/2_Documents.py
"""
📄 صفحة إدارة المستندات - Documents Page

تعرض المستندات في قاعدة المعرفة وتتيح رفع ملفات جديدة
"""

import streamlit as st
import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime

# إضافة المجلد الحالي إلى المسار
sys.path.append(str(Path(__file__).parent.parent))

from core.config import settings
from database.text_loader import TextLoader
from database.docx_loader import DocxLoader
from utils.logger import logger


# ============================================================
# 1. دوال مساعدة
# ============================================================

def get_documents_stats():
    """
    الحصول على إحصائيات المستندات
    
    Returns:
        dict: إحصائيات المستندات
    """
    kb_path = settings.KNOWLEDGE_BASE_PATH
    stats = {
        "total": 0,
        "by_category": {},
        "file_types": {}
    }
    
    if not kb_path.exists():
        return stats
    
    for category_dir in kb_path.iterdir():
        if category_dir.is_dir():
            count = 0
            for file_path in category_dir.glob("*"):
                if file_path.is_file():
                    count += 1
                    # تسجيل نوع الملف
                    ext = file_path.suffix.lower()
                    stats["file_types"][ext] = stats["file_types"].get(ext, 0) + 1
            stats["by_category"][category_dir.name] = count
            stats["total"] += count
    
    return stats


def get_documents(category: str = None):
    """
    الحصول على قائمة المستندات
    
    Args:
        category: تصفية حسب التصنيف
        
    Returns:
        list: قائمة المستندات
    """
    kb_path = settings.KNOWLEDGE_BASE_PATH
    documents = []
    
    if not kb_path.exists():
        return documents
    
    for category_dir in kb_path.iterdir():
        if category_dir.is_dir():
            if category and category_dir.name != category:
                continue
            for file_path in category_dir.glob("*"):
                if file_path.is_file():
                    documents.append({
                        "filename": file_path.name,
                        "category": category_dir.name,
                        "path": str(file_path),
                        "size": file_path.stat().st_size,
                        "modified": datetime.fromtimestamp(file_path.stat().st_mtime)
                    })
    
    # ترتيب حسب التاريخ (الأحدث أولاً)
    documents.sort(key=lambda x: x["modified"], reverse=True)
    
    return documents


def delete_document(file_path: str) -> bool:
    """
    حذف مستند
    
    Args:
        file_path: مسار الملف
        
    Returns:
        bool: نجاح الحذف
    """
    try:
        path = Path(file_path)
        if path.exists():
            path.unlink()
            logger.info(f"🗑️ Document deleted: {file_path}")
            return True
        return False
    except Exception as e:
        logger.error(f"❌ Error deleting document: {str(e)}")
        return False


def rebuild_index():
    """
    إعادة بناء فهرس FAISS
    """
    try:
        script_path = Path(__file__).parent.parent.parent / "scripts" / "build_index.py"
        if script_path.exists():
            result = subprocess.run(
                ["python", str(script_path)],
                capture_output=True,
                text=True,
                timeout=300
            )
            if result.returncode == 0:
                st.success("✅ تم إعادة بناء الفهرس بنجاح")
                logger.info("✅ Index rebuilt successfully")
            else:
                st.error(f"❌ فشل إعادة بناء الفهرس: {result.stderr}")
                logger.error(f"❌ Index rebuild failed: {result.stderr}")
        else:
            st.warning("⚠️ ملف build_index.py غير موجود")
    except subprocess.TimeoutExpired:
        st.error("❌ انتهت مهلة إعادة بناء الفهرس (أكثر من 5 دقائق)")
    except Exception as e:
        st.error(f"❌ خطأ في إعادة بناء الفهرس: {str(e)}")
        logger.error(f"❌ Index rebuild error: {str(e)}")


# ============================================================
# 2. عرض الصفحة
# ============================================================

def show():
    """عرض صفحة المستندات"""
    
    st.title("📄 إدارة المستندات")
    st.caption("رفع وعرض المستندات في قاعدة المعرفة")
    
    st.divider()
    
    # ============================================================
    # 1. إحصائيات سريعة
    # ============================================================
    
    stats = get_documents_stats()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📄 إجمالي المستندات", stats["total"])
    
    with col2:
        st.metric("📁 عدد التصنيفات", len(stats["by_category"]))
    
    with col3:
        if stats["by_category"]:
            max_cat = max(stats["by_category"], key=stats["by_category"].get)
            st.metric("📊 التصنيف الأكبر", max_cat)
        else:
            st.metric("📊 التصنيف الأكبر", "—")
    
    with col4:
        if stats["file_types"]:
            max_ext = max(stats["file_types"], key=stats["file_types"].get)
            st.metric("📂 النوع الأكثر", max_ext.upper())
        else:
            st.metric("📂 النوع الأكثر", "—")
    
    st.divider()
    
    # ============================================================
    # 2. رفع مستند جديد
    # ============================================================
    
    with st.expander("📤 رفع مستند جديد", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            uploaded_file = st.file_uploader(
                "اختر ملف",
                type=['txt', 'docx', 'pdf'],
                help="الملفات المدعومة: .txt, .docx, .pdf"
            )
        
        with col2:
            category = st.selectbox(
                "التصنيف",
                ["contracts", "policies", "quotations", "quality_reports", "other"],
                index=4,
                help="اختر التصنيف المناسب للملف"
            )
        
        # عرض معلومات الملف
        if uploaded_file:
            st.info(f"📄 **اسم الملف:** {uploaded_file.name}")
            st.info(f"📦 **الحجم:** {uploaded_file.size / 1024:.1f} KB")
        
        if uploaded_file and st.button("🚀 رفع الملف", use_container_width=True):
            # حفظ الملف
            save_path = settings.KNOWLEDGE_BASE_PATH / category / uploaded_file.name
            save_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.success(f"✅ تم رفع الملف بنجاح: {uploaded_file.name}")
            
            # إعادة بناء الفهرس
            with st.spinner("🔄 جاري إعادة بناء الفهرس..."):
                rebuild_index()
            
            st.rerun()
    
    # ============================================================
    # 3. عرض المستندات
    # ============================================================
    
    st.subheader("📋 قائمة المستندات")
    
    # فلتر التصنيف
    categories = ["الكل"] + list(stats["by_category"].keys())
    selected_category = st.selectbox("🔍 تصفية حسب التصنيف", categories, index=0)
    
    # الحصول على المستندات
    category_filter = None if selected_category == "الكل" else selected_category
    documents = get_documents(category_filter)
    
    # عرض المستندات
    if documents:
        # عدد النتائج
        st.caption(f"عرض {len(documents)} مستند")
        
        # عرض في جدول
        for doc in documents:
            with st.container():
                col1, col2, col3, col4 = st.columns([3, 1.5, 1.5, 1])
                
                with col1:
                    # أيقونة حسب النوع
                    ext = Path(doc["filename"]).suffix.lower()
                    icon = "📄" if ext == ".txt" else "📝" if ext == ".docx" else "📕" if ext == ".pdf" else "📎"
                    st.markdown(f"{icon} **{doc['filename']}**")
                
                with col2:
                    st.caption(f"📂 {doc['category']}")
                
                with col3:
                    st.caption(f"📦 {doc['size'] / 1024:.1f} KB")
                
                with col4:
                    # زر الحذف
                    if st.button("🗑️", key=f"delete_{doc['filename']}", help="حذف المستند"):
                        if delete_document(doc["path"]):
                            st.success(f"✅ تم حذف {doc['filename']}")
                            # إعادة بناء الفهرس
                            with st.spinner("🔄 جاري إعادة بناء الفهرس..."):
                                rebuild_index()
                            st.rerun()
                        else:
                            st.error(f"❌ فشل حذف {doc['filename']}")
                
                st.divider()
    else:
        st.info("📭 لا توجد مستندات في هذا التصنيف")
    
    # ============================================================
    # 4. أدوات إضافية
    # ============================================================
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 إعادة بناء الفهرس", use_container_width=True):
            with st.spinner("🔄 جاري إعادة بناء الفهرس..."):
                rebuild_index()
    
    with col2:
        # عرض مسار قاعدة المعرفة
        st.caption(f"📁 مسار قاعدة المعرفة: `{settings.KNOWLEDGE_BASE_PATH}`")


# ============================================================
# 3. تشغيل الصفحة (إذا كانت مستقلة)
# ============================================================

if __name__ == "__main__":
    show()
