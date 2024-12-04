import streamlit as st
from addition import add
from subtraction import subtract  # Assuming this file exists
from Multiplication import multiply  # Assuming this file exists
from division import divide

# Title
st.title("Calculator _ UI")
st.write("Welcome to the Smart Calculator App! Perform basic arithmetic operations like addition, subtraction, multiplication, and division effectively.")
st.write("credit goes to Aleesha tahir")
# Input Fields
num1 = st.number_input("Enter the first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter the second number:", value=0.0, step=1.0)

# Operator Selection
operator = st.selectbox(
    "Select an operation:",
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
)

# Calculate and Display Result
if st.button("Calculate"):
    if operator == "Addition (+)":
        result = add(num1, num2)
        st.success(f"The result is: {result}")
    elif operator == "Subtraction (-)":
        result = subtract(num1, num2)
        st.success(f"The result is: {result}")
    elif operator == "Multiplication (*)":
        result = multiply(num1, num2)
        st.success(f"The result is: {result}")
    elif operator == "Division (/)":
        if num2 != 0:
            result = divide(num1, num2)
            st.success(f"The result is: {result}")
        else:
            st.error("Division by zero is not allowed!")

