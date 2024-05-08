import streamlit as st
import plotly.express as px

st.title('Weather Forecast')
place = st.text_input('Location:')
days = st.slider('Forecast days', min_value=1, max_value=5,
                 help="""Select the number of days to forecast,
                      between 1 and 5.""")
option = st.selectbox('Select the type of info to analyze',
                      ('Temperature', 'Weather forecast'))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ['2022-25-10', '2022-26-10', '2022-27-10']
    temperatures = [25, 32, 28]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t,
                 labels={'x': 'Date', 'y': 'Temperature (°C)'})

st.plotly_chart(figure)