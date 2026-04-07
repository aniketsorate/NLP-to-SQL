from vanna_setup import agent

pairs = [
    ("How many patients?", "SELECT COUNT(*) FROM patients"),
    ("List doctors", "SELECT * FROM doctors"),
    ("Total revenue", "SELECT SUM(total_amount) FROM invoices"),
    ("Top 5 patients", "SELECT patient_id, SUM(total_amount) FROM invoices GROUP BY patient_id ORDER BY 2 DESC LIMIT 5"),
]

for q, sql in pairs:
    agent.memory.save_correct_tool_use(
        question=q,
        tool_name="RunSqlTool",
        tool_args={"sql": sql}
    )

print("Memory seeded!")