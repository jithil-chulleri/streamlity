import streamlit as st
import toml

# Load secrets based on environment
try:
    # Try to use Streamlit's secrets (for Streamlit Cloud)
    credentials = st.secrets["auth"]
except AttributeError:
    # If running locally, load from local secrets file
    with open("secrets.toml", "r") as f:
        credentials = toml.load(f)["auth"]

def authenticate(username, password):
    """Check if the provided username and password match any stored user."""
    for user in credentials.values():
        if user["username"] == username and user["password"] == password:
            return True
    return False
