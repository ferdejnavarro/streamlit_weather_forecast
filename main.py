import streamlit as st

st.title('Weather Forecast')
place = st.text_input('Location:')
days = st.slider('Forecast days', min_value=1, max_value=5,
                 help="""Select the number of days to forecast,
                      between 1 and 5.""")
option = st.selectbox('Select the type of info to analyze',
                      ('Temperature', 'Weather forecast'))
st.subheader(f"{option} for the next {days} days in {place}")
