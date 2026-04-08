import requests
import time
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000/chat"
OUTPUT_FILE = "RESULTS_RAW.md"

# safe delay to avoid rate limit
DELAY = 3  

questions = [
    "How many patients do we have?",
    "List all doctors and their specializations",
    "Show me appointments for last month",
    "Which doctor has the most appointments?",
    "What is the total revenue?",
    "Show revenue by doctor",
    "How many cancelled appointments last quarter?",
    "Top 5 patients by spending",
    "Average treatment cost by specialization",
    "Show monthly appointment count for the past 6 months",
    "Which city has the most patients?",
    "List patients who visited more than 3 times",
    "Show unpaid invoices",
    "What percentage of appointments are no-shows?",
    "Show the busiest day of the week for appointments",
    "Revenue trend by month",
    "Average appointment duration by doctor",
    "List patients with overdue invoices",
    "Compare revenue between departments",
    "Show patient registration trend by month"
]

print("\nStarting test run...\n")
start_time = time.time()

passed = 0
total = len(questions)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# NL2SQL Test Results\n\n")

    for i, q in enumerate(questions, 1):
        print(f"[{i}/{total}] {q}")

        try:
            req_start = time.time()

            response = requests.post(BASE_URL, json={"question": q})
            data = response.json()

            elapsed = round(time.time() - req_start, 2)

            sql = data.get("sql")
            rows = data.get("rows")
            error = data.get("error")

            success = error is None and rows is not None

            if success:
                passed += 1
                status = "PASS"
                print(f"  -> OK ({elapsed}s)")
            else:
                status = "FAIL"
                print(f"  -> FAIL: {error}")

            # write to file
            f.write(f"## Q{i}: {q}\n\n")

            if sql:
                f.write(f"**SQL:**\n```sql\n{sql}\n```\n\n")
            else:
                f.write(f"**SQL:** N/A\n\n")

            if error:
                f.write(f"**Error:** {error}\n\n")
            else:
                sample = rows[:5] if rows else []
                f.write(f"**Execution Time:** {elapsed}s\n\n")
                f.write(f"**Result Sample:**\n{sample}\n\n")

            f.write(f"**Status:** {status}\n\n---\n\n")

        except Exception as e:
            print(f"  -> ERROR: {str(e)}")

            f.write(f"## Q{i}: {q}\n\n")
            f.write(f"**Error:** {str(e)}\n\n---\n\n")

        time.sleep(DELAY)

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("\nDone")
print(f"Passed: {passed}/{total}")
print(f"Time taken: {total_time}s")
print(f"Saved to: {OUTPUT_FILE}")