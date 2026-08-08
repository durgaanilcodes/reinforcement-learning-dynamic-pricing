import streamlit as st

# --------------------------------------------------
# Page Title
# --------------------------------------------------
st.title("📊 Project Overview")

st.markdown("""
## Reinforcement Learning Based Dynamic Pricing for Hotels

The Travel and Hospitality industry faces a major challenge in setting the optimal room price.
Traditional pricing strategies often fail to adapt to changing customer demand, seasonal trends,
and room availability.

This project uses Reinforcement Learning (RL) to learn an intelligent pricing strategy that
adjusts hotel room prices dynamically. Instead of relying on fixed pricing rules, the RL agent
learns from interactions with the environment to maximize long-term revenue while maintaining
healthy booking rates.

The Streamlit dashboard provides an interactive platform to explore the dataset, understand
the RL environment, simulate pricing decisions, and visualize the performance of the trained model.
""")

st.divider()

# --------------------------------------------------
# Business Problem
# --------------------------------------------------
st.header("🏨 Business Problem")

st.info("""
Hotels often use fixed pricing strategies that do not respond effectively to changes in demand.
During high-demand periods, rooms may be underpriced, reducing potential revenue.
During low-demand periods, rooms may remain unsold due to high prices.

Dynamic Pricing helps hotels adjust prices automatically based on demand,
booking probability, season, and room availability.
""")

st.divider()

# --------------------------------------------------
# Objectives
# --------------------------------------------------
st.header("🎯 Project Objectives")

objectives = [
    "Present the business problem and complete project pipeline.",
    "Explore and analyze the hotel booking dataset.",
    "Explain the Reinforcement Learning environment.",
    "Simulate dynamic pricing decisions interactively.",
    "Visualize reward, revenue, and pricing performance.",
    "Provide complete project documentation."
]

for obj in objectives:
    st.success(obj)

st.divider()

# --------------------------------------------------
# Workflow
# --------------------------------------------------
st.header("🔄 Project Workflow")

st.markdown("""
1. Collect hotel booking dataset.
2. Preprocess and clean the data.
3. Design the Reinforcement Learning environment.
4. Train the RL agent.
5. Generate optimized pricing decisions.
6. Evaluate model performance.
7. Visualize results through the Streamlit dashboard.
""")

st.divider()

# --------------------------------------------------
# Technologies
# --------------------------------------------------
st.header("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
**Programming**
- Python
- Streamlit
- Pandas
- NumPy
""")

with col2:
    st.markdown("""
**Visualization & Tools**
- Plotly
- Matplotlib
- GitHub
- VS Code
""")

st.divider()

# --------------------------------------------------
# Expected Outcome
# --------------------------------------------------
st.header("📈 Expected Outcome")

st.success("""
The Reinforcement Learning agent learns an effective pricing strategy that
maximizes hotel revenue while adapting to changing market demand.
The Streamlit dashboard enables users to explore the project, visualize
results, and interact with the pricing simulation in an intuitive manner.
""")