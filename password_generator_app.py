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
    
    password = ''.join(random.choice(characters) for i in range(length))
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

# Display the generated password
if st.session_state.password:
    st.text_input("Generated Password:", value=st.session_state.password, key='password_display')

    # JavaScript to copy password to clipboard
    copy_code = """
    <script>
    function copyToClipboard() {
        var copyText = document.getElementById("password-display");
        copyText.select();
        document.execCommand("copy");
    }
    </script>
    <button onclick="copyToClipboard()">Copy Password</button>
    """
    components.html(copy_code, height=0)
else:
    st.write("Generate a password to display it here.")

