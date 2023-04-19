import streamlit as st
def largest_number():
    st.title("Find the largest among the 3 given numbers")

    # Create three input boxes for the three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Create a button to find the largest number
    if st.button("Find the largest number"):
        largest_num = np.max([num1, num2, num3])
        st.write("The largest number is:", largest_num)
