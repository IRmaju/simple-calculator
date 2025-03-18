import streamlit as st # type: ignore

def calculate(num1, num2, operation):
    if operation == "Addition (+)":
        return num1 + num2, "+"
    elif operation == "Subtraction (-)":
        return num1 - num2, "-"
    elif operation == "Multiplication (×)":
        return num1 * num2, "×"
    elif operation == "Division (÷)":
        if num2 == 0:
            return None, "÷"
        return num1 / num2, "÷"

def main():
    st.title("Simple Calculator")
    st.write("Enter two numbers and choose an operation")
    
    col1, col2 = st.columns(2)
    
    with col1:
       num1 = st.number_input("Enter first number", value=0, step=1)


    with col2:
      num2 = st.number_input("Enter second number", value=0, step=1)
        
    
    operation = st.selectbox("Choose operation", ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"])
    
    if st.button("Calculate"):
        result, symbol = calculate(num1, num2, operation)
        if result is None:
            st.error("Error: Division by zero!")
        else:
            st.success(f"{num1} {symbol} {num2} = {result}")
    
if __name__ == "__main__":
    main()
