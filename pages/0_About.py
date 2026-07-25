"""
👥 عن الفريق - SmartRetriever
صفحة تعريفية بأعضاء الفريق الثلاثة مع دعم كامل للثيم الفاتح والداكن.
"""

import base64
import os
import sys
from pathlib import Path
from PIL import Image
import streamlit as st

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
# 🎨 تحميل التنسيقات المخصصة (CSS الديناميكي)
# ============================================================
def load_css():
    """تحميل تنسيقات الواجهة مع دعم تلقائي للوضع الفاتح والداكن"""
    st.markdown("""
        <style>
        /* 🚫 إخفاء قائمة التنقل الافتراضية لـ Streamlit */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }

        /* 🎨 المتغيرات اللونية الافتراضية (Dark Mode) */
        :root {
            --bg-header: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%);
            --header-border: rgba(99, 102, 241, 0.3);
            --header-text: #FFFFFF;
            --header-subtext: #94A3B8;
            
            --card-bg: #1E293B;
            --card-border: rgba(255, 255, 255, 0.08);
            --card-hover-border: #38BDF8;
            
            --text-main: #F8FAFC;
            --text-muted: #94A3B8;
            --accent-color: #38BDF8;
            
            --badge-bg: #0F172A;
            --badge-text: #CBD5E1;
            --badge-border: rgba(255, 255, 255, 0.1);
            
            --box-bg: #0F172A;
            --box-border: rgba(56, 189, 248, 0.2);
            --footer-border: #1E293B;
        }

        /* ☀️ التكيف التلقائي مع الوضع الفاتح (Light Mode) */
        @media (prefers-color-scheme: light) {
            :root {
                --bg-header: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%);
                --header-border: #C7D2FE;
                --header-text: #1E1B4B;
                --header-subtext: #475569;
                
                --card-bg: #FFFFFF;
                --card-border: #E2E8F0;
                --card-hover-border: #0284C7;
                
                --text-main: #0F172A;
                --text-muted: #475569;
                --accent-color: #0284C7;
                
                --badge-bg: #F1F5F9;
                --badge-text: #334155;
                --badge-border: #E2E8F0;
                
                --box-bg: #F8FAFC;
                --box-border: #CBD5E1;
                --footer-border: #E2E8F0;
            }
        }

        /* ✅ تطبيق التكيف الداكن/الفاتح بدقة على Streamlit */
        [data-theme="light"] {
            --bg-header: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%);
            --header-border: #C7D2FE;
            --header-text: #1E1B4B;
            --header-subtext: #475569;
            
            --card-bg: #FFFFFF;
            --card-border: #E2E8F0;
            --card-hover-border: #0284C7;
            
            --text-main: #0F172A;
            --text-muted: #475569;
            --accent-color: #0284C7;
            
            --badge-bg: #F1F5F9;
            --badge-text: #334155;
            --badge-border: #E2E8F0;
            
            --box-bg: #F8FAFC;
            --box-border: #CBD5E1;
            --footer-border: #E2E8F0;
        }

        /* 🏛️ الهيدر */
        .about-header {
            background: var(--bg-header);
            border: 1px solid var(--header-border);
            border-radius: 16px;
            padding: 2.2rem 2rem;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        }
        .about-header h1 {
            color: var(--header-text) !important;
            font-weight: 800;
            font-size: 2.5rem;
            margin: 0 0 0.5rem 0;
        }
        .about-header p {
            color: var(--header-subtext) !important;
            font-size: 1.1rem;
            margin: 0;
        }

        /* 🃏 بطاقة العضو */
        .member-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 2rem 1.2rem;
            text-align: center;
            transition: all 0.3s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
        }
        .member-card:hover {
            border-color: var(--card-hover-border);
            transform: translateY(-6px);
            box-shadow: 0 12px 30px rgba(2, 132, 199, 0.12);
        }
        .member-avatar {
            width: 130px;
            height: 130px;
            border-radius: 50%;
            object-fit: cover;
            border: 3.5px solid var(--accent-color);
            margin: 0 auto 1.2rem auto;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .member-avatar-placeholder {
            width: 130px;
            height: 130px;
            border-radius: 50%;
            background: var(--box-bg);
            border: 3px dashed var(--accent-color);
            margin: 0 auto 1.2rem auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3.5rem;
        }
        .member-name {
            color: var(--text-main) !important;
            font-size: 1.4rem;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }
        .member-role {
            color: var(--accent-color) !important;
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 0.8rem;
        }
        .member-bio {
            color: var(--text-muted) !important;
            font-size: 0.92rem;
            line-height: 1.7;
            margin-bottom: 1.2rem;
            flex-grow: 1;
        }
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.4rem;
            margin-top: auto;
        }
        .skill-badge {
            background: var(--badge-bg);
            color: var(--badge-text) !important;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 500;
            border: 1px solid var(--badge-border);
        }

        /* 📊 بطاقات الإحصائيات */
        .stat-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 14px;
            padding: 1.4rem 1rem;
            text-align: center;
        }
        .stat-card .stat-number {
            color: var(--accent-color) !important;
            font-size: 2.2rem;
            font-weight: 800;
            line-height: 1.2;
        }
        .stat-card .stat-label {
            color: var(--text-main) !important;
            font-size: 0.95rem;
            font-weight: 600;
            margin-top: 0.3rem;
        }
        .stat-card .stat-delta {
            color: #10B981 !important;
            font-size: 0.82rem;
            margin-top: 0.2rem;
        }

        /* 📖 صندوق المعلومات والتعليمات */
        .info-box {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 14px;
            padding: 1.8rem 2rem;
            margin-top: 1.5rem;
        }
        .info-box h3, .info-box h4 {
            color: var(--text-main) !important;
            font-weight: 700;
            margin-top: 0;
            margin-bottom: 0.75rem;
        }
        .info-box p {
            color: var(--text-muted) !important;
            font-size: 0.98rem;
            line-height: 1.8;
            margin: 0;
        }
        .info-box strong {
            color: var(--accent-color) !important;
        }
        .instructions-box {
            background: var(--box-bg);
            border: 1px solid var(--box-border);
            border-radius: 12px;
            padding: 1.4rem 1.6rem;
            margin-top: 1.5rem;
        }
        .instructions-box h4 {
            color: var(--accent-color) !important;
            margin-top: 0;
            margin-bottom: 0.6rem;
        }
        .instructions-box p {
            color: var(--text-muted) !important;
            font-size: 0.9rem;
            line-height: 1.7;
            margin: 0;
        }
        .instructions-box code {
            background: var(--card-bg);
            color: var(--accent-color) !important;
            padding: 0.2rem 0.5rem;
            border-radius: 6px;
            font-size: 0.85rem;
            border: 1px solid var(--card-border);
        }

        /* 📌 تذييل الصفحة */
        .page-footer {
            text-align: center;
            color: var(--text-muted) !important;
            font-size: 0.85rem;
            padding: 2rem 0 1rem 0;
            border-top: 1px solid var(--footer-border);
            margin-top: 2.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # تحميل CSS مخصص إضافي إن وجد
    css_file = Path(__file__).parent.parent / "styles" / "custom.css"
    if css_file.exists():
        try:
            with open(css_file, "r", encoding="utf-8") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        except Exception as e:
            logger.warning(f"⚠️ فشل تحميل custom.css: {str(e)}")


# ============================================================
# 🖼️ دالة مساعدة لتحويل الصورة إلى Base64
# ============================================================
def get_image_b64(image_path: Path) -> str | None:
    """تحويل صورة محليّة إلى سلسلة Base64 لدمجها بسلاسة داخل كود HTML"""
    if image_path.exists():
        try:
            with open(image_path, "rb") as f:
                data = f.read()
            ext = image_path.suffix.lower().replace(".", "")
            mime_type = "jpeg" if ext in ["jpg", "jpeg"] else ext
            return f"data:image/{mime_type};base64,{base64.b64encode(data).decode()}"
        except Exception as e:
            logger.warning(f"⚠️ لا يمكن قراءة الصورة {image_path}: {str(e)}")
    return None


# ============================================================
# 🔀 التوجيه بين الصفحات
# ============================================================
def handle_routing(selected_page: str):
    """ربط التنقل بين صفحات التطبيق"""
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

    # ✅ 1. عرض القائمة الجانبية
    selected_page = render_sidebar(
        show_theme_toggle=True,
        show_stats=False,
        show_navigation=True
    )

    if selected_page != "عن الفريق":
        handle_routing(selected_page)

    # ✅ 2. الهيدر الرئيسي
    st.markdown("""
    <div class="about-header">
        <h1>👥 فريق SmartRetriever</h1>
        <p>نظام استرجاع ذكي وتحليل للمستندات القانونية والعقود</p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ 3. بيانات أعضاء الفريق
    IMAGES_DIR = Path(__file__).parent.parent / "assets" / "team"
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

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
            "bio": "عالمة بيانات متخصصة في تحليل البيانات وتصورها. خبرة في Pandas, Plotly, واستخراج المعلومات من المستندات.",
            "image": IMAGES_DIR / "manar.jpg",
            "icon": "📈",
            "skills": ["Pandas", "Plotly", "Data Analysis", "Document Processing", "Visualization"]
        }
    ]

    # عرض بطاقات الأعضاء في 3 أعمدة بشكل متناسق
    cols = st.columns(3)

    for i, member in enumerate(team_members):
        with cols[i]:
            img_b64 = get_image_b64(member["image"])

            if img_b64:
                avatar_html = f'<img src="{img_b64}" class="member-avatar" alt="{member["name"]}"/>'
            else:
                avatar_html = f'''
                <div class="member-avatar-placeholder">
                    <span>{member["icon"]}</span>
                </div>
                '''

            skills_html = "".join([f'<span class="skill-badge">#{skill}</span>' for skill in member["skills"]])

            card_html = f"""
            <div class="member-card">
                {avatar_html}
                <div class="member-name">{member["name"]}</div>
                <div class="member-role">{member["role"]}</div>
                <div class="member-bio">{member["bio"]}</div>
                <div class="skills-container">
                    {skills_html}
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)

            if not img_b64:
                st.caption(f"💡 ضع الصورة هنا: `{member['image'].name}`")

    # ✅ 4. الإحصائيات والتقنيات
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">16+</div>
            <div class="stat-label">📂 مستندات مخزنة</div>
            <div class="stat-delta">✅ جاهزة للاستعلام</div>
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
            <div class="stat-delta">⚡ Groq Cloud API</div>
        </div>
        """, unsafe_allow_html=True)

    # ✅ 5. وصف المشروع
    st.markdown("""
    <div class="info-box">
        <h3>📖 عن المشروع</h3>
        <p>
            <strong>SmartRetriever</strong> هو نظام ذكي لاسترجاع المستندات القانونية وإدارة العقود.
            يستخدم تقنيات <strong>RAG (Retrieval-Augmented Generation)</strong> و <strong>ChromaDB</strong>
            تسمح بتوفير إجابات دقيقة موثقة ومباشرة على استفسارات المستخدمين بناءً على محتوى المستندات المخزنة.
        </p>
        <p style="margin-top: 0.6rem;">
            🚀 تم تطوير المشروع بالكامل باستخدام <strong>Streamlit</strong> لتقديم واجهة سلسة، 
            ويتكامل بمرونة مع <strong>Groq API</strong> لتوليد إجابات سريعة وذكية.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ 6. تعليمات إضافة الصور
    st.markdown("""
    <div class="instructions-box">
        <h4>📸 كيفية إضافة صور الفريق</h4>
        <p>
            1️⃣ أنشئ مجلد <code>assets/team/</code> في المجلد الرئيسي للمشروع.<br>
            2️⃣ ضع الصور التالية بداخل المجلد:<br>
            &nbsp;&nbsp;• <code>goda.jpg</code> - صورة Goda Emad<br>
            &nbsp;&nbsp;• <code>ganaa.jpg</code> - صورة Ganaa Emad<br>
            &nbsp;&nbsp;• <code>manar.jpg</code> - صورة Manar Harby<br>
            3️⃣ قم بتحديث الصفحة وستظهر الصور فوراً وبأعلى جودة.
        </p>
        <p style="margin-top: 0.5rem; opacity: 0.8;">
            💡 المقاس الموصى به: <strong>500 × 500 بكسل</strong> (صورة مربعة).
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ✅ 7. تذييل الصفحة
    st.markdown("""
    <div class="page-footer">
        👥 فريق SmartRetriever | © 2026 | جميع الحقوق محفوظة
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# 🚀 تشغيل الصفحة
# ============================================================
if __name__ == "__main__":
    show()
