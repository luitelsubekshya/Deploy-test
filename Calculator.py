import streamlit as st


st.title("Sample Calculator")

st.header("Calculate Simple Interest")
#st.code("print('Hellow World')")
st.write("We can calculate interest in loan amount")

col_1, col_2, col_3, col_4 = st.columns(4)
user_name = col_1.text_input("enter your name")
st.write (f"Enter you name{user_name}")
principle = col_2.number_input("Enter Principle Amount", step = 1000, min_value = 1000)
st.write(principle)

rate = col_3.number_input("Enter Rate Amount")
st.write(rate)

time = col_4.number_input("Enter Time [in Years]", step = 1)
st.write(time)
agreed = st.checkbox("I agree to terms and conditions")
if agreed:
     clicked = st.button("Calculate interest")
     if clicked:
       interest = (principle * time * rate) / 100
       st.write(f'{user_name} has to pay {interest} as interest')

date = st.date_input("Choose your DOB", min_value="1990-01-01")

feed_back = st.text_area("Provide your feedback")

st.feedback("stars")


























