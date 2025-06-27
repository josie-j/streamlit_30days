import streamlit as st

st.title('st.session_state')

# 체중 변환 함수 (lbs<->kg)
def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046

# 체중값 입력 받기
st.header('Input')

# 숫자 입력 가능, + - 로도 조정가능한 형태 
col1, spacer, col2 = st.columns([2, 1, 2])
with col1:
    pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
    kilogram = st.number_input("Kilogram:", key = "kg", on_change = kg_to_lbs)
# ~ key 값, st.session_state."key"로 설정함\
# on_change: 함수

# 세션 상태 저장 값 ~ st.session_state.kg 과 st.session.lbs로 st.write를 통해 출력
st.header('Print')
st.write('st.session_state Object:', st.session_state)
# {
#     "kg": ~~
#     "lbs": ~~
# } 의 형태로 출력됨
