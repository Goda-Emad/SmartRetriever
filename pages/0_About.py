import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="عن الفريق - SmartRetriever",
    page_icon="👥",
    layout="wide"
)

# ============================================================
# 🎨 2. تطبيق التنسيقات وإصلاح اتجاه النصوص (RTL Fixes)
# ============================================================
def apply_custom_css():
    st.markdown("""
    <style>
        /* 🌐 ضبط الاتجاه العام وتثبيت الخط */
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Cairo', sans-serif !important;
            direction: rtl !important;
            text-align: right !important;
        }

        /* 🏛️ الهيدر الرئيسي */
        .hero-banner {
            background: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%) !important;
            border: 1px solid #C7D2FE !important;
            border-radius: 16px;
            padding: 2.5rem 1.5rem;
            text-align: center !important;
            margin-bottom: 2rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
        }
        .hero-banner h1 {
            color: #1E1B4B !important;
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            margin-bottom: 0.5rem !important;
        }
        .hero-banner p {
            color: #4338CA !important;
            font-size: 1.1rem !important;
            margin: 0 !important;
        }

        /* 🃏 بطاقات أعضاء الفريق */
        .team-card {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 16px !important;
            padding: 1.8rem 1.2rem !important;
            text-align: center !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
            height: 100% !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: space-between !important;
        }
        .team-avatar {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #38BDF8;
            margin-bottom: 1rem;
        }
        .member-name {
            color: #0F172A !important;
            font-size: 1.3rem !important;
            font-weight: 700 !important;
            margin-bottom: 0.3rem !important;
        }
        .member-role {
            color: #0284C7 !important;
            font-size: 0.95rem !important;
            font-weight: 600 !important;
            margin-bottom: 0.8rem !important;
        }
        .member-bio {
            color: #334155 !important; /* لون داكن مريح للقراءة */
            font-size: 0.88rem !important;
            line-height: 1.7 !important;
            direction: rtl !important;
            text-align: center !important;
            margin-bottom: 1rem !important;
        }

        /* 🏷️ الوسوم (Badges / Tags) */
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            justify-content: center;
            margin-top: auto;
        }
        .tag-badge {
            background-color: #F1F5F9;
            color: #475569;
            font-size: 0.75rem;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 20px;
            border: 1px solid #E2E8F0;
        }

        /* 📊 بطاقات الإحصائيات والمواصفات */
        .spec-card {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 16px !important;
            padding: 1.5rem 1rem !important;
            text-align: center !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
        }
        .spec-title {
            color: #0284C7 !important;
            font-size: 1.8rem !important;
            font-weight: 800 !important;
            margin-bottom: 0.4rem !important;
        }
        .spec-subtitle {
            color: #0F172A !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
            margin-bottom: 0.3rem !important;
        }
        .spec-desc {
            color: #10B981 !important;
            font-size: 0.82rem !important;
            font-weight: 600 !important;
        }

        /* 📖 صندوق عن المشروع المعالج بالكامل */
        .info-box {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 16px !important;
            padding: 2rem !important;
            margin-top: 1.5rem !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
            direction: rtl !important;
            text-align: right !important;
        }
        .info-box h3 {
            color: #0F172A !important;
            font-size: 1.4rem !important;
            font-weight: 700 !important;
            margin-bottom: 1rem !important;
        }
        .info-box p {
            color: #334155 !important;
            font-size: 1rem !important;
            line-height: 1.8 !important;
            margin-bottom: 0.8rem !important;
            direction: rtl !important;
            text-align: right !important;
            unicode-bidi: isolate !important;
        }
    </style>
    """, unsafe_allow_html=True)

apply_custom_css()

# ============================================================
# 🏛️ 3. الهيدر الرئيسي (Banner)
# ============================================================
st.markdown("""
<div class="hero-banner">
    <h1>👥 فريق SmartRetriever</h1>
    <p>نظام استرجاع ذكي وتحليل للمستندات القانونية والعقود</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 👨‍💻 4. بطاقات أعضاء الفريق (3 Columns)
# ============================================================
col1, col2, col3 = st.columns(3)

# --- العضو الأول: Goda Emad ---
with col1:
    st.markdown("""
    <div class="team-card">
        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Goda" class="team-avatar" alt="Goda Emad">
        <div class="member-name">Goda Emad</div>
        <div class="member-role">👨‍💻 Full-Stack Developer</div>
        <div class="member-bio">
            مطور Python متخصص في بناء تطبيقات الذكاء الاصطناعي واسترجاع المعلومات. خبرة في تطوير Full-Stack و RAG Systems و Streamlit.
        </div>
        <div class="tag-container">
            <span class="tag-badge">#Python</span>
            <span class="tag-badge">#Streamlit</span>
            <span class="tag-badge">#RAG</span>
            <span class="tag-badge">#ChromaDB</span>
            <span class="tag-badge">#FAISS</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- العضو الثاني: Ganaa Emad ---
with col2:
    st.markdown("""
    <div class="team-card">
        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Ganaa" class="team-avatar" alt="Ganaa Emad">
        <div class="member-name">Ganaa Emad</div>
        <div class="member-role">🧠 AI / ML Engineer</div>
        <div class="member-bio">
            مهندسة ذكاء اصطناعي متخصصة في معالجة اللغة الطبيعية ونماذج التضمين. خبرة في Transformers و Embeddings و RAG Pipelines.
        </div>
        <div class="tag-container">
            <span class="tag-badge">#NLP</span>
            <span class="tag-badge">#Transformers</span>
            <span class="tag-badge">#Sentence-Transformers</span>
            <span class="tag-badge">#LLMs</span>
            <span class="tag-badge">#Groq</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- العضو الثالث: Manar Harby ---
with col3:
    st.markdown("""
    <div class="team-card">
        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Manar" class="team-avatar" alt="Manar Harby">
        <div class="member-name">Manar Harby</div>
        <div class="member-role">📊 Data Scientist</div>
        <div class="member-bio">
            عالمة بيانات متخصصة في تحليل البيانات وتصورها واستخراج المعلومات من المستندات. خبرة في Pandas و Plotly وتجهيز البيانات.
        </div>
        <div class="tag-container">
            <span class="tag-badge">#Pandas</span>
            <span class="tag-badge">#Plotly</span>
            <span class="tag-badge">#Data Analysis</span>
            <span class="tag-badge">#Document Processing</span>
            <span class="tag-badge">#Visualization</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# 📊 5. بطاقات الإحصائيات والمواصفات الفنية
# ============================================================
s_col1, s_col2, s_col3 = st.columns(3)

with s_col1:
    st.markdown("""
    <div class="spec-card">
        <div class="spec-title">16+</div>
        <div class="spec-subtitle">📁 مستندات مخزنة</div>
        <div class="spec-desc">جاهزة للاستعلام ✅</div>
    </div>
    """, unsafe_allow_html=True)

with s_col2:
    st.markdown("""
    <div class="spec-card">
        <div class="spec-title">MiniLM</div>
        <div class="spec-subtitle">🔍 نموذج التضمين</div>
        <div class="spec-desc">🌐 متعدد اللغات</div>
    </div>
    """, unsafe_allow_html=True)

with s_col3:
    st.markdown("""
    <div class="spec-card">
        <div class="spec-title">Llama 3.3</div>
        <div class="spec-subtitle">🤖 نموذج المحادثة</div>
        <div class="spec-desc">⚡ Groq Cloud API</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# 📖 6. قسم "عن المشروع" (مُعالج لاتجام النصوص RTL)
# ============================================================
st.markdown("""
<div class="info-box">
    <h3>📖 عن المشروع</h3>
    <p>
        <strong>SmartRetriever</strong> هو نظام ذكي لاسترجاع المستندات القانونية وإدارة العقود.
        يستخدم تقنيات <strong>RAG (Retrieval-Augmented Generation)</strong> و <strong>ChromaDB</strong>
        بناءً على محتوى المستندات المخزنة، مما يسمح بتوفير إجابات دقيقة وموثقة ومباشرة على استفسارات المستخدمين.
    </p>
    <p>
        🚀 تم تطوير المشروع بالكامل باستخدام <strong>Streamlit</strong> لتقديم واجهة سلسة، 
        ويتكامل بمرونة مع <strong>Groq API</strong> لتوليد إجابات سريعة وذكية.
    </p>
</div>
""", unsafe_allow_html=True)
