import streamlit as st

st.title("Input Your Information")
#text input
name = st.text_input(":red[Enter Your Name]")
# st.write(":orange[Your name is:] ",name)
st.divider()

#number input
age = st.number_input("Enter Your age: ",value= None,placeholder="type your age") 
# st.write("Your age is: ",age)

pressed = st.button("Enter to confirm",type="primary")
if pressed:
    st.write(f"Your name is {name} and your age is {age}")
#password
# password = st.text_input("Enter Your Password:",type="password")