# app.py
import streamlit as st
from Authentication.login_ui import show_login
from Authentication.auth import authenticate

# Initialize session state variables for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# Define the main app logic
def main():
    if not st.session_state.logged_in:
        # Show login form if not logged in
        username = show_login()
        if username:
            st.session_state.logged_in = True
            st.session_state.username = username
    else:
        # Show the welcome message and Yes/No question
        st.write(f"Welcome, {st.session_state.username}!")
        ask_question()

def ask_question():
    st.write("Would you like to proceed?")
    response = st.radio("Please select:", ("Yes", "No"))

    # Respond based on user's choice
    if response == "Yes":
        st.write("Great! Let's continue.")
    elif response == "No":
        st.write("Alright, feel free to ask any questions if you have them!")

if __name__ == "__main__":
    main()
