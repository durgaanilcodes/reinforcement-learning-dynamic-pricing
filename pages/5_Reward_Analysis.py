import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Reward Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Reward Analysis & Graphs")

st.markdown("""
This page evaluates the Reinforcement Learning Dynamic Pricing strategy
using interactive charts and performance metrics.
""")

st.divider()
df = pd.read_csv("data/synthetic_booking_data.csv")

st.header("📊 Performance Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Revenue",
    f"${df['Revenue'].mean():.2f}"
)

col2.metric(
    "Average Dynamic Price",
    f"${df['Dynamic_Price'].mean():.2f}"
)

col3.metric(
    "Average Booking Probability",
    f"{df['Booking_Probability'].mean()*100:.1f}%"
)

st.divider()

st.header("🏨 Revenue by Hotel Type")

hotel_revenue = (
    df.groupby("Hotel_Type")["Revenue"]
    .mean()
    .reset_index()
)

fig = px.bar(
    hotel_revenue,
    x="Hotel_Type",
    y="Revenue",
    color="Hotel_Type",
    title="Average Revenue by Hotel Type"
)

st.plotly_chart(fig, use_container_width=True)

st.header("🌤 Revenue by Season")

season_revenue = (
    df.groupby("Season")["Revenue"]
    .mean()
    .reset_index()
)

fig = px.line(
    season_revenue,
    x="Season",
    y="Revenue",
    markers=True,
    title="Average Revenue by Season"
)

st.plotly_chart(fig, use_container_width=True)

st.header("🎯 Booking Probability vs Revenue")

fig = px.scatter(
    df,
    x="Booking_Probability",
    y="Revenue",
    color="Demand_Level",
    size="Dynamic_Price",
    hover_data=["Hotel_Type"],
    title="Booking Probability vs Revenue"
)

st.plotly_chart(fig, use_container_width=True)

st.header("💰 Dynamic Price Distribution")

fig = px.histogram(
    df,
    x="Dynamic_Price",
    nbins=30,
    title="Distribution of Dynamic Prices"
)

st.plotly_chart(fig, use_container_width=True)

st.header("📈 Revenue vs Dynamic Price")

fig = px.scatter(
    df,
    x="Dynamic_Price",
    y="Revenue",
    color="Season",
    title="Revenue vs Dynamic Price"
)

st.plotly_chart(fig, use_container_width=True)

st.header("🏆 RL Performance Summary")

st.success("""
The Reinforcement Learning approach dynamically adjusts hotel room prices
based on demand, season, and booking probability.

Key observations:

• Higher demand generally leads to higher prices.

• Revenue increases during peak seasons.

• Dynamic pricing adapts more effectively than fixed pricing strategies.

• The pricing policy aims to maximize long-term revenue while maintaining healthy booking rates.
""")