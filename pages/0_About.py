"""
👥 عن الفريق - SmartRetriever
صفحة تعريفية بأعضاء الفريق الثلاثة
"""

import streamlit as st
import sys
from pathlib import Path
from PIL import Image
import os

sys.path.append(str(Path(__file__).parent.parent))

from components.sidebar import render_sidebar, TRANSLATIONS
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
# 🎨 تنسيقات هيكلية فقط (Layout) - بدون ألوان ثابتة
# ============================================================
def load_structural_css():
    """
    تنسيقات الأبعاد/المسافات/الأشكال فقط (مش الألوان).
    الألوان بتتحدد ديناميكيًا من apply_dynamic_theme() في sidebar.py
    عشان الصفحة تستجيب لتبديل الثيم زي باقي الصفحات بالظبط.
    """
    st.markdown("""
        <style>
        .about-header {
            border-radius: 14px;
            padding: 2rem 2rem;
            margin-bottom: 2rem;
            text-align: center;
        }
        .about-header h1 {
            font-weight: 800;
            font-size: 2.8rem;
            margin: 0 0 0.5rem 0;
        }
        .about-header p {
            font-size: 1.1rem;
            margin: 0;
        }

        .member-card {
            border-radius: 14px;
            padding: 1.8rem 1.2rem;
            text-align: center;
            transition: all 0.3s ease;
            height: 100%;
        }
        .member-card:hover {
            border-color: #38BDF8 !important;
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
            margin: 0 auto 1rem auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
        }
        .member-name {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }
        .member-role {
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
        }
        .member-bio {
            font-size: 0.95rem;
            line-height: 1.7;
            margin-bottom: 1rem;
        }
        .skill-badge {
            display: inline-block;
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            font-size: 0.75rem;
            margin: 0.15rem;
        }

        .project-info {
            padding: 1.8rem 2rem;
            margin-top: 2rem;
        }
        .project-info h3 {
            font-weight: 700;
            margin-bottom: 0.75rem;
        }
        .project-info p {
            font-size: 1rem;
            line-height: 1.8;
        }
        .project-info strong {
            color: #38BDF8;
        }

        .instructions-box {
            padding: 1.2rem 1.5rem;
            margin-top: 1.5rem;
        }
        .instructions-box h4 {
            margin-bottom: 0.5rem;
        }
        .instructions-box p {
            font-size: 0.9rem;
            margin: 0;
        }
        .instructions-box code {
            padding: 0.1rem 0.4rem;
            border-radius: 4px;
            font-size: 0.85rem;
        }

        .stat-card {
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
        }
        .stat-card .stat-number {
            font-size: 2.2rem;
            font-weight: 700;
        }
        .stat-card .stat-label {
            font-size: 0.9rem;
        }
        .stat-card .stat-delta {
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
    """تحميل صورة من المسار المحدد"""
    try:
        if os.path.exists(image_path):
            return Image.open(image_path)
        return None
    except Exception as e:
        logger.warning(f"⚠️ لا يمكن تحميل الصورة: {image_path} - {str(e)}")
        return None


# ============================================================
# 📄 الصفحة الرئيسية
# ============================================================
def show():
    """عرض الواجهة الكلية لصفحة عن الفريق"""

    # ✅ 1. عرض السايدبار (بيتكفل بالثيم، إخفاء الـ nav التلقائي، واللغة)
    lang_code = render_sidebar(
        show_theme_toggle=True,
        show_stats=False,
        show_navigation=True
    )
    T = TRANSLATIONS.get(lang_code, TRANSLATIONS["ar"])

    # ✅ 2. التنسيقات الهيكلية (بدون ألوان - الألوان من الثيم المشترك)
    load_structural_css()

    # ✅ 3. الهيدر
    st.markdown(f"""
    <div class="about-header">
        <h1>{T['about_title']}</h1>
        <p>{T['about_subtitle']}</p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ 4. بيانات أعضاء الفريق
    IMAGES_DIR = Path(__file__).parent.parent / "assets" / "team"
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    team_members = [
        {
            "name": "Goda Emad",
            "role": "👨‍💻 Full-Stack Developer",
            "bio": "مطور Full-Stack متخصص في بناء تطبيقات الذكاء الاصطناعي واسترجاع المعلومات. خبرة في Python, Streamlit, و RAG Systems." if lang_code == "ar" else "Full-Stack developer specialized in building AI and information-retrieval applications. Experienced in Python, Streamlit, and RAG Systems.",
            "image": IMAGES_DIR / "goda.jpg",
            "icon": "🚀",
            "skills": ["Python", "Streamlit", "RAG", "ChromaDB", "FAISS"]
        },
        {
            "name": "Ganaa Emad",
            "role": "🧠 AI / ML Engineer",
            "bio": "مهندس ذكاء اصطناعي متخصص في معالجة اللغة الطبيعية ونماذج التضمين. خبرة في Transformers, Embeddings, و RAG Pipelines." if lang_code == "ar" else "AI engineer specialized in NLP and embedding models. Experienced in Transformers, Embeddings, and RAG Pipelines.",
            "image": IMAGES_DIR / "ganaa.jpg",
            "icon": "🤖",
            "skills": ["NLP", "Transformers", "Sentence-Transformers", "LLMs", "Groq"]
        },
        {
            "name": "Manar Harby",
            "role": "📊 Data Scientist",
            "bio": "عالم بيانات متخصص في تحليل البيانات وتصورها. خبرة في Pandas, Plotly, واستخراج المعلومات من المستندات." if lang_code == "ar" else "Data scientist specialized in data analysis and visualization. Experienced in Pandas, Plotly, and document information extraction.",
            "image": IMAGES_DIR / "manar.jpg",
            "icon": "📈",
            "skills": ["Pandas", "Plotly", "Data Analysis", "Document Processing", "Visualization"]
        }
    ]

    cols = st.columns(3)

    for i, member in enumerate(team_members):
        with cols[i]:
            img = load_image(str(member["image"]))

            if img:
                st.image(img, width=150, use_container_width=False)
            else:
                st.markdown(f"""
                <div class="member-avatar-placeholder">
                    {member["icon"]}
                </div>
                """, unsafe_allow_html=True)
                st.caption(f"{T['image_placeholder_hint']} `{member['image']}`")

            st.markdown(f"""
            <div class="member-card">
                <div class="member-name">{member["name"]}</div>
                <div class="member-role">{member["role"]}</div>
                <div class="member-bio">{member["bio"]}</div>
                <div style="margin-top: 0.5rem;">
            """, unsafe_allow_html=True)

            for skill in member["skills"]:
                st.markdown(f'<span class="skill-badge">#{skill}</span>', unsafe_allow_html=True)

            st.markdown("</div></div>", unsafe_allow_html=True)

    # ✅ 5. الإحصائيات
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">16+</div>
            <div class="stat-label">{T['stat_docs_label']}</div>
            <div class="stat-delta">{T['stat_docs_delta']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">MiniLM</div>
            <div class="stat-label">{T['stat_embed_label']}</div>
            <div class="stat-delta">{T['stat_embed_delta']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">Llama 3.3</div>
            <div class="stat-label">{T['stat_llm_label']}</div>
            <div class="stat-delta">{T['stat_llm_delta']}</div>
        </div>
        """, unsafe_allow_html=True)

    # ✅ 6. وصف المشروع
    st.markdown(f"""
    <div class="project-info">
        <h3>{T['about_project_title']}</h3>
        <p><strong>SmartRetriever</strong> {T['about_project_p1']}</p>
        <p style="margin-top: 0.5rem;">{T['about_project_p2']}</p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ 7. تعليمات إضافة الصور
    if lang_code == "ar":
        instructions_body = """
            1️⃣ أنشئ مجلد <code>assets/team/</code> في جذر المشروع<br>
            2️⃣ ضع الصور فيه بالأسماء التالية:<br>
            &nbsp;&nbsp;• <code>goda.jpg</code> - صورة Goda Emad<br>
            &nbsp;&nbsp;• <code>ganaa.jpg</code> - صورة Ganaa Emad<br>
            &nbsp;&nbsp;• <code>manar.jpg</code> - صورة Manar Harby<br>
            3️⃣ أعد تشغيل التطبيق وستظهر الصور تلقائياً
        """
    else:
        instructions_body = """
            1️⃣ Create an <code>assets/team/</code> folder at the project root<br>
            2️⃣ Add the photos with these exact names:<br>
            &nbsp;&nbsp;• <code>goda.jpg</code> - Goda Emad's photo<br>
            &nbsp;&nbsp;• <code>ganaa.jpg</code> - Ganaa Emad's photo<br>
            &nbsp;&nbsp;• <code>manar.jpg</code> - Manar Harby's photo<br>
            3️⃣ Restart the app and the photos will appear automatically
        """

    st.markdown(f"""
    <div class="instructions-box">
        <h4>{T['instructions_title']}</h4>
        <p>{instructions_body}</p>
        <p style="margin-top: 0.5rem;">{T['instructions_hint']}</p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ 8. تذييل الصفحة
    st.markdown(f"""
    <div style="
        text-align: center;
        font-size: 0.85rem;
        padding: 2rem 0 0.5rem 0;
        border-top: 1px solid rgba(128, 128, 128, 0.2);
        margin-top: 2rem;
        opacity: 0.7;
    ">
        {T['about_footer']}
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# 🚀 تشغيل الصفحة
# ============================================================
if __name__ == "__main__":
    show()
