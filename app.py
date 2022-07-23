import streamlit as st

def sub(a, b):
  return a - b

st.title('Subtraction App')

st.write("Subtraction of 2 given numbers")

a = st.number_input("Enter a number")

b = st.number_input("Enter another number")

st.write(sub(a, b))
