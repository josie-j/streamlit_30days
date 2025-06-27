import streamlit as st

st.set_page_config(layout="wide")

st.title('Configure Streamlit App Layout')

# 확장 가능한 상자 배치
with st.expander('About this App'):
    st.write('This App shows various way of configuring App')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

# 사용자 입력 받기 위한 입력 위젯
st.sidebar.header('Input')
user_name = st.sidebar.text_input("What's your name?")
user_emoji = st.sidebar.selectbox('Select Emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox("What's your favourite food?", ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

# 칼럼 생성
st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
    if user_name != "":
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write("👈 Please insert **Your Name**")

with col2:
    if user_emoji != "":
        st.write(f"{user_emoji} is your favourite **Emoji**!")
    else:
        st.write('👈 Please select **Emoji**!')

with col3:
    if user_food != "":
        st.write(f"🍴 {user_food} is your favourite **food**!")
    else:
        st.write("👈 Please select your favourite **food**!")