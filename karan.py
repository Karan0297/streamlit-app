import streamlit as st
import numpy as np
st.title("Find the largest among the 3 given numbers")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find the largest number"):
        largest_num = np.max([num1, num2, num3])
        st.write("The largest number is:", largest_num)
