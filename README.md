# 📬 Enron Email Response Generator & Summarizer (GenAI Assignment)

This repository contains the solution to the **TATA Communications Data Science & GenAI Assignment**. The objective was to build an intelligent system that performs **email summarization**, **response generation**, and **API deployment** using **Retrieval-Augmented Generation (RAG)** and **locally hosted LLMs via Ollama** on the Enron email dataset.

---

## 🧠 Solution Overview

We approached the assignment in five tasks:

| Task | Description |
|------|-------------|
| ✅ Task 1 | Dataset Exploration & Preprocessing |
| ✅ Task 2 | Email Summarization using LLM |
| ✅ Task 3 | Contextual Response Generation via RAG |
| ✅ Task 4 | Manual Evaluation of Model Outputs |
| ✅ Task 5 | API Deployment using FastAPI (Bonus) |

---

## 📂 Directory Structure

```bash
email-ai-summarizer/
│
├── app/                           # ✅ Task 5: FastAPI app (modular)
├── config/                        # Shared paths and settings
├── engine/                        # Embedding, vector store, prompt templates
├── models/                        # Pydantic models/schemas
├── routers/                       # API routes (summarization, response)
│
├── data/
│   └── filtered_enron_emails.csv  # Filtered emails (based on email types, not length)
│
├── faiss_index/                   # 🔒 FAISS vector index (excluded from Git)
│
├── notebooks/                     # Jupyter Notebooks for Tasks 1–4
│   ├── dataset_exploration_and_preprocessing.ipynb  # Task 1
│   ├── email_summarization.ipynb                    # Task 2
│   └── response_generation_task.ipynb               # Task 3 & 4
│
├── requirements.txt
├── .gitignore
└── README.md

## ✅ Tasks Summary

### 🔍 Task 1: Dataset Exploration & Preprocessing
- Performed initial analysis on the Enron dataset.
- Identified **relevant email topics** such as:
  - 📅 Meeting Requests
  - 📌 Project Updates
  - 📈 Status Follow-ups
- Filtered and saved emails under `filtered_enron_emails.csv`.
- 📌 **Filtering was based on email types, not character length.**

---

### ✂️ Task 2: Email Summarization
- Utilized locally hosted LLMs (via **Ollama**) to generate **concise summaries**.
- Focused on clarity, relevance, and capturing essential intent.
- Implemented within `email_summarization.ipynb`.

---


### 💬 Task 3: Contextual Response Generation (RAG)
- Built a RAG pipeline using:
  - **Ollama** for embedding + generation
  - **FAISS** for semantic document retrieval
- Only used emails with **length ≥ 500 characters** as single chunks (no overlap).
- Vector store built using `chromadb`.
- Integrated in `response_generation_task.ipynb`.

---

### 📊 Task 4: Evaluation
- Manually verified outputs based on:
  - Relevance
  - Fluency
  - Alignment with context
- All evaluation and debugging steps logged in the notebook.


---

### 🚀 Task 5 (Bonus): API Deployment

- Deployed using **FastAPI** with a **modular architecture**.
- Organized under `/app` directory.
- API endpoints support:
  - `/summarize` - Summarize email body
  - `/respond` - Generate email reply based on context


## ⚙️ Environment & Setup

- **Python Version**: 3.12.0

- 📦 Install requirements:

```bash
pip install -r requirements.txt

🚀 Start FastAPI server:

uvicorn app.main:app --reload


## ⚠️ Important Notes

| **Item**                      | **Status**                                 |
|------------------------------|---------------------------------------------|
| `data/emails.csv` (original dataset) | ❌ Not pushed to Git                     |
| `faiss_index/`                 | ❌ Not included in Git                    |
| `data/filtered_enron_emails.csv`   | ❌ Not included in Git      |


## 🧱 How to Rebuild the RAG Pipeline

1. **Clone the repository and install dependencies:**

```bash
git clone <repo-url>
cd email-ai-summarizer
pip install -r requirements.txt


## 🏁 Final Thoughts

This solution demonstrates how **GenAI** and **local LLMs** can be effectively used for:

- Intelligent summarization  
- Context-aware response generation  
- Scalable deployment using APIs  
