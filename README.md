# 🚀 LLM-Based Natural Language to SQL & Visualization System

An end-to-end **AI-powered data assistant** that converts natural language queries into SQL, executes them on a database, and generates visual insights automatically.

---

## 📌 Overview

This system processes user queries through a multi-step pipeline:
Natural Language → SQL Generation → Validation → Database Execution → Visualization


It leverages LLMs to understand user intent, generate accurate SQL queries, and produce meaningful visualizations from the results.

---

## ✨ Features

- 🔹 Natural Language → SQL using LLM (Groq )
- 🔹 SQL validation (only safe SELECT queries allowed)
- 🔹 SQLite database execution
- 🔹 Multi-step API pipeline:
  - `/chat` → Generate SQL  
  - `/result` → Execute SQL  
  - `/visualize` → Generate chart  
- 🔹 Automatic visualization using LLM-generated plotting logic
- 🔹 Interactive frontend using Streamlit
- 🔹 Result caching for faster responses
- 🔹 Rate limiting for API safety
- 🔹 Modular service-based architecture
- 🔹 Async FastAPI endpoints

---

## 🛠 Tech Stack

- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **LLM:** Groq / OpenRouter  
- **Framework:** LangChain  
- **Database:** SQLite  
- **Visualization:** Matplotlib  
- **Memory Layer:** Vanna (optional / experimental)

---

## 📂 Project Structure

```
nl2sql-project/
│
├── app/
│   ├── main.py
│
│   ├── routes/
│   │   ├── chat.py
│   │   ├── result.py
│   │   └── visualize.py
│
│   ├── services/
│   │   ├── llm_service.py
│   │   ├── db_service.py
│   │   ├── chart_service.py
│   │   └── memory_service.py
│
│   ├── core/
│   │   ├── config.py
│   │   ├── cache.py
│   │   └── rate_limiter.py
│
│   ├── utils/
│   │   ├── sql_validator.py
│   │   └── sql_extractor.py
│
│   └── prompts/
│       └── prompt.py
│
├── scripts/
│   ├── setup_database.py
│   ├── seed_memory.py
│   └── auto_test.py
│
├── data/
│   └── clinic.db
│
├── streamlit_app.py   
├── requirements.txt
├── README.md
└── .env

```

## Setup

pip install -r requirements.txt
python -m scripts.setup_database
python -m scripts.seed_memory
uvicorn app.main:app --reload
streamlit run streamlit_app.py

## API Usage

Open:
http://127.0.0.1:8000/docs

Example request:
{
  "question": "How many patients do we have?"
}

## Testing

python -m scripts.auto_test

This generates RESULTS_RAW.md with SQL, outputs, and execution details.

## Evaluation Summary

- Total Queries: 20  
- Fully Correct: 16  
- Partially Correct: 4  
- Failed: 0  

All queries generated valid SQL and executed successfully.  
Some differences are due to semantic interpretation (e.g., meaning of "revenue" or "unpaid") rather than SQL errors.

## Limitations
LLM-generated code may occasionally contain syntax errors
Visualization depends on model interpretation
Security risks exist when executing generated code (can be improved with structured outputs)

## Notes

The system focuses on generating valid SQL and executing it correctly.  
Minor variations may occur depending on interpretation of business terms.  
These can be improved with better prompt tuning or additional memory examples.

## Author

Aniket Sorate


