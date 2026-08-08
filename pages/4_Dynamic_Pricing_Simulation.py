import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Dynamic Pricing Simulation",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Dynamic Pricing Simulation")

st.markdown("""
Interactively simulate hotel room pricing using the
same variables used in the Reinforcement Learning project.
""")

st.divider()
st.header("Simulation Inputs")

col1, col2 = st.columns(2)

with col1:

    hotel = st.selectbox(
        "Hotel Type",
        ["Luxury", "Business", "Resort", "Budget"]
    )

    season = st.selectbox(
        "Season",
        ["Low", "Medium", "High", "Peak"]
    )

    demand = st.selectbox(
        "Demand Level",
        ["Low", "Medium", "High"]
    )

with col2:

    rooms = st.slider(
        "Rooms Available",
        0,
        300,
        100
    )

    base_price = st.slider(
        "Base Price",
        50,
        500,
        150
    )

    booking_probability = st.slider(
        "Booking Probability",
        0.0,
        1.0,
        0.50
    )
season_factor = {
    "Low":0.85,
    "Medium":1.0,
    "High":1.20,
    "Peak":1.40
}

demand_factor = {
    "Low":0.90,
    "Medium":1.0,
    "High":1.25
}

dynamic_price = (
    base_price
    * season_factor[season]
    * demand_factor[demand]
)

expected_revenue = (
    dynamic_price
    * booking_probability
)

st.divider()

st.header("Simulation Results")

c1,c2,c3 = st.columns(3)

c1.metric(
    "Dynamic Price",
    f"${dynamic_price:.2f}"
)

c2.metric(
    "Expected Revenue",
    f"${expected_revenue:.2f}"
)

c3.metric(
    "Booking Probability",
    f"{booking_probability*100:.1f}%"
)

st.divider()

if demand=="High":

    st.success(
        "Recommendation: Increase prices to maximize revenue."
    )

elif demand=="Medium":

    st.info(
        "Recommendation: Maintain current pricing."
    )

else:

    st.warning(
        "Recommendation: Reduce prices to attract more bookings."
    )
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=expected_revenue,
    title={'text':"Expected Revenue"},
    gauge={
        'axis':{'range':[0,600]},
        'bar':{'color':'green'}
    }
))

st.plotly_chart(fig, use_container_width=True)
