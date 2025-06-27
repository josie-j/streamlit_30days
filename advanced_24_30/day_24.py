import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

## st.cache -> st.cache_data or st.cache_resource
@st.cache_data()
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns = ['a', 'b', 'c', 'd', 'e']
    )
    return df

def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns = ['a', 'b', 'c', 'd', 'e']
    )
    return df

# 캐시 사용
a0 = time()
st.subheader('st.cache 사용')

# load_data_a 함수 삽입
st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# 캐시 미사용
b0 = time()
st.subheader('캐시 미사용')

# load_data_b 함수 삽입
st.write(load_data_b())
b1 = time()
st.info(b1-b0)