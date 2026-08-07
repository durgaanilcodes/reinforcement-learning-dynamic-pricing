import streamlit as st

st.set_page_config(
    page_title="Documentation",
    page_icon="📑",
    layout="wide"
)

st.title("📑 Project Documentation")

st.markdown("""
This page contains the project methodology, workflow, implementation details,
and team documentation for the Reinforcement Learning Dynamic Pricing project.
""")

st.divider()

st.header("📌 Project Methodology")

st.markdown("""
### Project Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis
4. Reinforcement Learning Environment Design
5. RL Agent Training
6. Dynamic Pricing Simulation
7. Performance Evaluation
8. Dashboard Development
""")

st.header("🛠 Technologies Used")

st.table({
    "Technology": [
        "Python",
        "Streamlit",
        "Pandas",
        "NumPy",
        "Plotly",
        "Gymnasium",
        "Stable-Baselines3",
        "Git & GitHub"
    ],
    "Purpose": [
        "Programming Language",
        "Dashboard Development",
        "Data Processing",
        "Numerical Computation",
        "Interactive Visualizations",
        "RL Environment",
        "RL Algorithms",
        "Version Control"
    ]
})

st.header("🔄 Workflow")

st.code("""
Hotel Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
RL Environment
      │
      ▼
RL Agent
      │
      ▼
Dynamic Pricing
      │
      ▼
Revenue Evaluation
      │
      ▼
Dashboard Visualization
""")

st.header("👥 Team Contributions")

st.markdown("""
| Team Member | Contribution |
|-------------|--------------|
| Durga Anil | RL Environment, Streamlit Integration, Model Optimization |
| Binit Binu | Dataset Preparation, Validation, Simulation Testing |
| Krutika Thakur | Visualizations, Dashboard Development, Charts, Architecture |
| Priyadharshini | Documentation, Methodology, Final Report |
""")

st.header("🎯 Project Outcome")

st.success("""
The project demonstrates how Reinforcement Learning can improve
hotel pricing strategies by dynamically adjusting prices based
on demand, season, room availability, and booking probability.

The dashboard provides an interactive interface to explore the
dataset, understand the RL environment, simulate pricing decisions,
and analyze project results.
""")