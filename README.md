# NL2SQL System

This project converts natural language questions into SQL queries and executes them on a healthcare dataset.

## Overview

The system takes a user question, generates a SQL query using an LLM, validates it, executes it on a SQLite database, and returns the result. For analytical queries, it can also generate charts automatically based on the result data.

## Features

- Natural language to SQL generation using LLM  
- SQL validation (only SELECT queries allowed)  
- SQLite database execution  
- Memory-based learning using Vanna  
- Result caching  
- Basic rate limiting  
- Automatic chart generation based on result structure  
- Automated testing using 20 evaluation queries  

## Tech Stack

- FastAPI  
- SQLite  
- Groq (LLM API)  
- Vanna (memory layer)  
- Plotly (visualization)  

## Project Structure

app/
  main.py
  routes/
    chat.py
  services/
    llm_service.py
    db_service.py
    chart_service.py
    memory_service.py
  core/
    config.py
    cache.py
    rate_limiter.py
  utils/
    sql_validator.py
    sql_extractor.py
  prompts/
    prompt_builder.py

scripts/
  setup_database.py
  seed_memory.py
  auto_test.py

data/
  clinic.db

## Setup

pip install -r requirements.txt
python -m scripts.setup_database
python -m scripts.seed_memory
uvicorn app.main:app --reload

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

## Notes

The system focuses on generating valid SQL and executing it correctly.  
Minor variations may occur depending on interpretation of business terms.  
These can be improved with better prompt tuning or additional memory examples.

## Author

Aniket Sorate


