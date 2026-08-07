import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="RL Dynamic Pricing Dashboard",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("🏨 Reinforcement Learning Based Dynamic Pricing Dashboard")

st.markdown("""
### Optimize Hotel Room Pricing using Reinforcement Learning

This dashboard presents a complete Reinforcement Learning based Dynamic Pricing System
developed for the Travel & Hospitality domain.

The application demonstrates how Reinforcement Learning can optimize hotel room prices
based on demand, booking probability, season, and room availability to maximize revenue.
""")

st.divider()

# ---------------------------------------------------
# Project Objectives
# ---------------------------------------------------
st.header("📌 Project Objectives")

col1, col2 = st.columns(2)

with col1:
    st.success("Maximize Hotel Revenue")
    st.success("Dynamic Price Optimization")
    st.success("Improve Booking Efficiency")

with col2:
    st.success("Interactive Dashboard")
    st.success("Visualize RL Training")
    st.success("Support Business Decision Making")

st.divider()

# ---------------------------------------------------
# Team Members
# ---------------------------------------------------
st.header("👨‍💻 Project Team")

team = {
    "Member": [
        "Durga Anil",
        "Binit Binu",
        "Krutika Thakur",
        "Priyadharshini"
    ]
}

st.table(team)

st.divider()

# ---------------------------------------------------
# Technologies
# ---------------------------------------------------
st.header("🛠 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.info("Python")
    st.info("Streamlit")
    st.info("Pandas")

with tech2:
    st.info("NumPy")
    st.info("Matplotlib")
    st.info("Plotly")

with tech3:
    st.info("Gymnasium")
    st.info("GitHub")
    st.info("VS Code")

st.divider()

st.info("👈 Use the sidebar to navigate through different dashboard pages.")