import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.markdown("""
This dashboard was developed as part of the **Reinforcement Learning Dynamic Pricing**
project. It demonstrates how Artificial Intelligence can optimize hotel room pricing
to maximize long-term revenue.
""")

st.divider()

st.header("📌 Project Information")

st.info("""
**Project Title**

Reinforcement Learning for Dynamic Pricing in the Travel & Hospitality Industry

**Domain**

Artificial Intelligence

Machine Learning

Reinforcement Learning

Travel & Hospitality
""")

st.header("🛠 Technologies")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### Programming

- Python
- Streamlit

### Libraries

- Pandas
- NumPy
- Plotly
""")

with col2:
    st.markdown("""
### Machine Learning

- Gymnasium
- Stable-Baselines3

### Tools

- VS Code
- Git
- GitHub
""")
st.header("👥 Team Members")

st.table({
    "Member":[
        "Durga Anil",
        "Binit Binu",
        "Krutika Thakur",
        "Priyadharshini"
    ],
    "Role":[
        "RL Environment & Integration",
        "Dataset & Validation",
        "Dashboard & Visualizations",
        "Documentation"
    ]
})
st.header("✨ Dashboard Features")

st.success("""
✔ Home Page

✔ Project Overview

✔ Dataset Analysis

✔ RL Environment

✔ Dynamic Pricing Simulation

✔ Reward Analysis

✔ Documentation

✔ Interactive Charts

✔ Download Dataset

✔ Responsive Dashboard
""")

st.header("🚀 Future Scope")

st.markdown("""
The project can be extended by:

- Deploying the RL model in real hotels.
- Integrating live booking APIs.
- Using Deep Reinforcement Learning models.
- Predicting demand using weather and events.
- Real-time pricing optimization.
""")
st.divider()

st.caption("Reinforcement Learning Dynamic Pricing Dashboard | Version 1.0")