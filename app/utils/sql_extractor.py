import re

def extract_sql(text: str):
    match = re.search(r"(SELECT .*?)(;|$)", text, re.I | re.S)
    return match.group(1) if match else None