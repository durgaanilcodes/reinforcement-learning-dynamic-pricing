import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="RL Dynamic Pricing Dashboard",
    page_icon="💰",
    layout="wide"
)

# -----------------------------
# Main Title
# -----------------------------
st.title("🏨 Reinforcement Learning Dynamic Pricing Dashboard")

st.markdown("""
Welcome to the **Dynamic Pricing Dashboard** developed for the
Travel & Hospitality Reinforcement Learning Project.

This dashboard combines the work of the entire team into one application.

Use the navigation menu on the left to explore different sections of the project.
""")

st.divider()

# -----------------------------
# Project Summary
# -----------------------------
st.header("📌 Project Summary")

st.write("""
The goal of this project is to optimize hotel room pricing using
Reinforcement Learning.

Instead of keeping prices fixed, the RL Agent learns the best pricing strategy
by interacting with a simulated hotel booking environment.

The objective is to maximize long-term revenue while maintaining high booking rates.
""")

st.divider()

# -----------------------------
# Dashboard Modules
# -----------------------------
st.header("📂 Dashboard Modules")

col1, col2 = st.columns(2)

with col1:
    st.success("📊 Project Overview")
    st.success("📂 Dataset Analysis")
    st.success("🤖 RL Environment")
    st.success("💰 Dynamic Pricing Simulation")

with col2:
    st.success("📈 Reward Analysis")
    st.success("📑 Documentation")
    st.success("ℹ️ About Project")

st.divider()

# -----------------------------
# Team Information
# -----------------------------
st.header("👨‍💻 Team Members")

st.table({
    "Name": [
        "Krutika Thakur",
        "Durga Anil",
        "Binit Binu",
        "Krutika Thakur",
        "Priyadharshini"
    ],
    "Role": [
        "Dashboard & Visualizations",
        "RL Environment",
        "Dataset Processing",
        "Dashboard & Visualizations",
        "RL Algorithms Research"
    ]
})

st.divider()

# -----------------------------
# Footer
# -----------------------------
st.caption("Developed using Streamlit • Reinforcement Learning Dynamic Pricing Project")