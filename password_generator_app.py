import random
import string
import streamlit as st
import streamlit.components.v1 as components

# Function to generate password based on difficulty level
def generate_password(length, level):
    if level == 'Easy':
        characters = string.ascii_letters  # Only lowercase and uppercase letters
    elif level == 'Medium':
        characters = string.ascii_letters + string.digits  # Letters and numbers
    elif level == 'Hard':
        characters = string.ascii_letters + string.digits + string.punctuation  # Letters, numbers, and symbols
    else:
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit UI setup
st.title("Random Password Generator")

# Input for difficulty level
level = st.selectbox("Select the password difficulty level", ["Easy", "Medium", "Hard"])

# Input for password length
length = st.slider("Select the password length", min_value=8, max_value=64, value=8)

# Initialize session state for the password
if 'password' not in st.session_state:
    st.session_state.password = ""

# Button to generate password
if st.button("Generate Password"):
    st.session_state.password = generate_password(length, level)

# Display the generated password and copy functionality
if st.session_state.password:
    password = st.session_state.password
    
    # Display the generated password in a custom-styled immutable text input box
    st.markdown(
        f"""
        <style>
        .password-input {{
            color: #000000;
            background-color: #F5F5F5;
            border: 1px solid #D0D0D0;
            padding: 10px;
            border-radius: 4px;
            font-size: 16px;
            width: 100%;
        }}
        </style>
        <input type="text" value="{password}" class="password-input" readonly>
        """,
        unsafe_allow_html=True
    )

    # JavaScript for copying password
    copy_button_html = f"""
    <input type="text" value="{password}" id="password_input" readonly style="position:absolute; left:-9999px;">
    <button onclick="document.getElementById('password_input').select(); document.execCommand('copy'); alert('Password copied to clipboard!');">Copy Password</button>
    """
    components.html(copy_button_html, height=50)
else:
    st.write("Generate a password to display it here.")
