import streamlit as st
import requests
import pandas as pd
import base64

st.set_page_config(page_title="AI Data App", layout="wide")

# ✅ ALWAYS VISIBLE
st.title("📊 NL → SQL → Visualization")

# input always visible
query = st.text_input("Enter your question:")

# button logic
if st.button("Run"):
    if not query:
        st.warning("Please enter a query")
    else:
        try:
            st.write("Running...")

            # STEP 1
            chat = requests.post("http://127.0.0.1:8000/chat",
                                 json={"question": query}).json()

            st.write("SQL:", chat)

            # STEP 2
            result = requests.post("http://127.0.0.1:8000/result",
                                   json={
                                       "question": query,
                                       "sql": chat["sql"]
                                   }).json()

            df = pd.DataFrame(result["data"])
            st.dataframe(df)

            # STEP 3
            response = requests.post("http://127.0.0.1:8000/visualize",
                                     json={
                                         "question": query,
                                         "data": result["data"]
                                     })

            viz = response.json()

            st.write("DEBUG:", viz)

            if isinstance(viz, dict) and "chart" in viz:
                img = base64.b64decode(viz["chart"])
                st.image(img)
            else:
                st.error("Invalid response")
                st.write(viz)

        except Exception as e:
            st.error(str(e))