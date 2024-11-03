# Define user credentials (for demo purposes)
USERNAME = "admin"
PASSWORD = "123"

def authenticate(username, password):
    """Check if the username and password are correct."""
    return username == USERNAME and password == PASSWORD
