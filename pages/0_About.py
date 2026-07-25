"""
👥 عن الفريق - SmartRetriever
صفحة تعريفية بأعضاء الفريق الثلاثة
"""

import streamlit as st
import sys
from pathlib import Path
from PIL import Image
import os

# إضافة المجلد الرئيسي للتطبيق إلى المسار
sys.path.append(str(Path(__file__).parent.parent))

from components.sidebar import render_sidebar
from utils.logger import logger


# ============================================================
# ⚙️ إعدادات الصفحة
# ============================================================
st.set_page_config(
    page_title="عن الفريق | SmartRetriever",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# 🎨 تحميل التنسيقات المخصصة (CSS)
# ============================================================
def load_css():
    """تحميل تنسيقات الواجهة وإخفاء القائمة الجانبية الافتراضية"""
    st.markdown("""
        <style>
        /* 🚫 إخفاء قائمة التنقل الافتراضية التي يولدها Streamlit */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }

        /* ✅ تنسيق الهيدر */
        .about-header {
            background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%);
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 14px;
            padding: 2rem 2rem;
            margin-bottom: 2rem;
            text-align: center;
        }
        .about-header h1 {
            color: #FFFFFF;
            font-weight: 800;
            font-size: 2.8rem;
            margin: 0 0 0.5rem 0;
        }
        .about-header p {
            color: #94A3B8;
            font-size: 1.1rem;
            margin: 0;
        }

        /* ✅ بطاقة العضو */
        .member-card {
            background: #182232;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 1.8rem 1.2rem;
            text-align: center;
            transition: all 0.3s ease;
            height: 100%;
        }
        .member-card:hover {
            border-color: #38BDF8;
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(56, 189, 248, 0.1);
        }
        .member-avatar {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #38BDF8;
            margin: 0 auto 1rem auto;
            display: block;
        }
        .member-avatar-placeholder {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background: #1E293B;
            border: 4px dashed #38BDF8;
            margin: 0 auto 1rem auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            color: #38BDF8;
        }
        .member-name {
            color: #FFFFFF;
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }
        .member-role {
            color: #38BDF8;
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
        }
        .member-bio {
            color: #94A3B8;
            font-size: 0.95rem;
            line-height: 1.7;
            margin-bottom: 1rem;
        }
        .skill-badge {
            display: inline-block;
            background: #1E293B;
            color: #CBD5E1;
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            font-size: 0.75rem;
            margin: 0.15rem;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        /* ✅ تنسيق وصف المشروع */
        .project-info {
            background: #182232;
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 14px;
            padding: 1.8rem 2rem;
            margin-top: 2rem;
        }
        .project-info h3 {
            color: #FFFFFF;
            font-weight: 700;
            margin-bottom: 0.75rem;
        }
        .project-info p {
            color: #94A3B8;
            font-size: 1rem;
            line-height: 1.8;
        }
        .project-info strong {
            color: #38BDF8;
        }

        /* ✅ تنسيق التعليمات */
        .instructions-box {
            background: #0F172A;
            border: 1px solid rgba(56, 189, 248, 0.2);
            border-radius: 12px;
            padding: 1.2rem 1.5rem;
            margin-top: 1.5rem;
        }
        .instructions-box h4 {
            color: #38BDF8;
            margin-bottom: 0.5rem;
        }
        .instructions-box p {
            color: #94A3B8;
            font-size: 0.9rem;
            margin: 0;
        }
        .instructions-box code {
            background: #1E293B;
            color: #38BDF8;
            padding: 0.1rem 0.4rem;
            border-radius: 4px;
            font-size: 0.85rem;
        }

        /* ✅ تنسيق الإحصائيات */
        .stat-card {
            background: #182232;
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
        }
        .stat-card .stat-number {
            color: #38BDF8;
            font-size: 2.2rem;
            font-weight: 700;
        }
        .stat-card .stat-label {
            color: #94A3B8;
            font-size: 0.9rem;
        }
        .stat-card .stat-delta {
            color: #34D399;
            font-size: 0.8rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # تحميل ملف CSS الخارجي إن وجد
    css_file = Path(__file__).parent.parent / "styles" / "custom.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ============================================================
# 🖼️ دالة تحميل الصور
# ============================================================
def load_image(image_path: str):
    """
    تحميل صورة من المسار المحدد
    
    Args:
        image_path: مسار الصورة
        
    Returns:
        صورة PIL أو None
    """
    try:
        if os.path.exists(image_path):
            return Image.open(image_path)
        else:
            return None
    except Exception as e:
        logger.warning(f"⚠️ لا يمكن تحميل الصورة: {image_path} - {str(e)}")
        return None


# ============================================================
# 🔀 التوجيه بين الصفحات
# ============================================================
def handle_routing(selected_page: str):
    """ربط التنقل بين الصفحات"""
    page_routes = {
        "HOME": "app.py",
        "المساعد الذكي": "pages/1_Chat.py",
        "المستندات": "pages/2_Documents.py",
        "التحليلات": "pages/3_Analytics.py",
    }
    if selected_page in page_routes:
        target_file = page_routes[selected_page]
        if Path(target_file).exists():
            st.switch_page(target_file)


# ============================================================
# 📄 الصفحة الرئيسية
# ============================================================
def show():
    """عرض الواجهة الكلية لصفحة عن الفريق"""
    load_css()

    # ✅ 1. عرض السايدبار والتنقل
    selected_page = render_sidebar(
        show_theme_toggle=True,
        show_stats=False,
        show_navigation=True
    )

    if selected_page != "عن الفريق":
        handle_routing(selected_page)

    # ✅ 2. الهيدر
    st.markdown("""
    <div class="about-header">
        <h1>👥 فريق SmartRetriever</h1>
        <p>نظام استرجاع ذكي للمستندات القانونية والعقود</p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ 3. بيانات أعضاء الفريق
    # تحديد مسار مجلد الصور
    IMAGES_DIR = Path(__file__).parent.parent / "assets" / "team"
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # بيانات الأعضاء
    team_members = [
        {
            "name": "Goda Emad",
            "role": "👨‍💻 Full-Stack Developer",
            "bio": "مطور Full-Stack متخصص في بناء تطبيقات الذكاء الاصطناعي واسترجاع المعلومات. خبرة في Python, Streamlit, و RAG Systems.",
            "image": IMAGES_DIR / "goda.jpg",
            "icon": "🚀",
            "skills": ["Python", "Streamlit", "RAG", "ChromaDB", "FAISS"]
        },
        {
            "name": "Ganaa Emad",
            "role": "🧠 AI / ML Engineer",
            "bio": "مهندس ذكاء اصطناعي متخصص في معالجة اللغة الطبيعية ونماذج التضمين. خبرة في Transformers, Embeddings, و RAG Pipelines.",
            "image": IMAGES_DIR / "ganaa.jpg",
            "icon": "🤖",
            "skills": ["NLP", "Transformers", "Sentence-Transformers", "LLMs", "Groq"]
        },
        {
            "name": "Manar Harby",
            "role": "📊 Data Scientist",
            "bio": "عالم بيانات متخصص في تحليل البيانات وتصورها. خبرة في Pandas, Plotly, واستخراج المعلومات من المستندات.",
            "image": IMAGES_DIR / "manar.jpg",
            "icon": "📈",
            "skills": ["Pandas", "Plotly", "Data Analysis", "Document Processing", "Visualization"]
        }
    ]

    # عرض الأعضاء في 3 أعمدة
    cols = st.columns(3)

    for i, member in enumerate(team_members):
        with cols[i]:
            img = load_image(str(member["image"]))

            # عرض الصورة أو placeholder
            if img:
                st.image(img, width=150, use_container_width=False)
            else:
                st.markdown(f"""
                <div class="member-avatar-placeholder">
                    {member["icon"]}
                </div>
                """, unsafe_allow_html=True)
                # رسالة إرشادية
                st.caption(f"💡 ضع الصورة هنا: `{member['image']}`")

            st.markdown(f"""
            <div class="member-card">
                <div class="member-name">{member["name"]}</div>
                <div class="member-role">{member["role"]}</div>
                <div class="member-bio">{member["bio"]}</div>
                <div style="margin-top: 0.5rem;">
            """, unsafe_allow_html=True)

            # عرض المهارات
            for skill in member["skills"]:
                st.markdown(f'<span class="skill-badge">#{skill}</span>', unsafe_allow_html=True)

            st.markdown("</div></div>", unsafe_allow_html=True)

    # ✅ 4. الإحصائيات
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">16+</div>
            <div class="stat-label">📂 مستندات</div>
            <div class="stat-delta">✅ تم تحميلها</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">MiniLM</div>
            <div class="stat-label">🔍 نموذج التضمين</div>
            <div class="stat-delta">🌍 متعدد اللغات</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">Llama 3.3</div>
            <div class="stat-label">🤖 نموذج المحادثة</div>
            <div class="stat-delta">⚡ Groq Cloud</div>
        </div>
        """, unsafe_allow_html=True)

    # ✅ 5. وصف المشروع
    st.markdown("""
    <div class="project-info">
        <h3>📖 عن المشروع</h3>
        <p>
            <strong>SmartRetriever</strong> هو نظام ذكي لاسترجاع المستندات القانونية وإدارة العقود.
            يستخدم تقنيات <strong>RAG (Retrieval-Augmented Generation)</strong> و <strong>ChromaDB</strong>
            لتوفير إجابات دقيقة على استفسارات المستخدمين بناءً على محتوى المستندات المخزنة.
        </p>
        <p style="margin-top: 0.5rem;">
            🚀 تم بناء المشروع باستخدام <strong>Streamlit</strong> مع واجهة سهلة الاستخدام،
            ويتكامل مع <strong>Groq API</strong> لتوليد إجابات سريعة وذكية.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ 6. تعليمات إضافة الصور
    st.markdown("""
    <div class="instructions-box">
        <h4>📸 كيفية إضافة صور الفريق</h4>
        <p>
            1️⃣ أنشئ مجلد <code>assets/team/</code> في جذر المشروع<br>
            2️⃣ ضع الصور فيه بالأسماء التالية:<br>
            &nbsp;&nbsp;• <code>goda.jpg</code> - صورة Goda Emad<br>
            &nbsp;&nbsp;• <code>ganaa.jpg</code> - صورة Ganaa Emad<br>
            &nbsp;&nbsp;• <code>manar.jpg</code> - صورة Manar Harby<br>
            3️⃣ أعد تشغيل التطبيق وستظهر الصور تلقائياً
        </p>
        <p style="margin-top: 0.5rem; color: #64748B;">
            💡 المقاسات الموصى بها: 500 × 500 بكسل (مربع)
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ 7. تذييل الصفحة
    st.markdown("""
    <div style="
        text-align: center;
        color: #475569;
        font-size: 0.85rem;
        padding: 2rem 0 0.5rem 0;
        border-top: 1px solid #1E293B;
        margin-top: 2rem;
    ">
        👥 فريق SmartRetriever | © 2026 | جميع الحقوق محفوظة
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# 🚀 تشغيل الصفحة
# ============================================================
if __name__ == "__main__":
    show()
