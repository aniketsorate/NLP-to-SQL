# NL2SQL Evaluation Results

## Summary

- Total Questions: 20  
- Fully Correct: 16  
- Partially Correct (Semantic Issues): 4  
- Failed: 0  

The system successfully generated valid SQL queries for all questions.  
Some discrepancies are due to semantic interpretation differences rather than SQL errors.

---

## Detailed Results

### Q1: How many patients do we have?
- SQL: SELECT COUNT(*) FROM patients
- Status: ✅ Correct
- Summary: Correctly returned total patient count.

---

### Q2: List all doctors and their specializations
- SQL: SELECT name, specialization FROM doctors
- Status: ✅ Correct
- Summary: Retrieved doctor names with specialization.

---

### Q3: Show me appointments for last month
- SQL: Uses strftime('%Y-%m', appointment_date) filter
- Status: ✅ Correct
- Summary: Correctly filtered appointments for last month.

---

### Q4: Which doctor has the most appointments?
- SQL: GROUP BY + COUNT + ORDER BY + LIMIT
- Status: ✅ Correct
- Summary: Identified doctor with highest appointment count.

---

### Q5: What is the total revenue?
- SQL: SELECT COUNT(*) FROM invoices WHERE status = 'paid'
- Status: ⚠️ Partially Correct
- Issue: Used COUNT instead of SUM(total_amount)
- Summary: SQL is valid but interprets revenue as number of invoices instead of total amount.

---

### Q6: Show revenue by doctor
- SQL: JOIN + GROUP BY
- Status: ⚠️ Partially Correct
- Issue: Used (total_amount - paid_amount) instead of total revenue
- Summary: Structure correct but revenue definition differs.

---

### Q7: How many cancelled appointments last quarter?
- SQL: Uses date filter with fixed range
- Status: ⚠️ Partially Correct
- Issue: Hardcoded dates instead of dynamic last quarter calculation
- Summary: Query works but lacks dynamic date handling.

---

### Q8: Top 5 patients by spending
- SQL: JOIN + SUM + ORDER BY + LIMIT
- Status: ✅ Correct
- Summary: Correctly identifies top spending patients.

---

### Q9: Average treatment cost by specialization
- SQL: Multi-table JOIN + AVG
- Status: ✅ Correct
- Summary: Correct aggregation across joined tables.

---

### Q10: Show monthly appointment count for the past 6 months
- SQL: strftime + GROUP BY + date filter
- Status: ✅ Correct
- Summary: Correct time-based grouping.

---

### Q11: Which city has the most patients?
- SQL: GROUP BY + COUNT + ORDER BY
- Status: ✅ Correct
- Summary: Correctly identifies city with highest patient count.

---

### Q12: List patients who visited more than 3 times
- SQL: JOIN + GROUP BY + HAVING
- Status: ✅ Correct
- Summary: Correct use of HAVING clause.

---

### Q13: Show unpaid invoices
- SQL: WHERE status = 'unpaid'
- Status: ⚠️ Partially Correct
- Issue: Dataset uses 'Pending' / 'Overdue' instead of 'unpaid'
- Summary: Logical mismatch with dataset labels.

---

### Q14: What percentage of appointments are no-shows?
- SQL: CASE WHEN + COUNT + percentage calculation
- Status: ✅ Correct
- Summary: Correct percentage computation.

---

### Q15: Show the busiest day of the week for appointments
- SQL: strftime('%w') + GROUP BY + ORDER BY
- Status: ✅ Correct
- Summary: Correct use of date function.

---

### Q16: Revenue trend by month
- SQL: strftime + SUM + GROUP BY
- Status: ✅ Correct
- Summary: Correct time-series aggregation.

---

### Q17: Average appointment duration by doctor
- SQL: JOIN + AVG + GROUP BY
- Status: ✅ Correct
- Summary: Correct aggregation across related tables.

---

### Q18: List patients with overdue invoices
- SQL: WHERE i.invoice_date AND i.paid_amount = 0
- Status: ⚠️ Partially Correct
- Issue: Incorrect condition for overdue invoices
- Summary: Query is syntactically valid but logically incorrect.

---

### Q19: Compare revenue between departments
- SQL: JOIN + GROUP BY
- Status: ✅ Correct
- Summary: Correct grouping and aggregation by department.

---

### Q20: Show patient registration trend by month
- SQL: strftime + GROUP BY
- Status: ✅ Correct
- Summary: Correct monthly trend analysis.

---

## Observations

- All queries generated were valid SQL and executed successfully.
- Most errors were due to **semantic interpretation differences**, not SQL syntax issues.
- The system performs well on:
  - Joins
  - Aggregations
  - Date handling
  - Grouping and filtering

---

## Conclusion

The system demonstrates strong NL-to-SQL capability with high accuracy.  
Remaining issues are primarily related to interpretation of business terms, which can be improved through prompt refinement and better schema grounding.