import streamlit as st
import pandas as pd
import numpy as np

st.header('Line Chart')

# 무작위 생성 데이터 프레임
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

# line chart
st.line_chart(chart_data)
