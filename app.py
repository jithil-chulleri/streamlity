import streamlit as st

# Define user credentials (for demo purposes)
USERNAME = "admin"
PASSWORD = "123"

# Create the login form
st.title("Login Page")
st.write("Please enter your credentials to log in")

# Input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Button to submit credentials
if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.success("Login successful!")
        st.write("Welcome,", username)
        # Here you could redirect to a different section of the app or display other content
    else:
        st.error("Invalid username or password. Please try again.")
