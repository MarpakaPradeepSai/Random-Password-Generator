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

# HTML and JavaScript for button with custom styling
html_code = f"""
<style>
.generate-button {{
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    background-color: #FF0000; /* Red color */
    color: white;
    cursor: pointer;
    font-size: 16px;
    margin-bottom: 20px;
}}
.generate-button:hover {{
    background-color: #CC0000; /* Darker red on hover */
}}
</style>
<div>
    <button class="generate-button" onclick="generatePassword()">Generate Password</button>
</div>
<script>
function generatePassword() {{
    // Simulate button click in Streamlit app
    window.parent.postMessage({{ type: 'generate_password' }}, '*');
}}
</script>
"""

# Render the custom HTML for the generate password button
components.html(html_code, height=60)

# Handle custom message from JavaScript to generate password
st.markdown(
    """
    <script>
    window.addEventListener('message', function(event) {
        if (event.data.type === 'generate_password') {
            document.getElementById('generate_password_button').click();
        }
    });
    </script>
    """,
    unsafe_allow_html=True
)

# Button to generate password in Streamlit
generate_button = st.button("Generate Password", key='generate_password_button')

# Generate password when the button is clicked
if generate_button:
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
        font-size: 16px;
        width: 300px;
        margin-right: 10px;
    }}
    .copy-button {{
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        background-color: #007BFF;
        color: white;
        cursor: pointer;
    }}
    .copy-button:hover {{
        background-color: #0056b3;
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
