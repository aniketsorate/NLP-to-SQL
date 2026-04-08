import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("data/clinic.db")
cursor = conn.cursor()

# Drop tables if exist
tables = ["patients", "doctors", "appointments", "treatments", "invoices"]
for t in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {t}")

# Create tables
cursor.execute("""
CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    date_of_birth DATE,
    gender TEXT,
    city TEXT,
    registered_date DATE
)
""")

cursor.execute("""
CREATE TABLE doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT,
    department TEXT,
    phone TEXT
)
""")

cursor.execute("""
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    appointment_date DATETIME,
    status TEXT,
    notes TEXT
)
""")

cursor.execute("""
CREATE TABLE treatments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER,
    treatment_name TEXT,
    cost REAL,
    duration_minutes INTEGER
)
""")

cursor.execute("""
CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    invoice_date DATE,
    total_amount REAL,
    paid_amount REAL,
    status TEXT
)
""")

# Dummy data
cities = ["Mumbai", "Pune", "Delhi", "Bangalore", "Chennai"]
specializations = ["Dermatology", "Cardiology", "Orthopedics", "General", "Pediatrics"]

# Insert doctors
for i in range(15):
    cursor.execute("INSERT INTO doctors (name, specialization, department, phone) VALUES (?, ?, ?, ?)",
                   (f"Doctor {i}", random.choice(specializations), "Dept", "9999999999"))

# Insert patients
for i in range(200):
    cursor.execute("""
    INSERT INTO patients (first_name, last_name, email, phone, date_of_birth, gender, city, registered_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        f"Name{i}", f"Surname{i}",
        None if random.random() < 0.2 else f"user{i}@mail.com",
        None if random.random() < 0.2 else "9999999999",
        datetime.now() - timedelta(days=random.randint(7000, 20000)),
        random.choice(["M", "F"]),
        random.choice(cities),
        datetime.now() - timedelta(days=random.randint(0, 365))
    ))

# Insert appointments
for i in range(500):
    cursor.execute("""
    INSERT INTO appointments (patient_id, doctor_id, appointment_date, status, notes)
    VALUES (?, ?, ?, ?, ?)
    """, (
        random.randint(1, 200),
        random.randint(1, 15),
        datetime.now() - timedelta(days=random.randint(0, 365)),
        random.choice(["Scheduled", "Completed", "Cancelled", "No-Show"]),
        None if random.random() < 0.3 else "Notes"
    ))

# Insert treatments
for i in range(350):
    cursor.execute("""
    INSERT INTO treatments (appointment_id, treatment_name, cost, duration_minutes)
    VALUES (?, ?, ?, ?)
    """, (
        random.randint(1, 500),
        "Treatment",
        random.randint(50, 5000),
        random.randint(10, 120)
    ))

# Insert invoices
for i in range(300):
    total = random.randint(100, 5000)
    paid = random.randint(0, total)
    cursor.execute("""
    INSERT INTO invoices (patient_id, invoice_date, total_amount, paid_amount, status)
    VALUES (?, ?, ?, ?, ?)
    """, (
        random.randint(1, 200),
        datetime.now() - timedelta(days=random.randint(0, 365)),
        total,
        paid,
        random.choice(["Paid", "Pending", "Overdue"])
    ))

conn.commit()
conn.close()

print("Database created successfully!")