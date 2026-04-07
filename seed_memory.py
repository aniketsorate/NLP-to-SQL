from vanna_setup import agent

pairs = [

# 🔹 PATIENT QUERIES
("How many patients do we have?",
 "SELECT COUNT(*) AS total_patients FROM patients"),

("List all patients",
 "SELECT * FROM patients"),

("Show patients from Pune",
 "SELECT * FROM patients WHERE city = 'Pune'"),

("How many male and female patients?",
 "SELECT gender, COUNT(*) FROM patients GROUP BY gender"),

# 🔹 DOCTOR QUERIES
("List all doctors and their specialization",
 "SELECT name, specialization FROM doctors"),

("Which doctor has the most appointments?",
 "SELECT doctor_id, COUNT(*) AS total FROM appointments GROUP BY doctor_id ORDER BY total DESC LIMIT 1"),

("Appointments per doctor",
 "SELECT doctor_id, COUNT(*) AS total_appointments FROM appointments GROUP BY doctor_id"),

# 🔹 APPOINTMENT QUERIES
("Show all completed appointments",
 "SELECT * FROM appointments WHERE status = 'Completed'"),

("Show appointments in last month",
 "SELECT * FROM appointments WHERE appointment_date >= DATE('now', '-1 month')"),

("Appointments by doctor",
 "SELECT doctor_id, COUNT(*) FROM appointments GROUP BY doctor_id"),

# 🔹 FINANCIAL QUERIES
("What is the total revenue?",
 "SELECT SUM(total_amount) AS total_revenue FROM invoices"),

("Show unpaid invoices",
 "SELECT * FROM invoices WHERE status != 'Paid'"),

("Average treatment cost",
 "SELECT AVG(cost) AS avg_cost FROM treatments"),

# 🔹 TIME-BASED QUERIES
("Appointments in last 3 months",
 "SELECT * FROM appointments WHERE appointment_date >= DATE('now', '-3 months')"),

("Monthly appointment trend",
 "SELECT strftime('%Y-%m', appointment_date) AS month, COUNT(*) FROM appointments GROUP BY month ORDER BY month")

]

for q, sql in pairs:
    agent.agent_memory.save_tool_usage(
        "RunSqlTool",
        {"sql": sql},
        q,
        {}
    )

print("Memory seeded successfully with 15 Q-SQL pairs!")