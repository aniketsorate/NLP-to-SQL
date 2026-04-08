from app.services.memory_service import save_memory


pairs = [

# -------------------------------
# 🔹 PATIENT QUERIES
# -------------------------------
("How many patients do we have?",
 "SELECT COUNT(*) FROM patients"),

("List all patients",
 "SELECT * FROM patients"),

("Show patients from Pune",
 "SELECT * FROM patients WHERE city = 'Pune'"),

("How many male and female patients?",
 "SELECT gender, COUNT(*) FROM patients GROUP BY gender"),

# -------------------------------
# 🔹 DOCTOR QUERIES
# -------------------------------
("List all doctors and their specializations",
 "SELECT name, specialization FROM doctors"),

("Which doctor has the most appointments?",
 "SELECT doctor_id, COUNT(*) FROM appointments GROUP BY doctor_id ORDER BY COUNT(*) DESC LIMIT 1"),

("Appointments per doctor",
 "SELECT doctor_id, COUNT(*) FROM appointments GROUP BY doctor_id"),

# -------------------------------
# 🔹 APPOINTMENT QUERIES
# -------------------------------
("Show all completed appointments",
 "SELECT * FROM appointments WHERE status = 'Completed'"),

("Show appointments for last month",
 "SELECT * FROM appointments WHERE appointment_date >= DATE('now','-1 month')"),

("Appointments in last 3 months",
 "SELECT * FROM appointments WHERE appointment_date >= DATE('now','-3 months')"),

# -------------------------------
# 🔹 FINANCIAL QUERIES
# -------------------------------
("What is the total revenue?",
 "SELECT SUM(total_amount) FROM invoices"),

("Show unpaid invoices",
 "SELECT * FROM invoices WHERE status != 'Paid'"),

("Average treatment cost",
 "SELECT AVG(cost) FROM treatments"),

# -------------------------------
# 🔹 TIME-BASED QUERIES
# -------------------------------
("Monthly appointment trend",
 "SELECT strftime('%Y-%m', appointment_date) AS month, COUNT(*) FROM appointments GROUP BY month"),

("Top 5 patients by spending",
 "SELECT patient_id, SUM(total_amount) FROM invoices GROUP BY patient_id ORDER BY 2 DESC LIMIT 5")
]


for q, sql in pairs:
    save_memory(q, sql)

print("✅ Memory seeded")

print("Memory seeded successfully with 15 Q-SQL pairs!")