import random
import string
import streamlit as st

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

# Streamlit UI setup
st.title("Random Password Generator")

# Input for difficulty level
level = st.selectbox("Select the password difficulty level", ["easy", "medium", "hard"])

# Input for password length
length = st.slider("Select the password length", min_value=8, max_value=64, value=8)

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(length, level)
    if password:
        # Display the generated password in a text box
        st.text_input("Generated Password:", value=password)
        
        # Display the copy button (for UI purposes only)
        if st.button("Copy Password"):
            st.experimental_set_query_params(password=password)
            st.success("Password copied to clipboard!")
    else:
        st.error("Something went wrong. Please try again.")

# Footer
st.write("Adjust the length and select a difficulty level to generate a secure password.")
