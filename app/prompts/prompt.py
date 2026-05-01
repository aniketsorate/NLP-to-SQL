from langchain_core.prompts import ChatPromptTemplate

sql_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert SQL generator.\n\n"
     "Generate a valid SQLite SELECT query.\n\n"
     "Rules:\n"
     "- Only SELECT queries\n"
     "- No explanation\n"
     "- Use SQLite syntax\n"
     "- Use strftime for dates\n"

    ),
    
    ("human",
     "Schema:\n\n"
     "patients(id, first_name, last_name, email, phone, date_of_birth, gender, city, registered_date)\n"
     "doctors(id, name, specialization, department, phone)\n"
     "appointments(id, patient_id, doctor_id, appointment_date, status, notes)\n"
     "treatments(id, appointment_id, treatment_name, cost, duration_minutes)\n"
     "invoices(id, patient_id, invoice_date, total_amount, paid_amount, status)\n\n"
     "Question: {question}"
    )
])


code_prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are a data analyst who writes clean Python visualization code. "
     "Only return executable code. Use matplotlib only. "
     "Use dataframe variable `df`."
    ),
    
    ("human", 
     "Question: {question}\n\n"
     "Dataset schema: {schema}\n\n"
     "Column types: {dtypes}\n\n"
     "Sample data:\n{sample}\n\n"
     "Generate Python code to create a meaningful graph."
    )
])