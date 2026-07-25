import streamlit as st
import base64
from pathlib import Path

# ============================================================
# 🎨 إصلاح التنسيقات وتثبيت الاتجاه العربي (RTL)
# ============================================================
def apply_rtl_and_fixes():
    st.markdown("""
        <style>
        /* 🌐 فرض اتجاه الكتابة من اليمين لليسار لكافة النصوص */
        .about-header, .member-card, .info-box, .instructions-box, .stat-card {
            direction: rtl !important;
            text-align: right !important;
            unicode-bidi: isolate !important;
        }

        /* 🏛️ الهيدر الرئيسي */
        .about-header {
            background: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%);
            border: 1px solid #C7D2FE;
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
            text-align: center !important;
        }
        .about-header h1 {
            color: #1E1B4B !important;
            font-size: 2.2rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }
        .about-header p {
            color: #4338CA !important;
            font-size: 1.1rem;
            margin: 0;
        }

        /* 🃏 بطاقة العضو */
        .member-card {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 1.8rem 1.2rem;
            text-align: center !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .member-name {
            color: #0F172A !important;
            font-size: 1.3rem;
            font-weight: 700;
            margin-top: 0.8rem;
        }
        .member-role {
            color: #0284C7 !important;
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 0.8rem;
        }
        /* تحسين تباين النص الوصفي */
        .member-bio {
            color: #334155 !important; /* لون داكن وواضح للقراءة */
            font-size: 0.92rem;
            line-height: 1.7;
            margin-bottom: 1.2rem;
            direction: rtl !important;
            text-align: center !important;
        }

        /* 📖 إصلاح صندوق عن المشروع */
        .info-box {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 1.8rem 2rem;
            margin-top: 1.5rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            direction: rtl !important;
            text-align: right !important;
        }
        .info-box h3 {
            color: #0F172A !important;
            font-size: 1.4rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        .info-box p {
            color: #334155 !important;
            font-size: 1rem;
            line-height: 1.8;
            margin-bottom: 0.8rem;
            direction: rtl !important;
            text-align: right !important;
            unicode-bidi: isolate !important;
        }
        .info-box span.en-word {
            direction: ltr !important;
            display: inline-block;
        }
        </style>
    """, unsafe_allow_html=True)

# تطبيق التنسيقات
apply_rtl_and_fixes()

# ============================================================
# 📖 عرض صندوق "عن المشروع" المعالج وبدون أخطاء اتجاه
# ============================================================
st.markdown("""
<div class="info-box">
    <h3>📖 عن المشروع</h3>
    <p>
        <strong>SmartRetriever</strong> هو نظام ذكي لاسترجاع المستندات القانونية وإدارة العقود.
        يستخدم تقنيات <strong>RAG (Retrieval-Augmented Generation)</strong> و <strong>ChromaDB</strong>
        تسمح بتوفير إجابات دقيقة موثقة ومباشرة على استفسارات المستخدمين بناءً على محتوى المستندات المخزنة.
    </p>
    <p>
        🚀 تم تطوير المشروع بالكامل باستخدام <strong>Streamlit</strong> لتقديم واجهة سلسة، 
        ويتكامل بمرونة مع <strong>Groq API</strong> لتوليد إجابات سريعة وذكية.
    </p>
</div>
""", unsafe_allow_html=True)
