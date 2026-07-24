# app/pages/3_Analytics.py
"""
📊 صفحة التحليلات والإحصائيات - Analytics Page

تعرض إحصائيات وتحليلات النظام والمستندات والموردين
"""

import streamlit as st
import sys
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from datetime import datetime, timedelta
import re

# إضافة المجلد الحالي إلى المسار
sys.path.append(str(Path(__file__).parent.parent))

from core.config import settings
from database.faiss_loader import FAISSLoader
from utils.logger import logger


# ============================================================
# ✅ تحميل التنسيقات (CSS)
# ============================================================

def load_css():
    """تحميل ملف التنسيقات المخصص"""
    css_file = Path(__file__).parent.parent / "styles" / "custom.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        logger.warning(f"⚠️ CSS file not found: {css_file}")


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
        "file_types": {},
        "total_size": 0,
        "documents": []
    }
    
    if not kb_path.exists():
        return stats
    
    for category_dir in kb_path.iterdir():
        if category_dir.is_dir():
            count = 0
            for file_path in category_dir.glob("*"):
                if file_path.is_file():
                    count += 1
                    ext = file_path.suffix.lower()
                    stats["file_types"][ext] = stats["file_types"].get(ext, 0) + 1
                    stats["total_size"] += file_path.stat().st_size
                    stats["documents"].append({
                        "filename": file_path.name,
                        "category": category_dir.name,
                        "size": file_path.stat().st_size,
                        "modified": datetime.fromtimestamp(file_path.stat().st_mtime)
                    })
            stats["by_category"][category_dir.name] = count
            stats["total"] += count
    
    return stats


def get_suppliers_from_filenames(documents):
    """
    استخراج أسماء الموردين من أسماء الملفات
    
    Args:
        documents: قائمة المستندات
        
    Returns:
        list: قائمة الموردين
    """
    suppliers = {}
    
    # أنماط للبحث عن الموردين
    patterns = [
        r'Supplier_([A-Za-z]+)',
        r'Supplier_([A-Za-z]+_[A-Za-z]+)',
        r'([A-Za-z]+_Inc)',
        r'([A-Za-z]+_Supplies)',
        r'([A-Za-z]+_Logistics)',
        r'([A-Za-z]+_Group)',
        r'([A-Za-z]+_Co)',
    ]
    
    for doc in documents:
        filename = doc["filename"]
        for pattern in patterns:
            match = re.search(pattern, filename)
            if match:
                supplier = match.group(1).replace('_', ' ')
                if supplier not in suppliers:
                    suppliers[supplier] = {
                        "name": supplier,
                        "documents": 0,
                        "categories": set(),
                        "total_size": 0
                    }
                suppliers[supplier]["documents"] += 1
                suppliers[supplier]["categories"].add(doc["category"])
                suppliers[supplier]["total_size"] += doc["size"]
                break
    
    return [{"name": k, **v} for k, v in suppliers.items()]


def get_quality_scores(documents):
    """
    استخراج درجات الجودة من الملفات
    
    Args:
        documents: قائمة المستندات
        
    Returns:
        list: قائمة درجات الجودة
    """
    scores = []
    
    for doc in documents:
        if "quality" in doc["category"] or "Quality" in doc["filename"]:
            # محاولة استخراج درجة الجودة من اسم الملف
            match = re.search(r'(\d+)', doc["filename"])
            if match:
                score = int(match.group(1))
                if score <= 100:
                    # استخراج اسم المورد من اسم الملف
                    supplier_name = doc["filename"].replace('_Quality_Report_', '').replace('.docx', '')
                    # تنظيف الاسم إذا كان يحتوي على أرقام
                    supplier_name = re.sub(r'^\d+_', '', supplier_name)
                    scores.append({
                        "supplier": supplier_name,
                        "score": score,
                        "category": doc["category"]
                    })
    
    return scores


def get_contract_values(documents):
    """
    استخراج قيم العقود من الملفات
    
    Args:
        documents: قائمة المستندات
        
    Returns:
        list: قائمة قيم العقود
    """
    contracts = []
    
    for doc in documents:
        if "contract" in doc["category"] or "Contract" in doc["filename"]:
            # محاولة استخراج القيمة من اسم الملف
            match = re.search(r'(\d+[,\d]*\.?\d*)', doc["filename"])
            if match:
                try:
                    value_str = match.group(1).replace(',', '')
                    value = float(value_str)
                    if value > 1000:
                        supplier_name = doc["filename"].replace('_Supplier_Contract_', '').replace('.docx', '')
                        supplier_name = re.sub(r'^\d+_', '', supplier_name)
                        contracts.append({
                            "supplier": supplier_name,
                            "value": value,
                            "category": doc["category"]
                        })
                except:
                    pass
    
    return contracts


# ============================================================
# 2. عرض الصفحة
# ============================================================

def show():
    """عرض صفحة التحليلات"""
    
    # ✅ تحميل التنسيقات أولاً
    load_css()
    
    st.title("📊 التحليلات والإحصائيات")
    st.caption("نظرة عامة على النظام والمستندات والموردين")
    
    st.divider()
    
    # ============================================================
    # 1. جلب البيانات
    # ============================================================
    
    stats = get_documents_stats()
    documents = stats["documents"]
    
    # ============================================================
    # 2. بطاقات الإحصائيات
    # ============================================================
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "📄 إجمالي المستندات",
            stats["total"],
            delta="+2" if stats["total"] > 0 else "0"
        )
    
    with col2:
        st.metric(
            "📁 التصنيفات",
            len(stats["by_category"]),
            delta=None
        )
    
    with col3:
        total_size_mb = stats["total_size"] / (1024 * 1024)
        st.metric(
            "💾 الحجم الإجمالي",
            f"{total_size_mb:.1f} MB",
            delta=None
        )
    
    with col4:
        suppliers = get_suppliers_from_filenames(documents)
        st.metric(
            "🏢 الموردين",
            len(suppliers),
            delta=None
        )
    
    st.divider()
    
    # ============================================================
    # 3. الرسوم البيانية
    # ============================================================
    
    # 3.1 توزيع المستندات حسب التصنيف
    if stats["by_category"]:
        df_categories = pd.DataFrame({
            "التصنيف": list(stats["by_category"].keys()),
            "العدد": list(stats["by_category"].values())
        })
        fig1 = px.pie(
            df_categories,
            names="التصنيف",
            values="العدد",
            title="📊 توزيع المستندات حسب التصنيف",
            color_discrete_sequence=px.colors.qualitative.Set3,
            hole=0.3
        )
        fig1.update_layout(
            height=400,
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.1)
        )
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("📭 لا توجد مستندات للتحليل")
    
    # 3.2 أنواع الملفات
    if stats["file_types"]:
        col1, col2 = st.columns(2)
        
        with col1:
            df_filetypes = pd.DataFrame({
                "نوع الملف": list(stats["file_types"].keys()),
                "العدد": list(stats["file_types"].values())
            })
            fig2 = px.bar(
                df_filetypes,
                x="نوع الملف",
                y="العدد",
                title="📂 أنواع الملفات",
                color_discrete_sequence=["#2563EB"]
            )
            fig2.update_layout(height=300)
            st.plotly_chart(fig2, use_container_width=True)
        
        with col2:
            # توزيع الأحجام
            if documents:
                sizes = [doc["size"] / 1024 for doc in documents]
                df_sizes = pd.DataFrame({"الحجم (KB)": sizes})
                fig3 = px.histogram(
                    df_sizes,
                    x="الحجم (KB)",
                    title="📊 توزيع أحجام الملفات (KB)",
                    nbins=10,
                    color_discrete_sequence=["#10B981"]
                )
                fig3.update_layout(height=300)
                st.plotly_chart(fig3, use_container_width=True)
    
    st.divider()
    
    # ============================================================
    # 4. الموردين
    # ============================================================
    
    if suppliers:
        st.subheader("🏢 تحليل الموردين")
        
        # جدول الموردين
        suppliers_df = pd.DataFrame([
            {
                "المورد": s["name"],
                "المستندات": s["documents"],
                "التصنيفات": ", ".join(s["categories"]),
                "الحجم (KB)": f"{s['total_size'] / 1024:.1f}"
            }
            for s in suppliers
        ])
        
        st.dataframe(
            suppliers_df,
            use_container_width=True,
            hide_index=True
        )
        
        # رسم بياني للموردين
        fig4 = px.bar(
            suppliers_df,
            x="المورد",
            y="المستندات",
            title="📊 عدد المستندات لكل مورد",
            color_discrete_sequence=["#8B5CF6"]
        )
        fig4.update_layout(height=350)
        st.plotly_chart(fig4, use_container_width=True)
    
    st.divider()
    
    # ============================================================
    # 5. درجات الجودة (إن وجدت)
    # ============================================================
    
    quality_scores = get_quality_scores(documents)
    
    if quality_scores:
        st.subheader("⭐ تحليل الجودة")
        
        scores_df = pd.DataFrame(quality_scores)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # متوسط درجات الجودة
            avg_score = sum(s["score"] for s in quality_scores) / len(quality_scores)
            st.metric(
                "📊 متوسط درجة الجودة",
                f"{avg_score:.1f}%",
                delta="+5%" if avg_score > 80 else "0%"
            )
        
        with col2:
            # أفضل مورد
            best = max(quality_scores, key=lambda x: x["score"])
            st.metric(
                "🏆 أفضل مورد",
                best["supplier"],
                delta=f"{best['score']}%"
            )
        
        # رسم بياني لدرجات الجودة
        fig5 = px.bar(
            scores_df,
            x="supplier",
            y="score",
            title="⭐ درجات الجودة لكل مورد",
            labels={"supplier": "المورد", "score": "درجة الجودة (%)"},
            color="score",
            color_continuous_scale="RdYlGn",
            range_color=[0, 100]
        )
        fig5.update_layout(height=350)
        st.plotly_chart(fig5, use_container_width=True)
    
    # ============================================================
    # 6. قيم العقود (إن وجدت)
    # ============================================================
    
    contracts = get_contract_values(documents)
    
    if contracts:
        st.subheader("💰 تحليل العقود")
        
        contracts_df = pd.DataFrame([
            {
                "المورد": c["supplier"],
                "القيمة (ريال)": c["value"],
                "التصنيف": c["category"]
            }
            for c in contracts
        ])
        
        # ترتيب حسب القيمة
        contracts_df = contracts_df.sort_values("القيمة (ريال)", ascending=False)
        
        st.dataframe(
            contracts_df,
            use_container_width=True,
            hide_index=True
        )
        
        # رسم بياني للعقود
        fig6 = px.bar(
            contracts_df,
            x="المورد",
            y="القيمة (ريال)",
            title="💰 قيم العقود لكل مورد",
            color_discrete_sequence=["#F59E0B"]
        )
        fig6.update_layout(height=350)
        st.plotly_chart(fig6, use_container_width=True)
    
    # ============================================================
    # 7. معلومات النظام
    # ============================================================
    
    with st.expander("⚙️ معلومات النظام", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📁 المسارات:**")
            st.code(f"قاعدة المعرفة: {settings.KNOWLEDGE_BASE_PATH}")
            st.code(f"فهرس FAISS: {settings.FAISS_INDEX_PATH}")
            st.code(f"بيانات: {settings.DATA_PATH}")
        
        with col2:
            st.markdown("**🔧 الإعدادات:**")
            st.code(f"النموذج: {settings.EMBEDDING_MODEL}")
            st.code(f"الجهاز: {settings.EMBEDDING_DEVICE}")
            st.code(f"أبعاد المتجهات: {settings.EMBEDDING_DIMENSION}")
        
        st.markdown("**📊 حالة الفهرس:**")
        try:
            loader = FAISSLoader()
            index_info = loader.get_index_info()
            st.code(f"الحالة: {index_info.get('status', 'غير معروف')}")
            st.code(f"عدد المستندات: {index_info.get('total_vectors', 0)}")
        except Exception as e:
            st.warning(f"⚠️ لا يمكن قراءة حالة الفهرس: {str(e)}")


# ============================================================
# 3. تشغيل الصفحة (إذا كانت مستقلة)
# ============================================================

if __name__ == "__main__":
    show()
