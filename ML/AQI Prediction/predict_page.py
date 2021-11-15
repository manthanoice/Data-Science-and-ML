import streamlit as st
import pickle
import numpy as np
import pandas

def load_model():
    with open('ahmedabad.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data['model']

def show_predict_page():
    st.title("AQI Prediction")

    cities = (
        "Ahmedabad",
        "Banglore",
        "Delhi"
    )

    city = st.selectbox("City", cities)

    temprature = st.slider("Temprature", 0.0, 100.0, 0.0)
    maximum_temp = st.slider("Maximum Temprature", 0.0, 60.0, 0.0)
    minimum_temp = st.slider("Minimum Temprature", 0.0, 40.0, 0.0)
    avg_humi = st.slider("Averrage relative humidity", 0, 120, 0)
    tot_rainfall = st.slider("Total Rainfall", 0.0, 200.0, 0.0)
    avg_visib = st.slider("Average Visibility", 0.0, 10.0, 0.0)
    avg_wind_speed = st.slider("Average Wind Speed", 0.0, 30.0, 0.0)
    avg_temp = st.slider("Average Temprature", 0.0, 60.0, 0.0)

    ok = st.button("Calculate AQI")
    if ok:
        x = np.array([[temprature, maximum_temp, minimum_temp, avg_humi, tot_rainfall, avg_visib, avg_wind_speed, avg_temp]])
        answer = regressor.predict(x)
        st.subheader(f"AQI would be {answer[0]:.2f}")