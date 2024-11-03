# login_ui.py

import streamlit as st
from Authentication.auth import authenticate  # Import the authentication function

def show_login():
    """Render the login UI and handle user interaction."""
    st.title("Login Page")
    st.write("Please enter your credentials to log in")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Button to submit credentials
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            st.write("Welcome,", username)
            # Here you could redirect to another section of the app or show more content
        else:
            st.error("Invalid username or password. Please try again.")
