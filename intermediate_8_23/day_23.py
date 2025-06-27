import streamlit as st

st.title('st.query_params')

with st.expander('About this app'):
    st.write("`st.query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1 . 지침
st.header('1. Instructions')
st.markdown('''
인터넷 브라우저의 URL 바에서 다음을 추가하세요:
`?firstname=Jack&surname=Beanstalk`
기본 URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/` 뒤에 추가하여
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`가 되도록 합니다.
''')

# 2. st.experimental_get_query_params의 내용
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.query_params)

# 3. URL에서 정보 검색 및 표시
st.header('3. Retrieving and displaying information from the URL')

firstname = st.query_params['firstname'][0]
surname = st.query_params['surname'][0]

st.write(f"Hello **{firstname} {surname}**, how are you?")
