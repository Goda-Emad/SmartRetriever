<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=200&section=header&text=SmartRetriever&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=AI-Powered%20Procurement%20Intelligence&descAlignY=55&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=764ABA&center=true&vCenter=true&width=600&lines=Ask+questions.+Get+answers+from+your+contracts.;Powered+by+RAG+%2B+FAISS+%2B+Groq+LPU+Inference.;Built+for+smarter%2C+faster+procurement+decisions." alt="Typing SVG" />

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-00A98F?style=for-the-badge&logo=meta&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LPU%20Inference-F55036?style=for-the-badge&logo=lightning&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

</div>

---

## 📋 Overview

**SmartRetriever** is an intelligent document-retrieval and question-answering system built specifically for procurement workflows. Instead of manually digging through dozens of contracts, quotations, and quality reports, procurement teams can ask natural-language questions and get accurate, source-grounded answers instantly.

The system combines **semantic search (FAISS)**, **document chunking & reranking**, and a **large language model backend (Groq API)** to deliver fast, context-aware responses — all deployed through an intuitive Streamlit interface.

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="500">
</div>

---

## ✨ Key Features

- 🔍 **Semantic Document Retrieval** — Finds the most relevant contract, quotation, or report using vector similarity search (FAISS)
- 💬 **Conversational Q&A Interface** — Ask questions in natural language and get grounded, accurate answers
- 📊 **Analytics Dashboard** — Visual insights across suppliers, contracts, and quality metrics
- 📄 **Multi-Document Support** — Handles contracts, supplier evaluations, quotations, and quality reports (.docx)
- 🧩 **Modular RAG Pipeline** — Clean separation between retrieval, reranking, chunking, and generation layers
- ⚡ **Fast Inference** — Powered by Groq's LPU inference engine for near-instant responses
- 🔐 **Secure by Design** — API keys managed via environment secrets, never hardcoded

---

## 🎨 UI/UX Design

SmartRetriever is designed around a single principle: **procurement teams should never feel like they're "searching" — they should feel like they're conversing with an expert who already read every document.**

### Design Philosophy
- **Clarity over clutter** — Every screen surfaces one primary action at a time (ask, browse, or analyze), reducing cognitive load for non-technical procurement staff.
- **Trust through transparency** — Answers are always displayed alongside their source document, so users can verify AI-generated responses instantly.
- **Consistency** — A shared component library (`components/sidebar.py`, `components/chat_utils.py`) keeps navigation, spacing, and typography identical across every page.

### Experience by Page
| Page | UX Focus |
|---|---|
| 💬 **Chat** | Conversational interface with streaming responses and inline source citations, minimizing wait-time anxiety through animated loading states |
| 📄 **Documents** | Card-based document browser with category filters (contracts, quotations, policies, quality reports) for quick visual scanning |
| 📊 **Analytics** | Dashboard-style layout with charts for supplier performance and contract activity, prioritizing at-a-glance decision-making |

### Motion & Micro-interactions
Subtle animation is used purposefully — never decoratively — to guide attention and reduce perceived latency:
- **Loading states**: animated indicators while the RAG pipeline retrieves and reranks documents, keeping users informed during Groq inference
- **Transitions**: smooth fade/slide transitions between sidebar navigation states
- **Feedback micro-animations**: subtle highlight effects confirming a query was received or a document was selected

### Styling
All custom visual treatment lives in `styles/custom.css`, keeping design tokens (colors, spacing, animation timing) centralized and easy to theme without touching component logic.

---

## 🏗️ Architecture

```
User Query → Retriever (FAISS) → Reranker → Context Builder → Groq LLM → Answer
```

| Layer | Responsibility |
|---|---|
| `rag/retriever.py` | Semantic search & document retrieval from FAISS index |
| `rag/reranker.py` | Re-ranks retrieved chunks by relevance |
| `rag/chunking.py` | Splits documents into optimal semantic chunks |
| `rag/qa_engine.py` | Orchestrates the full RAG pipeline |
| `llm/groq_client.py` | Handles communication with Groq API |
| `database/` | FAISS index loading, embeddings, and document parsing |

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit
- **LLM Provider:** Groq API (LLaMA-based models)
- **Vector Store:** FAISS
- **Document Processing:** python-docx
- **Language:** Python 3.10+

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- A Groq API key ([console.groq.com](https://console.groq.com))

### Installation

```bash
# Clone the repository
git clone https://github.com/manarharbyabdelmoneam-cmd/SmartRetriever.git
cd SmartRetriever

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create `.streamlit/secrets.toml` and add your API key:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### Run Locally

```bash
streamlit run app.py
```

### Deploy on Streamlit Cloud

1. Push the repository to GitHub (secrets excluded via `.gitignore`)
2. Connect the repo at [share.streamlit.io](https://share.streamlit.io)
3. Add your `GROQ_API_KEY` under **App Settings → Secrets**
4. Deploy 🎉

---

## 📁 Project Structure

```
SmartRetriever/
├── app.py
├── pages/
├── components/
├── rag/
├── llm/
├── database/
├── core/
├── services/
├── utils/
├── knowledge_base/
├── scripts/
└── requirements.txt
```

---

## 🗺️ Roadmap

- [ ] Multi-language support (Arabic/English)
- [ ] Supplier performance scoring dashboard
- [ ] Export Q&A history as PDF reports
- [ ] Integration with ERP systems

---

## 👥 Meet the Team

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:667eea,100:764ba2&height=3&width=800" width="80%"/>
</div>

<div align="center">

### 🚀 The minds behind SmartRetriever

<table>
<tr>
<td align="center" width="33%">
<img src="https://avatars.dicebear.com/api/initials/GE.svg" width="90" style="border-radius:50%"/><br/>
<b>🧠 Goda Emad</b><br/>
<sub>AI / Backend Developer</sub><br/>
<sub>RAG Pipeline · LLM Integration · System Architecture</sub>
</td>
<td align="center" width="33%">
<img src="https://avatars.dicebear.com/api/initials/GE.svg" width="90" style="border-radius:50%"/><br/>
<b>⚙️ Ganna Emad</b><br/>
<sub>Backend Developer</sub><br/>
<sub>API Layer · Data Pipeline · System Integration</sub>
</td>
<td align="center" width="33%">
<img src="https://avatars.dicebear.com/api/initials/MH.svg" width="90" style="border-radius:50%"/><br/>
<b>🎨 Manar Harby</b><br/>
<sub>Frontend & Documentation</sub><br/>
<sub>UI/UX Design · Streamlit Interface · Docs</sub>
</td>
</tr>
</table>

*Built with focus, late nights, and a lot of ☕ by a team passionate about making AI genuinely useful for procurement teams.*

</div>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:667eea,100:764ba2&height=3&width=800" width="80%"/>
</div>

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/manarharbyabdelmoneam-cmd/SmartRetriever/issues).

---

<div align="center">

### ⭐ If this project helped you, consider giving it a star!

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:764ba2,100:667eea&height=120&section=footer" width="100%"/>

<sub>Made with ❤️ by **Goda Emad**, **Ganna Emad** & **Manar Harby** — for smarter procurement decisions</sub>

</div>
