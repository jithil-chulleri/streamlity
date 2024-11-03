# auth.py
import streamlit as st

def authenticate(username, password):
    """Check if the provided username and password match any stored user."""
    for user in st.secrets["auth"].values():
        if user["username"] == username and user["password"] == password:
            return True
    return False
