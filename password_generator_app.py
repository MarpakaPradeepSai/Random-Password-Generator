import random
import string
import streamlit as st
import pyperclip

# Function to generate password based on difficulty level
def generate_password(length, level):
    if level == 'easy':
        characters = string.ascii_letters  # Only lowercase and uppercase letters
    elif level == 'medium':
        characters = string.ascii_letters + string.digits  # Letters and numbers
    elif level == 'hard':
        characters = string.ascii_letters + string.digits + string.punctuation  # Letters, numbers, and symbols
    else:
        return None
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to copy password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(password)
    st.success("Password copied to clipboard!")

# Streamlit UI setup
st.title("Random Password Generator")

# Input for password length
length = st.slider("Select the password length", min_value=6, max_value=24, value=12)

# Input for difficulty level
level = st.selectbox("Select the password difficulty level", ["easy", "medium", "hard"])

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(length, level)
    if password:
        # Create two columns for password display and copy button
        col1, col2 = st.columns([3, 1])
        
        # Display password in a text input field
        with col1:
            st.text_input("Generated Password", value=password, key="password_field", disabled=True)
        
        # Copy button
        with col2:
            if st.button("Copy"):
                copy_to_clipboard(password)
    else:
        st.error("Something went wrong. Please try again.")
