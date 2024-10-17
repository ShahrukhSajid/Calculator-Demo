import streamlit as st

# Title of the app
st.title("BNU Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown for selecting operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Button to perform calculation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."

    # Display the result
    st.write(f"The result is: {result}")

# Optional: Add some additional info or features
st.sidebar.header("About")
st.sidebar.text("This is a simple calculator app built with Streamlit.")
