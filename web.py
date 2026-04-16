import joblib
import sys
import pandas as pd
import os
import streamlit as st
import plotly.graph_objects as go

print(sys.executable)

Getting the path and loading the saved pkl
base_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'rf_model.pkl')
scaler_path = os.path.join(base_path, 'scaler.pkl')
@st.cache_resource
def load_model():
   return joblib.load (model_path), joblib.load (scaler_path)
model, scaler = load_model()


# The page interface
st.set_page_config(page_title="Hotel intelligence dashboard", layout="wide")
st.title("Hotel Booking Analyzer")
st.markdown("Enter the booking details to know if cancellation would take place")

with st.sidebar:
    st.header("Booking Details")
    adr = st.number_input("Average Daily Rate (ADR)", min_value=0, value=100, step=1)
    lead_time = st.slider("Lead_time (Days)", 0, 365, 30)
    total_night = st.number_input("Total Night (Days)", min_value=0, value=3, step=1)
    special_request = st.selectbox("Special Request", [0, 1, 2, 3, 4, 5])
    car_park = st.selectbox("Total Car Park", [0, 1])
    adults = st.number_input("Number of Adults", 0, 4, 2)
    children = st.number_input("Number of Children", 0, 10, 0)


input_data = {
    "lead_time": [lead_time],
    "stays_in_weekend_nights": [total_night],
    "stays_in_week_nights": [0],
    "adults": [adults],
    "children": [children],
    "is_repeated_guest": [0],
    "previous_cancellations": [0],
    "previous_bookings_not_canceled": [0],
    "booking_changes": [0],
    "company": [0],
    "adr": [adr],
    "required_car_parking_spaces": [car_park],
    "total_of_special_requests": [special_request]
}

input_df = pd.DataFrame(input_data)

scaler = scaler.transform(input_df)
pred = model.predict(scaler)[0]
prob = model.predict_proba(scaler)[0][1]

col1, col2 = st.columns(2)

with col1:
    st.header("AI Suggestion")
    if pred == 1:
        st.error("High Risk: This booking is likely to cancel")
    elif pred == 0:
        st.success("No risk: This booking will be true😊")
    else:
        print("The value are not properly aligned")

with col2:
    st.header("Score")
    st.metric(label="Probability of cancellation", value=f"{prob*100:.2f}%")

# Create a Gauge Chart
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = prob * 100,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Cancellation Risk Score (%)"},
    gauge = {
        'axis': {'range': [None, 100]},
        'bar': {'color': "blue"},
        'steps' : [
            {'range': [0, 50], 'color': "green"},
            {'range': [50, 75], 'color': "yellow"},
            {'range': [75, 100], 'color': "red"}]}))

st.plotly_chart(fig)

st.divider()
if prob > 0.6:
    st.warning("**Recommendation:** Send confirmation email or request a deposit for this booking immediately")
elif adr > 115:
    st.info("**Insight**: The ADR is greater than the average ($117) send a discount to keep the guest's loyalty")
