# 📬 Enron Email Response Generator & Summarizer (Data Science and Generative AI Assignment)

This repository contains the solution to the **TATA Communications Data Science & GenAI Assignment**. The objective was to build an intelligent system that performs **email summarization**, **response generation**, and **API deployment** (with **FastAPI**) using **Pre-trained LLMs**, **Retrieval-Augmented Generation (RAG)** and **locally hosted LLMs via Ollama** on the Enron email dataset.

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
contextual-email-retrieval-api/
│
├── app/                           # ✅ Task 5: FastAPI app (modular)
├     config/                        # Shared paths and settings
├     engine/                        # Embedding, vector store, prompt templates
├     models/                        # Pydantic models/schemas
├     routers/                       # API routes (summarization, generations)
│     main.py  
├── data/                           # this dir is excluded from git
│   └── filtered_enron_emails.csv  # Filtered emails (based on email types)
│
├── faiss_index/                   # FAISS vector index (excluded from Git)
│
├── notebooks/                     # Jupyter Notebooks for Tasks 1–4
│   ├── dataset_exploration_and_preprocessing.ipynb  # Task 1
│   ├── email_summarization.ipynb                    # Task 2
│   └── response_generation_task.ipynb               # Task 3 
│   |-- model_evaluation.ipynb                       # Task 4
|
├── requirements.txt
├── .gitignore
└── README.md


## **✅ Tasks Summary**

### 🔍 Task 1: Dataset Exploration & Preprocessing
- Performed initial analysis on the Enron dataset.

- Identified **relevant email topics** such as:
  - Meeting Requests
  - Project Updates
  - Status Follow-ups

- Filtered and saved emails under `filtered_enron_emails.csv`.
- **Filtering was based on email types**
- Implemented within `notebooks/dataset_exploration_and_preprocessing.ipynb`

---

### ✂️ Task 2: Email Summarization
- Utilized locally pre-trained LLMs such as `bart-large-cnn`, `pegasus-xsum` to generate **concise summaries**.
- Focused on clarity, relevance, and capturing essential intent.
- Implemented within `notebooks/email_summarization.ipynb`.

---


### 💬 Task 3: Contextual Response Generation (RAG)
- Built a RAG-based Response Generation using:
  - **Ollama** for embedding + generation
  - **FAISS** for semantic document retrieval

- Only used emails with **length ≥ 500 characters** as single chunks (with 50 overlap).
- Vector store built using `faiss-index`.
- Implemented within `notebooks/response_generation_task.ipynb`.

---

### 📊 Task 4: Evaluation
- Manually verified outputs based on:
  - Relevance
  - Fluency
  - Alignment with context
- All evaluations and thoughts are disscussed on `notebooks/model_evaluation.ipynb`.


---

### 🚀 Task 5 (Bonus): API Deployment

- Deployed using **FastAPI** with a **modular architecture**.
- Organized under `/app` directory.
- API endpoints support:
  - `/generate-email-response` -  Generate responses for common email types. 


## ⚙️ Environment & Setup

- **Python Version**: 3.12.0


## ⚠️ Important Notes

| **Item**                              | **Status**                  |
|---------------------------------------|-----------------------------|
| `data/emails.csv` (original dataset)  | ❌ Not pushed to Git        |
| `faiss_index/`                        | ❌ Not included in Git      |
| `data/filtered_enron_emails.csv`      | ❌ Not included in Git      |


## 🧱 How to Rebuild this project

1. **Clone the repository and install dependencies:**

```bash

git clone <repo-url>
cd contextual-email-retrieval-api

- Create a venv 
  - conda create -p venv python==3.12.0

- Activate venv
  - source activate venv/

- 📦 Install requirements:

```bash
pip install -r requirements.txt

🚀 Start FastAPI server:

uvicorn app.main:app --reload


## 🏁 Final Thoughts

This solution demonstrates how **GenAI** and **local LLMs** can be effectively used for:

- Intelligent summarization  
- Context-aware response generation  
- Scalable deployment using APIs  


## 🔮 Future Enhancements
- Move from in-memory to scalable NoSQL vector DBs

- Use high-end GPU machines to accelerate embedding creation

- Integrate more advanced LLMs and text-embedding models

- Deploy APIs to the cloud for broader business use cases