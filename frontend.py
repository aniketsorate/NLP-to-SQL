import streamlit as st
import requests
import pandas as pd
import base64

st.set_page_config(page_title="AI Data App", layout="wide")

# --- Header ---
st.title("📊 AI Data Assistant")
st.markdown("Ask questions in natural language → get SQL → results → visualization")

# --- Input ---
query = st.text_input("🔍 Enter your question")

# --- Run Button ---
if st.button("🚀 Run Query"):
    if not query:
        st.warning("Please enter a query")
    else:
        try:
            with st.spinner("Generating SQL..."):
                chat = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={"question": query}
                ).json()

            # --- Layout: 2 columns ---
            col1, col2 = st.columns(2)

            # ================= LEFT SIDE =================
            with col1:
                st.subheader("🧠 Generated SQL")
                st.code(chat, language="sql")

                # STEP 2
                with st.spinner("Fetching data..."):
                    result = requests.post(
                        "http://127.0.0.1:8000/result",
                        json={
                            "question": query,
                            "sql": chat
                        }
                    ).json()

                df = pd.DataFrame(result["data"])

                st.subheader("📋 Result Table")
                st.dataframe(df, use_container_width=True)

                st.metric("Rows", len(df))

            # ================= RIGHT SIDE =================
            with col2:
                st.subheader("📈 Visualization")

                with st.spinner("Generating chart..."):
                    response = requests.post(
                        "http://127.0.0.1:8000/visualize",
                        json={
                            "question": query,
                            "data": result["data"]
                        }
                    )

                viz = response.json()

                if isinstance(viz, dict) and "chart" in viz:
                    img = base64.b64decode(viz["chart"])
                    st.image(img)
                else:
                    st.error("Visualization failed")
                    st.write(viz)

        except Exception as e:
            st.error(f"Error: {str(e)}")