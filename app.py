import streamlit as st
from main import simulate_project_pipeline, project_lead_query

st.set_page_config(page_title="Agentic Project Team Simulator", layout="wide")

st.title("🏗 Agentic Project Team Simulator")

st.markdown("Simulate a full-stack project team from *requirement gathering* to *testing* using intelligent agents.")

# === 1. Business Requirement Input ===
st.subheader("📋 Business Requirement Input")
business_req = st.text_area("Enter high-level business requirement:", height=200)

if st.button("🚀 Run Simulation"):
    if business_req.strip():
        with st.spinner("Running simulation with BA, Dev, and Tester agents..."):
            output = simulate_project_pipeline(business_req)
            st.success("Simulation Complete!")

            st.subheader("📌 Artifacts")
            st.markdown("### 📘 User Stories (BA)")
            st.code(output["user_stories"], language='markdown')

            st.markdown("### 💻 Code (Developer)")
            st.code(output["code"], language='python')

            st.markdown("### ✅ Test Cases (Tester)")
            st.code(output["test_cases"], language='markdown')
    else:
        st.warning("Please enter a business requirement first.")

# === 2. Project Manager Chatbot Interface ===
st.divider()
st.subheader("🤖 Project Lead Chatbot")
st.write("Ask questions about the status or quality of the generated artifacts.")

query = st.text_input("🗣 Your question:")

if st.button("💬 Ask"):
    if query.strip():
        response = project_lead_query(query)
        st.markdown(f"*Response:* {response}")
    else:
        st.warning("Please enter a question.")
