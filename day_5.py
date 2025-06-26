import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
# altair: data visualization tool


# 헤더 작성
st.header('st.write')

# Mardown 형식 작성
# **: italic
# :: : emoji
st.write('Hello, *World!* :sunglasses:')

# 숫자와 같은 데이터 형식
st.write(1234)

# data frame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# 여러 인수 전달
st.write('아래는 DataFrame입니다', df, '위는 dataframe 입니다.')

# (변수 전달) 그래프 표시

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x="a", y="b", size="c", color='c', tooltip=['a', 'b', 'c'])
st.write(c)