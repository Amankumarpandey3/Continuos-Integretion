import streamlit as st

#Steamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square,code and fifth power.")

# Get user input
n = st.number_input("Enter an Integer", value=1, Step=1)

# Calculate results
square = n**2
cube = n**3
fifth_power = n**5

#Display result
st.write("The square of [n] is : {square}" )
st.write("The cube of [n] is {cube}")
st.write("The fifth power of [n] is: {fifth_power}")