import requests
import time
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000/chat"

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

OUTPUT_FILE = "RESULTS_RAW.md"
DELAY = 1.5   # ⏳ buffer time (increase if rate limit hits)

print("\n🚀 Starting NL2SQL Automated Testing...\n")

start_time = time.time()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# NL2SQL Test Results\n\n")

    for i, q in enumerate(questions, 1):
        print(f"\n🟡 [{i}/{len(questions)}] Processing...")
        print(f"➡️ Question: {q}")

        try:
            req_start = time.time()

            response = requests.post(BASE_URL, json={"question": q})
            data = response.json()

            req_time = round(time.time() - req_start, 2)

            sql = data.get("sql", "N/A")
            rows = data.get("rows", [])
            error = data.get("error")

            # Console logs
            if error:
                print(f"❌ ERROR: {error}")
            else:
                print(f"✅ SUCCESS ({req_time}s)")
                print(f"SQL: {sql[:80]}...")

            # Write to file
            f.write(f"## Q{i}: {q}\n\n")
            f.write(f"**SQL:**\n```sql\n{sql}\n```\n\n")

            if error:
                f.write(f"**Error:** {error}\n\n")
            else:
                f.write(f"**Execution Time:** {req_time}s\n\n")
                f.write(f"**Result Sample:**\n{rows[:5]}\n\n")

            f.write("---\n\n")

        except Exception as e:
            print(f"❌ FAILED: {str(e)}")

            f.write(f"## Q{i}: {q}\n\n")
            f.write(f"**Error:** {str(e)}\n\n---\n\n")

        # ⏳ Delay to avoid rate limit
        time.sleep(DELAY)

end_time = time.time()

total_time = round(end_time - start_time, 2)

print("\n🎉 Testing Completed!")
print(f"⏱️ Total Time: {total_time}s")
print(f"📄 Results saved in: {OUTPUT_FILE}")