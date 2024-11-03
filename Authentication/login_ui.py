# login_ui.py
import streamlit as st
from Authentication.auth import authenticate

def show_login():
    """Display the login form and handle authentication."""
    st.title("Login")
    st.write("Please enter your credentials to log in.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if authenticate(username, password):
            st.success("Login successful!")
            return username
        else:
            st.error("Invalid username or password.")
            return None
