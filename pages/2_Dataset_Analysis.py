import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Dataset Analysis",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Dataset Analysis")

st.markdown("""
This page allows users to explore the hotel booking datasets used in the
Reinforcement Learning Dynamic Pricing project.
""")

st.divider()

# -------------------------------------------------
# Select Dataset
# -------------------------------------------------

dataset = st.selectbox(
    "Choose Dataset",
    (
        "hotel_bookings.csv",
        "cleaned_hotel_bookings.csv",
        "synthetic_booking_data.csv"
    )
)

try:
    df = pd.read_csv(f"data/{dataset}")

except Exception as e:
    st.error(f"Unable to load dataset.\n\n{e}")
    st.stop()
# -------------------------------------------------
# Sidebar Filters
# -------------------------------------------------

st.sidebar.header("🔍 Filters")

filtered_df = df.copy()

# Hotel Type Filter
if "Hotel_Type" in df.columns:
    hotel = st.sidebar.multiselect(
        "Hotel Type",
        options=sorted(df["Hotel_Type"].dropna().unique()),
        default=sorted(df["Hotel_Type"].dropna().unique())
    )
    filtered_df = filtered_df[filtered_df["Hotel_Type"].isin(hotel)]

# Season Filter
if "Season" in df.columns:
    season = st.sidebar.multiselect(
        "Season",
        options=sorted(df["Season"].dropna().unique()),
        default=sorted(df["Season"].dropna().unique())
    )
    filtered_df = filtered_df[filtered_df["Season"].isin(season)]

# Demand Level Filter
if "Demand_Level" in df.columns:
    demand = st.sidebar.multiselect(
        "Demand Level",
        options=sorted(df["Demand_Level"].dropna().unique()),
        default=sorted(df["Demand_Level"].dropna().unique())
    )
    filtered_df = filtered_df[filtered_df["Demand_Level"].isin(demand)]
# -------------------------------------------------
# Dataset Information
# -------------------------------------------------

st.header("📊 Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", filtered_df.shape[0])
col2.metric("Columns", filtered_df.shape[1])
col3.metric("Missing Values", int(filtered_df.isnull().sum().sum()))

st.divider()

# -------------------------------------------------
# Preview
# -------------------------------------------------

st.header("Dataset Preview")

st.dataframe(filtered_df.describe(include="all"), use_container_width=True)

# -------------------------------------------------
# Summary Statistics
# -------------------------------------------------

st.header("Summary Statistics")

st.dataframe(df.describe(include="all"), use_container_width=True)

st.divider()

# -------------------------------------------------
# Missing Values
# -------------------------------------------------

st.header("Missing Values")

missing = filtered_df.isnull().sum()

st.dataframe(
    missing.reset_index().rename(
        columns={"index": "Column", 0: "Missing Values"}
    ),
    use_container_width=True
)

st.divider()

# -------------------------------------------------
# Hotel Type Distribution
# -------------------------------------------------

if "Hotel_Type" in filtered_df.columns:
    st.header("🏨 Hotel Type Distribution")

    fig = px.pie(
        filtered_df,
        names="Hotel_Type",
        title="Hotel Type Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# -------------------------------------------------
# Season Distribution
# -------------------------------------------------

if "Season" in filtered_df.columns:
    st.header("🌤 Season Distribution")

    season_counts = (
        filtered_df["Season"]
        .value_counts()
        .reset_index()
    )

    season_counts.columns = ["Season", "Bookings"]

    fig = px.bar(
        season_counts,
        x="Season",
        y="Bookings",
        title="Bookings by Season"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# -------------------------------------------------
# Demand Level Distribution
# -------------------------------------------------

if "Demand_Level" in filtered_df.columns:
    st.header("📈 Demand Level Distribution")

    demand_counts = (
        filtered_df["Demand_Level"]
        .value_counts()
        .reset_index()
    )

    demand_counts.columns = ["Demand_Level", "Bookings"]

    fig = px.bar(
        demand_counts,
        x="Demand_Level",
        y="Bookings",
        title="Demand Level Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# -------------------------------------------------
# Revenue Distribution
# -------------------------------------------------

if "Revenue" in filtered_df.columns:
    st.header("💰 Revenue Distribution")

    fig = px.histogram(
        filtered_df,
        x="Revenue",
        nbins=30,
        title="Revenue Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# -------------------------------------------------
# Dynamic Price vs Revenue
# -------------------------------------------------

if "Dynamic_Price" in filtered_df.columns and "Revenue" in filtered_df.columns:
    st.header("📊 Dynamic Price vs Revenue")

    fig = px.scatter(
        filtered_df,
        x="Dynamic_Price",
        y="Revenue",
        color="Hotel_Type" if "Hotel_Type" in filtered_df.columns else None,
        title="Dynamic Price vs Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# -------------------------------------------------
# Booking Probability Distribution
# -------------------------------------------------

if "Booking_Probability" in filtered_df.columns:
    st.header("🎯 Booking Probability Distribution")

    fig = px.histogram(
        filtered_df,
        x="Booking_Probability",
        nbins=25,
        title="Booking Probability Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# -------------------------------------------------
# Download Button
# -------------------------------------------------

st.download_button(
    label="📥 Download Filtered Dataset",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_dataset.csv",
    mime="text/csv"
)
st.divider()

# -------------------------------------------------
# Saved Analysis Graphs
# -------------------------------------------------

st.header("📊 Graphs Analysis")

st.subheader("Revenue by Hotel Type")
st.image(
    "assets/graphs/revenue_by_hoteltype.png",
    use_container_width=True
)

st.subheader("Revenue by Season")
st.image(
    "assets/graphs/revenue_by_season.png",
    use_container_width=True
)

st.subheader("Revenue vs Price")
st.image(
    "assets/graphs/Revenue_vs_Price.png",
    use_container_width=True
)

st.subheader("Demand vs Price")
st.image(
    "assets/graphs/Demand_vs_Price.png",
    use_container_width=True
)

st.subheader("Booking Probability")
st.image(
    "assets/graphs/Booking_Probability.png",
    use_container_width=True
)

st.subheader("Dynamic Price Distribution")
st.image(
    "assets/graphs/dynamic_price_distribution.png",
    use_container_width=True
)

st.subheader("Average Dynamic Price")
st.image(
    "assets/graphs/average_dynamic_price.png",
    use_container_width=True
)

st.subheader("Average Revenue by Season")
st.image(
    "assets/graphs/average_revenue_byseason.png",
    use_container_width=True
)