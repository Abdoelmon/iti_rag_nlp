# 🧠 NLP PDF RAG System (Multi-User, Production Ready)

A Retrieval-Augmented Generation (RAG) system that allows users to:

- 📄 Upload their own PDF
- 🔎 Ask questions about the PDF
- 💬 Store conversations
- 👥 Support multiple users (each with their own index)

Built with:

- FastAPI (Backend API)
- Streamlit (Frontend UI)
- FAISS (Vector Store)
- HuggingFace Embeddings
- Groq LLM
- SQLite (Conversation Storage)

---

#  Project Architecture
User → Streamlit UI → FastAPI → RAG Engine

↓

Upload PDF → Build FAISS Index (per user)

↓

Ask Question → Retrieve → LLM → Save Conversation


---

# ⚙️ 1️⃣ Requirements

## Python Version

Recommended: Python 3.10


Check version:
```
python --version
```


---

# 📦 2️⃣ Create Virtual Environment

## Windows
```
conda create -n rag python=3.10
```
```
conda activate rag
```

---

# 📥 3️⃣ Install Dependencies
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```

---

# 🔐 4️⃣ Setup Environment Variables

Create a file named:

.env


Add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here


---

# 🗄 5️⃣ Database Setup

The database is automatically created on first run.

SQLite file:
rag.db


No manual setup required.

---

# 📂 6️⃣ Create Required Folders

Make sure these folders exist:

storage/uploads

storage/indexes

If not, create them manually.

---
# 🚀 7️⃣ Run FastAPI Server

From project root:
```
uvicorn app.api:app --reload
```

If successful, you should see:

Uvicorn running on http://127.0.0.1:8000


Open Swagger docs:

http://127.0.0.1:8000/docs


---

# 🎨 8️⃣ Run Streamlit UI

Open a new terminal (while API is running):
```
streamlit run streamlit_app.py
```

It will open:

http://localhost:8501


---

# 🧪 How to Use the System

## Step 1: Enter User ID

Each user must enter a unique user ID.

Example:
abdo123


---

## Step 2: Upload PDF

- Upload your NLP PDF
- Click Upload
- The system will:
  - Save PDF
  - Split text
  - Generate embeddings
  - Build FAISS index
  - Save index for that user

Index path:
storage/indexes/<user_id>/


---

## Step 3: Ask Questions

Enter a question like:

- What is NLP?
- Explain tokenization.
- What is text preprocessing?
- Difference between stemming and lemmatization?

The system will:

1. Load the user's FAISS index
2. Retrieve relevant chunks
3. Send context to LLM
4. Return answer
5. Store conversation in database

---

# 💬 Conversation Storage

Stored in SQLite table:
conversations


Schema:

| id | user_id | question | answer |
|----|---------|----------|--------|

---

# 🔎 API Endpoints

## Upload PDF
POST /upload


Form Data:

- user_id
- file (PDF)

---

## Ask Question
POST /ask


Query Params:

- user_id
- question

---

# 🧠 RAG Pipeline Details

## Embedding Model
sentence-transformers/all-MiniLM-L6-v2

## Vector Store

FAISS (L2 Distance)


## Retrieval
MMR
k=3


## LLM
openai/gpt-oss-120b (via Groq)


---

# 🛠 Troubleshooting

## 1️⃣ FAISS Error

If FAISS fails to install:
```
pip install faiss-cpu
```

---

## 2️⃣ GROQ API Error

Make sure:

- .env exists
- API key is correct
- Environment variable is loaded

---

## 3️⃣ Port Already in Use

Change port:
```
uvicorn app.api:app --reload --port 8001
```


---

# 📈 Performance Notes

- First PDF upload may take 10–30 seconds
- Larger PDFs take longer
- Index loading is fast after creation
- Embedding runs locally
- LLM runs on Groq servers

---



# 👨‍💻 Author

Built as a full Production RAG system project.

---

# 🎯 Summary

You now have:

- Multi-user RAG system
- Dynamic PDF ingestion
- Per-user FAISS index
- Conversation persistence
- API + UI
- Production-ready architecture (without Docker)

---

🔥 Ready for deployment.