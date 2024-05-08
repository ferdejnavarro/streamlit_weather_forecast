import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast')
place = st.text_input('Location:')
days = st.slider('Forecast days', min_value=1, max_value=5,
                 help="""Select the number of days to forecast,
                      between 1 and 5.""")
option = st.selectbox('Select the type of info to analyze',
                      ('Temperature', 'Weather forecast'))
st.subheader(f"{option} for the next {days} days in {place}")


if place:
    # Get temperature or weather data
    filtered_data = get_data(place, days)

    if option == 'Temperature':
        temperatures = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        # Create temperature plot
        figure = px.line(x=dates, y=temperatures,
                     labels={'x': 'Date', 'y': 'Temperature (°C)'})
        st.plotly_chart(figure)

    if option == 'Weather forecast':
        images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                  'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
        weather = [dict['weather'][0]['main'] for dict in filtered_data]
        image_paths = [images[condition] for condition in weather]
        st.image(image_paths, width=115)
