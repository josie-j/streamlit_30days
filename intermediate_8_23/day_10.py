import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    "What's your favourite colour?",
    ('Blue', 'Red', 'Yellow'))

st.write('Your favourite colour is ', option)