# 🔬 ResearchAI — AI Research Agent & Chat Assistant

> An AI-powered web application combining a smart Chat AI assistant
> with a Deep Research agent that searches the web and writes
> professional reports instantly.

🌐 **Live Demo:** [Click Here to Try ResearchAI](https://mirybegeyw6ccxybtxwyft.streamlit.app)
📂 **GitHub:** [nevedhya03-dotcom/AI_Agent-](https://github.com/nevedhya03-dotcom/AI_Agent-)

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Pages](#-pages)
- [How to Run](#-how-to-run)
- [API Keys](#-api-keys)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Project Stats](#-project-stats)
- [Built By](#-built-by)

---

## 📖 About the Project

ResearchAI is a full-stack AI web application built using
Python and Streamlit. It combines two powerful AI modes —
a **Chat AI assistant** and a **Deep Research agent** — into one
clean, modern interface with dark/light theme support.

This project demonstrates real-world skills in:
- LLM integration using Groq LLaMA3
- Agentic AI workflows using LangGraph
- Real-time web search using Tavily API
- Math solving using SymPy
- Flowchart generation using Mermaid.js
- Full-stack deployment on Streamlit Cloud

---

## ✨ Features

### 💬 Chat AI
* Ask any question — science, history, technology, coding
* Solve math equations step by step using SymPy
* Generate flowcharts and diagrams just by describing them
* Multi-turn conversations with full chat history maintained

### 🔍 Deep Research Agent
* AI agent searches 5+ live web sources automatically
* Writes structured professional research reports
* Download reports as PDF with one click
* Powered by LangGraph multi-step agentic workflow

### 🎨 UI / UX
* Dark and Light theme toggle (full page)
* Animated hero section and feature cards
* Pill-shaped fixed navigation bar
* Inverted footer design based on theme
* Smooth transitions and hover animations

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Core programming language |
| 🦜 LangChain | AI framework connecting all components |
| 🕸️ LangGraph | Multi-step agentic workflow builder |
| 🤖 Groq LLaMA3 | Ultra-fast LLM for chat and report writing |
| 🔍 Tavily API | Real-time live web search |
| 🚀 Streamlit | Web UI and cloud deployment |
| 📄 ReportLab | Professional PDF report generation |
| 🧮 SymPy | Mathematical equation solving |
| 📊 Mermaid.js | Flowchart and diagram rendering |

---

## 📄 Pages

| Page | Description |
|------|-------------|
| 🏠 Home | Landing page with features, stats and pipeline overview |
| 💬 Chat AI | Interactive AI chat with math and flowchart support |
| 🔍 Research | Deep web research agent with PDF export |
| ❓ How it Works | Tech stack and agent pipeline explained |

---

## 🚀 How to Run

### Step 1 — Clone the Repository
```bash
git clone https://github.com/nevedhya03-dotcom/AI_Agent-.git
cd AI_Agent-
```

### Step 2 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Set Up API Keys
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
```

### Step 4 — Run the App
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🔑 API Keys

Both API keys are completely free to get:

| API | Link | Free Limit |
|-----|------|------------|
| Groq API | [console.groq.com](https://console.groq.com) | Unlimited (free tier) |
| Tavily API | [app.tavily.com](https://app.tavily.com) | 1000 searches/month |

---

## 📁 Project Structure

```
AI_Agent-/
│
├── app.py              ← Main Streamlit UI (all pages + theme)
├── agent_core.py       ← AI agent + chat + math + flowchart logic
├── requirements.txt    ← All Python dependencies
├── .env                ← API keys (never push to GitHub)
├── .gitignore          ← Ignores .env and pycache
└── README.md           ← You are here!
```

---

## ⚙️ How It Works

### 💬 Chat AI Pipeline

```
User Message
      ↓
Groq LLaMA3 processes with full chat history
      ↓
Math keywords detected?
      → SymPy solves the equation precisely
Flowchart requested?
      → Mermaid.js renders diagram live
      ↓
Answer shown in chat bubble instantly
```

### 🔍 Research Agent Pipeline

```
User enters a research topic
      ↓
LangGraph agent starts workflow
      ↓
Tavily API searches 5+ live web sources
      ↓
Groq LLaMA3 reads and synthesizes all results
      ↓
Structured report generated with sections:
  - Executive Summary
  - Key Findings
  - Detailed Analysis
  - Conclusion
      ↓
User downloads report as PDF
```

---

## 📊 Project Stats

| Metric | Value |
|--------|-------|
| ⚡ Average response time | ~30 seconds |
| 🌐 Web sources per research | 5+ live sources |
| 💬 Chat turns supported | Unlimited |
| 📄 Export formats | PDF |
| 🎨 Themes | Dark + Light |
| 💰 Cost to use | 100% Free |

---

## 📦 Requirements

```
langchain
langchain-community
langchain-groq
langgraph
tavily-python
streamlit
python-dotenv
reportlab
sympy
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🖥️ Screenshots

| Home Page | Chat AI | Research Page |
|-----------|---------|---------------|
| Dark theme hero with stats | Multi-turn AI chat | Deep research with PDF |

*(Add your own screenshots here)*

---

## 🧠 What I Learned Building This

- How to build **multi-step AI agents** using LangGraph
- Integrating **real-time web search** with LLM workflows
- Rendering **Mermaid diagrams** inside Streamlit
- Building **full-stack AI apps** with proper UI/UX
- Deploying AI applications on **Streamlit Cloud**
- Managing **API keys securely** using .env files

---

## 👩‍💻 Built By

**Nevedhya Patni**

Computer Science @ Vellore Institute of Technology (CGPA 8.5)

- 📧 Email: nevedhya03@gmail.com
- 💼 GitHub: [github.com/nevedhya03-dotcom](https://github.com/nevedhya03-dotcom)
- 🔬 Live App: [mirybegeyw6ccxybtxwyft.streamlit.app](https://mirybegeyw6ccxybtxwyft.streamlit.app)

---

## 📜 License

This project is open source and available under the
[MIT License](LICENSE).

---

*Built with ❤️ using Python, LangChain, LangGraph, Groq, Tavily and Streamlit*