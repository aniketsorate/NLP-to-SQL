def validate_sql(sql: str):
    s = sql.lower()

    if not s.startswith("select"):
        return False, "Only SELECT queries allowed"

    for word in ["insert", "update", "delete", "drop", "alter", "exec"]:
        if word in s:
            return False, f"Forbidden keyword: {word}"

    if "sqlite_master" in s:
        return False, "System table access not allowed"

    if "extract(" in s:
        return False, "Use SQLite strftime"

    return True, "OK"