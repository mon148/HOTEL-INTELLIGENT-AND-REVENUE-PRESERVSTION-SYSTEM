import joblib
import sys
import pandas as pd
import os
import streamlit as st
import plotly.graph_objects as go
import extra_streamlit_components as stx


print(sys.executable)

# Getting the path and loading the saved pkl
base_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_path, 'rf_model.pkl')
scaler_path = os.path.join(base_path, 'scaler.pkl')
@st.cache_resource
def load_model():
   return joblib.load (model_path), joblib.load (scaler_path)
model, scaler = load_model()


# Initialize the "Memory" (Cookie Manager)
cookie_manager = stx.CookieManager()

def manage_access():
    # Checking if the user has a verification cookie in their browser
    auth_cookie = cookie_manager.get(cookie="hotel_access_token")

    if auth_cookie == "verified_user_2026":
        return True

    #If no cookie, show the login screen
    st.title("🔐 Secure Intelligence Portal")
    password = st.text_input("Enter Access Code", type="password")
    remember = st.checkbox("Keep me logged in for 7 days")

    if st.button("Authenticate"):
        if password == "NigeriaAI2026":
            max_age = 604800 if remember else None
            cookie_manager.set("hotel_access_token", "verified_user_2026", max_age=max_age)
            st.rerun()
        else:
            st.error("Access Denied.")
    return False

# Execution
if not manage_access():
    st.stop()


# The page interface
st.set_page_config(page_title="Hotel intelligence dashboard", layout="wide")
st.title("Hotel Booking Analyzer")
st.markdown("Enter the booking details to know if cancellation would take place")

with st.sidebar:
    st.header("Booking Details")
    adr = st.number_input("Average Daily Rate (ADR)", min_value=0, value=100, step=1)
    lead_time = st.slider("Lead_time (Days)", 0, 365, 30)
    total_night = st.number_input("Total Night (Days)", min_value=0, value=80, step=1)
    special_request = st.selectbox("Special Request", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    car_park = st.selectbox("Total Car Park", [0, 1, 2, 3, 4, 5])
    adults = st.number_input("Number of Adults", 0, 30, 2)
    children = st.number_input("Number of Children", 0, 45, 0)


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

# Cloud storage
def save_to_database(input_data, prediction, probability, supabase=None):
    supabase.table("predictions").insert({
        "adr": input_data['adr'][0],
        "lead_time": input_data['lead_time'][0],
        "risk_score": probability,
        "verdict": prediction
    }).execute()

# Creating a Gauge Chart That shows The Model's Prediction
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
else:
    print("The ADR is unknown")