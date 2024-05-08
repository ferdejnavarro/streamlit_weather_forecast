# STREAMLIT Weather Forecast

## About
This app allows you to access the weather forecast for any given city's by 
typing its name and selecting the information you want to see, including
temperature, weather forecast (clear, cloudy, raining, or snowing), and its 
pressure.

# How to use
To run this application, you need to run streamlit by typing "streamlit run 
main.py" in your terminal. However, the app accesses weather data through an 
API, so in order to use it you must sign up and create an API key on this 
website: https://openweathermap.org/api

After you've created your API key, you must type it as a string for the
'API_KEY' variable in backend.py so that the app can access the weather data.
