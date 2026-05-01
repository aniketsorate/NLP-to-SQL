# NL2SQL Test Results

# Some queries may produce slightly different outputs depending on data distribution and prompt interpretation. The system is designed to improve over time using memory-based learning.

## Q1: How many patients do we have?

**SQL:**
```sql
SELECT COUNT(*) FROM patients
```

**Execution Time:** 0.0s

**Result Sample:**
[[200]]

**Status:** PASS

---

## Q2: List all doctors and their specializations

**SQL:**
```sql
SELECT 
  name, 
  specialization 
FROM 
  doctors
```

**Execution Time:** 0.01s

**Result Sample:**
[['Doctor 0', 'Dermatology'], ['Doctor 1', 'Dermatology'], ['Doctor 2', 'Dermatology'], ['Doctor 3', 'Pediatrics'], ['Doctor 4', 'Dermatology']]

**Status:** PASS

---

## Q3: Show me appointments for last month

**SQL:**
```sql
SELECT 
    a.id,
    p.first_name,
    p.last_name,
    d.name AS doctor_name,
    a.appointment_date,
    a.status,
    a.notes
FROM 
    appointments a
JOIN 
    patients p ON a.patient_id = p.id
JOIN 
    doctors d ON a.doctor_id = d.id
WHERE 
    strftime('%Y-%m', a.appointment_date) = strftime('%Y-%m', datetime('now', '-1 month'))
```

**Execution Time:** 0.02s

**Result Sample:**
[[11, 'Name15', 'Surname15', 'Doctor 14', '2026-03-27 17:18:20.164822', 'Scheduled', 'Notes'], [15, 'Name41', 'Surname41', 'Doctor 12', '2026-03-04 17:18:20.164822', 'Completed', 'Notes'], [29, 'Name8', 'Surname8', 'Doctor 6', '2026-03-18 17:18:20.164822', 'Scheduled', None], [55, 'Name75', 'Surname75', 'Doctor 4', '2026-03-12 17:18:20.164822', 'Completed', None], [56, 'Name16', 'Surname16', 'Doctor 8', '2026-03-29 17:18:20.164822', 'Scheduled', 'Notes']]

**Status:** PASS

---

## Q4: Which doctor has the most appointments?

**SQL:**
```sql
SELECT 
    d.name, 
    COUNT(*) as appointment_count
FROM 
    appointments a
JOIN 
    doctors d ON a.doctor_id = d.id
GROUP BY 
    d.name
ORDER BY 
    appointment_count DESC
LIMIT 1
```

**Execution Time:** 0.0s

**Result Sample:**
[['Doctor 10', 45]]

**Status:** PASS

---

## Q5: What is the total revenue?

**SQL:**
```sql
SELECT COUNT(*) AS total_revenue
FROM invoices
WHERE status = 'paid'
```

**Execution Time:** 0.0s

**Result Sample:**
[[0]]

**Status:** Fail

---

## Q6: Show revenue by doctor

**SQL:**
```sql
SELECT 
  d.name, 
  SUM(i.total_amount - i.paid_amount) as revenue
FROM 
  invoices i
  JOIN appointments a ON i.patient_id = a.patient_id
  JOIN doctors d ON a.doctor_id = d.id
GROUP BY 
  d.name
```

**Execution Time:** 0.01s

**Result Sample:**
[['Doctor 0', 60248.0], ['Doctor 1', 81976.0], ['Doctor 10', 88540.0], ['Doctor 11', 73362.0], ['Doctor 12', 50037.0]]

**Status:** Pass

---

## Q7: How many cancelled appointments last quarter?

**SQL:**
```sql
SELECT COUNT(*) 
FROM appointments 
WHERE status = 'cancelled' AND strftime('%Y-%m', appointment_date) BETWEEN strftime('%Y-%m', '2022-10-01') AND strftime('%Y-%m', '2022-12-31')
```

**Execution Time:** 0.04s

**Result Sample:**
[[0]]

**Status:** Fail

---

## Q8: Top 5 patients by spending

**SQL:**
```sql
SELECT first_name, last_name, SUM(total_amount) as total_spent
FROM patients
JOIN invoices ON patients.id = invoices.patient_id
GROUP BY patients.id
ORDER BY total_spent DESC
LIMIT 5
```

**Execution Time:** 0.01s

**Result Sample:**
[['Name142', 'Surname142', 17342.0], ['Name89', 'Surname89', 15463.0], ['Name164', 'Surname164', 15210.0], ['Name173', 'Surname173', 13232.0], ['Name119', 'Surname119', 12387.0]]

**Status:** PASS

---

## Q9: Average treatment cost by specialization

**SQL:**
```sql
SELECT 
    d.specialization, 
    AVG(t.cost) AS average_cost
FROM 
    treatments t
JOIN 
    appointments a ON t.appointment_id = a.id
JOIN 
    doctors d ON a.doctor_id = d.id
GROUP BY 
    d.specialization
```

**Execution Time:** 0.87s

**Result Sample:**
[['Dermatology', 2531.740932642487], ['General', 2475.054054054054], ['Orthopedics', 2379.535714285714], ['Pediatrics', 2523.7818181818184]]

**Status:** PASS

---

## Q10: Show monthly appointment count for the past 6 months

**SQL:**
```sql
SELECT 
    strftime('%Y-%m', appointment_date) AS month,
    COUNT(*) AS appointment_count
FROM 
    appointments
WHERE 
    appointment_date >= DATE('now', '-6 months')
GROUP BY 
    month
ORDER BY 
    month
```

**Execution Time:** 0.01s

**Result Sample:**
[['2025-10', 34], ['2025-11', 36], ['2025-12', 52], ['2026-01', 46], ['2026-02', 52]]

**Status:** PASS

---

## Q11: Which city has the most patients?

**SQL:**
```sql
SELECT city
FROM patients
GROUP BY city
ORDER BY COUNT(*) DESC
LIMIT 1
```

**Execution Time:** 0.01s

**Result Sample:**
[['Bangalore']]

**Status:** PASS

---

## Q12: List patients who visited more than 3 times

**SQL:**
```sql
SELECT p.*
FROM patients p
JOIN appointments a ON p.id = a.patient_id
GROUP BY p.id
HAVING COUNT(a.id) > 3
```

**Execution Time:** 0.01s

**Result Sample:**
[[13, 'Name12', 'Surname12', 'user12@mail.com', '9999999999', '1978-02-22 17:18:20.164822', 'F', 'Pune', '2025-11-20 17:18:20.164822'], [14, 'Name13', 'Surname13', 'user13@mail.com', '9999999999', '1975-11-12 17:18:20.164822', 'M', 'Chennai', '2026-03-29 17:18:20.164822'], [16, 'Name15', 'Surname15', 'user15@mail.com', '9999999999', '1999-03-20 17:18:20.164822', 'M', 'Delhi', '2025-11-13 17:18:20.164822'], [17, 'Name16', 'Surname16', 'user16@mail.com', '9999999999', '1972-03-09 17:18:20.164822', 'F', 'Chennai', '2026-02-07 17:18:20.164822'], [19, 'Name18', 'Surname18', 'user18@mail.com', None, '1992-04-21 17:18:20.164822', 'M', 'Delhi', '2026-01-24 17:18:20.164822']]

**Status:** PASS

---

## Q13: Show unpaid invoices

**SQL:**
```sql
SELECT id, patient_id, invoice_date, total_amount, paid_amount, status
FROM invoices
WHERE status = 'unpaid'
```

**Execution Time:** 0.0s

**Result Sample:**
[]

**Status:** PASS

---

## Q14: What percentage of appointments are no-shows?

**SQL:**
```sql
SELECT CAST(SUM(CASE WHEN status = 'no-show' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) AS percentage
FROM appointments
```

**Execution Time:** 0.01s

**Result Sample:**
[[0.0]]

**Status:** PASS

---

## Q15: Show the busiest day of the week for appointments

**SQL:**
```sql
SELECT strftime('%w', appointment_date) AS day_of_week, 
       COUNT(*) AS count
FROM appointments
GROUP BY strftime('%w', appointment_date)
ORDER BY count DESC
LIMIT 1
```

**Execution Time:** 0.61s

**Result Sample:**
[['6', 90]]

**Status:** PASS

---

## Q16: Revenue trend by month

**SQL:**
```sql
SELECT 
  strftime('%Y-%m', DATE(invoice_date)) AS month,
  SUM(total_amount) AS revenue,
  COUNT(*) AS count_invoices
FROM invoices
GROUP BY month
ORDER BY month
```

**Execution Time:** 0.01s

**Result Sample:**
[['2025-04', 64313.0, 22], ['2025-05', 63270.0, 20], ['2025-06', 51224.0, 24], ['2025-07', 76271.0, 29], ['2025-08', 61578.0, 28]]

**Status:** PASS

---

## Q17: Average appointment duration by doctor

**SQL:**
```sql
SELECT 
  D.name, 
  AVG(T.duration_minutes) AS average_duration
FROM 
  treatments T
  JOIN appointments A ON T.appointment_id = A.id
  JOIN doctors D ON A.doctor_id = D.id
GROUP BY 
  D.name
```

**Execution Time:** 0.01s

**Result Sample:**
[['Doctor 0', 65.86363636363636], ['Doctor 1', 65.51851851851852], ['Doctor 10', 66.05405405405405], ['Doctor 11', 64.75], ['Doctor 12', 52.074074074074076]]

**Status:** PASS

---

## Q18: List patients with overdue invoices

**SQL:**
```sql
SELECT p.id, p.first_name, p.last_name, i.total_amount
FROM patients p
JOIN invoices i ON p.id = i.patient_id
WHERE i.invoice_date AND i.paid_amount = 0
```

**Execution Time:** 0.01s

**Result Sample:**
[]

**Status:** PASS

---

## Q19: Compare revenue between departments

**SQL:**
```sql
SELECT 
  D.department,
  COUNT(DISTINCT I.id) AS invoice_count,
  SUM(CASE WHEN I.status = 'paid' THEN I.total_amount - I.paid_amount ELSE 0 END) AS pending_revenue,
  SUM(CASE WHEN I.status = 'paid' THEN I.total_amount - I.paid_amount ELSE I.total_amount END) AS total_revenue
FROM patients P
JOIN appointments A ON P.id = A.patient_id
JOIN doctors D ON A.doctor_id = D.id
JOIN invoices I ON A.patient_id = I.patient_id
GROUP BY D.department
```

**Execution Time:** 0.01s

**Result Sample:**
[['Dept', 278, 0, 1974731.0]]

**Status:** PASS

---

## Q20: Show patient registration trend by month

**SQL:**
```sql
SELECT 
  strftime('%Y-%m', t1.registered_date) as registration_month,
  COUNT(*) as count
FROM patients t1
GROUP BY registration_month
ORDER BY registration_month ASC
```

**Execution Time:** 0.01s

**Result Sample:**
[['2025-04', 12], ['2025-05', 15], ['2025-06', 10], ['2025-07', 23], ['2025-08', 10]]

**Status:** PASS

---

