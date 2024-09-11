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
st.markdown("""
<style>
    .title {
        text-align: center;
    }
    .stButton > button {
        color: white !important;
        background-color: red !important;
        border-color: red !important;
    }
    .stButton > button:hover, .stButton > button:focus, .stButton > button:active {
        color: white !important;
        background-color: red !important;
        border-color: red !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Random Password Generator</h1>", unsafe_allow_html=True)

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
    # HTML and JavaScript for password display and copying
    html_code = f"""
    <style>
    .container {{
        display: flex;
        align-items: center;
    }}
    .password-input {{
        color: #000000;
        background-color: #F5F5F5;
        border: 1px solid #D0D0D0;
        padding: 10px;
        border-radius: 4px;
        font-size: 14px;
        width: 300px;
        margin-right: 10px;
    }}
    .copy-button {{
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        background-color: #0056b3;
        color: white;
        cursor: pointer;
    }}
    .copy-button:hover {{
        background-color: #004494;
    }}
    </style>
    <div class="container">
        <input type="text" value="{password}" class="password-input" id="password_input" readonly>
        <button class="copy-button" onclick="copyToClipboard()">Copy Password</button>
    </div>
    <script>
    function copyToClipboard() {{
        var copyText = document.getElementById('password_input');
        copyText.select();
        document.execCommand('copy');
        alert('Password copied to clipboard!');
    }}
    </script>
    """
    # Render the HTML and JavaScript
    components.html(html_code, height=80)
else:
    st.write("Generate a password to display it here.")
