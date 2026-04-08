import pandas as pd
import plotly.express as px

def generate_chart(rows, cols):
    try:
        if not rows or len(cols) < 2:
            return None

        df = pd.DataFrame(rows, columns=cols)

        if any("month" in c.lower() or "date" in c.lower() for c in cols):
            if df[cols[1]].dtype != "object":
                return px.line(df, x=cols[0], y=cols[1]).to_json()

        if df[cols[1]].dtype != "object":
            return px.bar(df, x=cols[0], y=cols[1]).to_json()

        return None
    except:
        return None