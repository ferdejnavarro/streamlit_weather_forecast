import streamlit as st
import plotly.express as px
from backend import get_data

st.title(f"Weather Forecast 🌞☔")
place = st.text_input('Location:')
days = st.slider('Forecast days', min_value=1, max_value=5,
                 help="""Select the number of days to forecast,
                      between 1 and 5.""")
option = st.selectbox('Select the information to analyze',
                      ('Weather forecast', 'Temperature', 'Pressure'))

if option == "Temperature":
    option_t = st.selectbox('Select units',
                      ('°C', '°F', 'K'))


st.subheader(f"{option} for the next {days} days in {place}")

error_location = """The entered city name is not valid, 
please try another one."""

if place:
    # Get temperature or weather data
    try:
        filtered_data = get_data(place, days)
        dates = [dict['dt_txt'] for dict in filtered_data]

        if option == 'Temperature':

            temperatures = [dict['main']['temp'] for dict in
                            filtered_data]

            match option_t:
                case "°C":
                    temperatures = [t - 273.15 for t in temperatures]
                case "°F":
                    temperatures = [(t - 273.15) * 1.8 + 32 for t in
                                    temperatures]
                case "K":
                    temperatures = temperatures

            # Create temperature plot
            figure = px.line(x=dates, y=temperatures,
                             labels={'x': 'Date',
                                     'y': f"Temperature ({option_t})"})
            st.plotly_chart(figure)

        if option == 'Weather forecast':
            images = {'Clear': 'images/clear.png',
                      'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            weather = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in weather]
            st.image(image_paths, width=115, caption=dates)

        if option == 'Pressure':
            pressures = [dict['main']['pressure'] for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            # Create pressure plot
            figure = px.line(x=dates, y=pressures,
                             labels={'x': 'Date', 'y': 'Pressure (Bar)'})
            st.plotly_chart(figure)

    except KeyError:
        st.info(error_location)
