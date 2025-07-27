import streamlit as st
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

st.title("Weather App")

city = st.text_input("Enter a city name:")

api_key = 'e4de532e5c8a87860c96eeab90fae913'

if st.button("Get Weather"):
    if city:
        weather_data = get_weather(city, api_key)
        
        if weather_data.get('cod') != 200:
            st.error("City not found!")
        else:
            st.success(f"Weather data for {city}:")
            st.write(f"Temperature: {weather_data['main']['temp']} °C")
            st.write(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
            st.write(f"Humidity: {weather_data['main']['humidity']} %")
            st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        st.error("Please enter a city name.")