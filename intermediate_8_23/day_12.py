import streamlit as st

st.header('st.checkbox')

# taking order
st.write('What would you like to order?')

# selections
icecream = st.checkbox('ice cream')
coffee = st.checkbox('coffee')
coke = st.checkbox('coke')

# customed text of selections
if icecream:
    st.write("Great! Here's some more ice cream 🍦")

if coffee:
    st.write("Sure, here's your coffee ☕") 

if coke:
    st.write("Here you are 🥤")