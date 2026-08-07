import streamlit as st

st.set_page_config(
    page_title="RL Environment",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Reinforcement Learning Environment")

st.markdown("""
This page explains how Reinforcement Learning (RL) is used for
Dynamic Pricing in the hotel booking system.
""")

st.divider()

st.header("📖 What is Reinforcement Learning?")

st.markdown("""
Reinforcement Learning (RL) is a Machine Learning technique in which an
Agent learns by interacting with an Environment.

Instead of following fixed rules, the agent tries different pricing
strategies and learns from rewards to maximize long-term revenue.
""")
st.header("🧠 RL Components")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🤖 Agent")

    st.info("""
The Agent is the pricing model.

It decides what hotel room price should be offered.
""")

    st.subheader("🌍 Environment")

    st.info("""
The Environment represents hotel bookings,
customer demand and room availability.
""")

with col2:

    st.subheader("📊 State")

    st.success("""
Current information available to the agent.

Example:
- Season
- Hotel Type
- Demand Level
- Rooms Available
""")

    st.subheader("🎯 Action")

    st.success("""
The pricing decision taken by the agent.

Example:
Increase price
Decrease price
Keep price unchanged
""")

st.subheader("🏆 Reward")

st.warning("""
The reward is the revenue earned after
customers decide whether to book the room.
""")
st.divider()

st.header("🔄 RL Workflow")

st.markdown("""
1. Observe the current hotel booking state.

2. Choose a pricing action.

3. Customer reacts.

4. Revenue is calculated.

5. Agent receives reward.

6. Agent updates its policy.

7. Repeat for thousands of episodes.
""")

st.divider()

st.header("🧠 RL Algorithms Used")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Q-Learning")

    st.write("""
✔ Value-based learning

✔ Off-policy algorithm

✔ Uses Q-Table
""")

with col2:

    st.subheader("SARSA")

    st.write("""
✔ On-policy learning

✔ Safer exploration

✔ Learns from current policy
""")

with col3:

    st.subheader("Deep Q Network (DQN)")

    st.write("""
✔ Uses Neural Networks

✔ Handles large state spaces

✔ Better scalability
""")
st.divider()

st.header("✅ Why Reinforcement Learning?")

st.success("""
• Learns automatically from experience

• Maximizes long-term revenue

• Adapts to changing demand

• Better than static pricing

• Can handle dynamic environments
""")