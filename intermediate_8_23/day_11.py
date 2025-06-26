import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    "What's your favourite colour?",
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('Colours you choose: ', options)