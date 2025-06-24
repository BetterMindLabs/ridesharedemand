import streamlit as st
import google.generativeai as genai

# === Gemini Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === UI Setup ===
st.set_page_config(page_title="🚗 Ride-Share Demand Forecaster")
st.title("🚗 Ride-Share Demand Forecaster")
st.write("Adjust the sliders below to estimate ride demand in a given region and context.")

# === Inputs ===
city = st.selectbox("📍 City", ["New York", "Los Angeles", "Chicago", "San Francisco", "Miami"])
day_of_week = st.selectbox("📆 Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
hour = st.slider("🕒 Hour of Day", 0, 23, 18)
weather = st.selectbox("🌦️ Weather", ["Clear", "Rainy", "Snowy", "Cloudy", "Hot", "Cold"])
event = st.selectbox("🎉 Major Event Nearby?", ["None", "Concert", "Sports Game", "Festival", "Conference"])

# === Predict Button ===
if st.button("Forecast Demand"):
    with st.spinner("Forecasting..."):
        prompt = f"""
You are a transportation analytics model that predicts ride-share demand.

Based on the input, estimate:
- Demand Level: Low / Moderate / High / Very High
- Reason: 1-line brief explanation
- Confidence: Percentage between 60–95%

Input:
City: {city}  
Day: {day_of_week}  
Hour: {hour}  
Weather: {weather}  
Event: {event}

Respond in this format:
Demand Level: <...>  
Reason: <...>  
Confidence: <...>%
"""

        response = model.generate_content(prompt)
        result = response.text.strip()

        st.subheader("📈 Predicted Ride Demand")
        st.text(result)
