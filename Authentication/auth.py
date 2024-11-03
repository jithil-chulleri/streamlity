# auth.py
import streamlit as st

def authenticate(username, password):
    """Check if the username and password match the stored credentials."""
    # Read the credentials from Streamlit secrets
    stored_username = st.secrets["auth"]["username"]
    stored_password = st.secrets["auth"]["password"]
    
    return username == stored_username and password == stored_password
