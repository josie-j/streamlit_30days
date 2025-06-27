import streamlit as st
import requests

st.title('🏀 Bored API App')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', 'education', 'recreational', 'social', 'DIY', 'charity', 'cooking', 'relaxation', 'music', 'busywork'])

# 선택한 활동, f-string 연결 -> json 데이터 검색
suggested_activity_url = f"http://www.boredapi.com/api/activity?type={selected_type}"
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

# 앱 정보, json 데이터 표시
c1, c2 = st.columns(2)
with c1:
    with st.expander('About this app'):
        st.write('Are you bored? **Bored API App** suggests activites you can do when you are bored. This app runs by Bored API.')
with c2:
    with st.expander('JSON data'):
        st.write(suggested_activity)

# 제안된 활동 표시
st.header('Suggested Activity')
st.info(suggested_activity['activity'])

# 제안된 활동의 정보(참가자 수, 활동 유형, 가격 등) 표시
col1, col2, col3 = st.columns

(3)
with col1:
    st.metric(labe='Participants', value=suggested_activity['participants'], delta="")
with col2:
    st.metric(label="Type of Activity", value=suggested_activity['type'].capitalize(), delta='')
with col3:
    st.metric(label='Price', value=suggested_activity['price'], delta='')
# delta= '' ~ indicator of metrics changed
