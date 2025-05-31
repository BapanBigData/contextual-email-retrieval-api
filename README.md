# 📬 Enron Email Response Generator & Summarizer (GenAI Assignment)

This repository is submitted as a solution to the **TATA Communications Data Science & GenAI Assignment**. It demonstrates the application of Generative AI and Retrieval-Augmented Generation (RAG) techniques for email understanding, summarization, and contextual response generation using the Enron dataset.

---

## 📁 Project Structure

```bash
email-ai-summarizer/
│
├── app/                          # FastAPI app for deployment
├── config/                       # Path utilities and shared config
├── engine/                       # Core RAG logic: embeddings, prompts, vector store
├── models/                       # Pydantic schemas
├── routers/                      # API routes (modular)
│
├── data/
│   ├── emails.csv                # Original dataset (not included in Git)
│   └── filtered_enron_emails.csv  # Filtered emails (based on selected email types)
│
├── faiss_index/                  # FAISS vector index (not pushed to Git)
│
├── notebooks/                    # Jupyter Notebooks (Tasks 1–4)
│   ├── dataset_exploration_and_preprocessing.ipynb      # ✅ Task 1
│   ├── email_summarization.ipynb                        # ✅ Task 2
│   └── response_generation_task.ipynb                   # ✅ Task 3 & 4
│
├── requirements.txt
├── .gitignore
└── README.md

✅ Tasks Completed
Task 1: Dataset Exploration & Preprocessing
Notebook: notebooks/dataset_exploration_and_preprocessing.ipynb

Loaded and explored the Enron dataset.

Identified a set of relevant email_types such as:

Meeting requests

Project updates

Status follow-ups

Filtered emails based on those types (not by length).

Saved the processed file as filtered_enron_emails.csv.

Task 2: Email Summarization
Notebook: notebooks/email_summarization.ipynb

Used local LLMs (via Ollama) to generate meaningful summaries of selected emails.

Summarization was tuned for clarity, relevance, and brevity.

Task 3: Response Generation
Notebook: notebooks/response_generation_task.ipynb

Built a Retrieval-Augmented Generation (RAG) pipeline for generating context-aware replies to filtered emails.

Key components:

FAISS Vector Store for efficient document retrieval.

Local LLMs for generating responses from relevant chunks.

Task 4: Evaluation
Evaluated generated responses and summaries manually.

Checked for:

Relevance

Fluency

Appropriateness based on email topic and context.

Task 5 (Bonus): API Deployment
Deployed the system using FastAPI in a modular fashion under the app/ directory.

Supports endpoints for:

Email summarization

Email response generation

✅ To run the API:

bash
Copy
Edit
uvicorn app.main:app --reload
⚙️ Environment Details
Python Version: 3.12.0

All required packages are listed in:

bash
Copy
Edit
requirements.txt
Install them using:

bash
Copy
Edit
pip install -r requirements.txt
⚠️ Important Notes
🔒 emails.csv (original full dataset) is not pushed to the Git repository.

🔒 faiss_index/ directory is also excluded to avoid pushing large binary files.

✅ filtered_enron_emails.csv is a filtered version based on email types, not character length.

📌 How to Rebuild the RAG Pipeline
Clone the repo & install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Prepare the data:

Make sure filtered_enron_emails.csv is in the data/ folder.

Embed documents using Ollama:

Follow the logic in engine/embedding_func.py to compute embeddings via Ollama.

Build FAISS index:

Use engine/vectorstore.py to create a vector store of embedded documents.

Start the API:

bash
Copy
Edit
uvicorn app.main:app --reload
🙌 Final Remarks
This project provides an end-to-end system that leverages GenAI for:

Summarizing long-form emails

Generating responses intelligently via context retrieval