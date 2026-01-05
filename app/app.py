import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import numpy as np
import joblib

from src.optimizer import generate_recommendation

st.set_page_config(
    page_title="AI Energy Optimization System",
    layout="wide"
)

st.title("🔌 AI-Powered Energy Consumption Optimization System")
st.markdown(
    "Predict energy usage, evaluate efficiency, and get actionable optimization recommendations."
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("models/energy_model.pkl")

# -----------------------------
# Sidebar Inputs (Simulated Current State)
# -----------------------------
st.sidebar.header("Current Energy Snapshot")

hour = st.sidebar.slider("Hour of Day", 0, 23, 19)

global_active_power = st.sidebar.number_input(
    "Global Active Power (kW)", 0.0, 10.0, 3.5
)

global_reactive_power = st.sidebar.number_input(
    "Global Reactive Power (kVAR)", 0.0, 5.0, 1.2
)

voltage = st.sidebar.number_input(
    "Voltage", 210.0, 260.0, 235.0
)

global_intensity = st.sidebar.number_input(
    "Global Intensity", 0.0, 50.0, 15.0
)

sub_metering_1 = st.sidebar.number_input(
    "Kitchen Load", 0.0, 5.0, 1.0
)

sub_metering_2 = st.sidebar.number_input(
    "Laundry Load", 0.0, 5.0, 1.8
)

sub_metering_3 = st.sidebar.number_input(
    "HVAC / Heater Load", 0.0, 5.0, 2.3
)

# -----------------------------
# Feature Construction
# -----------------------------
reactive_ratio = global_reactive_power / (global_active_power + 1e-6)

efficiency_score = max(
    0,
    min(
        100,
        100 - (
            (global_active_power * 10) +
            (global_reactive_power * 15)
        )
    )
)

input_features = np.array([[
    global_active_power,
    global_reactive_power,
    voltage,
    global_intensity,
    sub_metering_1,
    sub_metering_2,
    sub_metering_3,
    hour,
    0,     # dayofweek placeholder
    global_active_power,  # lag_1 placeholder
    global_active_power,  # lag_24 placeholder
    global_active_power,  # rolling_mean_6 placeholder
    global_active_power,  # rolling_mean_24 placeholder
    reactive_ratio,
    efficiency_score
]])

# -----------------------------
# Prediction + Optimization
# -----------------------------
if st.button("Run Energy Optimization"):
    predicted_consumption = model.predict(input_features)[0]

    optimization_result = generate_recommendation(
        predicted_consumption=predicted_consumption,
        efficiency_score=efficiency_score,
        reactive_ratio=reactive_ratio,
        hour=hour,
        sub_metering_2=sub_metering_2,
        sub_metering_3=sub_metering_3
    )

    # -----------------------------
    # Display Results
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🔮 Predicted Consumption (Next Hour)",
            f"{predicted_consumption:.2f} kW"
        )

    with col2:
        st.metric(
            "⚙️ Efficiency Score",
            f"{efficiency_score:.0f} / 100"
        )

    with col3:
        st.metric(
            "💰 Estimated Savings",
            f"{optimization_result['estimated_savings_percent']} %"
        )

    st.subheader("📌 Optimization Recommendations")

    for rec in optimization_result["recommendations"]:
        st.success(rec)
