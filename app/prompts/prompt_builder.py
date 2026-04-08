def build_sql_prompt(question: str, memory_examples: str = "") -> str:
    return f"""
You are an expert SQL generator.

Generate a valid SQLite SELECT query.

Rules:
- Only SELECT queries
- No explanation
- Use SQLite syntax
- Use strftime for dates
- Use COUNT(*) for counts

Schema:

patients(id, first_name, last_name, email, phone, date_of_birth, gender, city, registered_date)
doctors(id, name, specialization, department, phone)
appointments(id, patient_id, doctor_id, appointment_date, status, notes)
treatments(id, appointment_id, treatment_name, cost, duration_minutes)
invoices(id, patient_id, invoice_date, total_amount, paid_amount, status)

Examples:
{memory_examples}

Question: {question}
"""