import streamlit as st

st.title('st.form')

# with 표기법 사용한 예시
st.header('1. `with` 표기법 사용 예시')
st.subheader('커피 머신')

with st.form('my_form'):
    st.subheader('**커피 주문하기**')

    # 위젯
    coffee_bean_val = st.selectbox('Coffee Bean', ['Arabica', 'Roabustar'])
    coffee_roast_val = st.selectbox('Coffee Roasting', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing Method', ['Aero-press', 'Drip', 'French Press', 'Mocha Pot', 'Cyphon'])
    serving_type_val = st.selectbox("Serving Type", ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Brought my own cup')

    # 모든 양식은 제출 버튼을 가져야함
    submitted = st.form_submit_button('Submit')

# 제출 버튼 클릭 후 로직
if submitted:
    st.markdown(f'''
                ☕ Your order:
                - Coffee Bean: `{coffee_bean_val}`
                - Coffee Roasting: `{coffee_roast_val}`
                - Brewing Method: `{brewing_val}`
                - Serving Type: `{serving_type_val}`
                - Milk: `{milk_val}`
                - Bring your own cup: `{owncup_val}`   # checked: True, un-checked: False
                ''')
else:
    st.write('☝️ Please make your order!')


# 객체 표기법
st.header('객체 표기법 예시')

form = st.form('my_form_2')
selected_val = form.slider('Select Value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)