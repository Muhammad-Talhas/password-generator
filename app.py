import streamlit as st
import random
import string

# Set page configuration (should be the first Streamlit command)
st.set_page_config(
    page_title="Password Generator",
    page_icon="🔑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
def add_custom_css():
    st.markdown("""
        <style>
            body {
                background-color: #f4f4f4;
                font-family: 'Arial', sans-serif;
            }
            .stSlider, .stCheckbox, .stButton {
                font-size: 18px;
            }
            .stButton button {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px;
                border: none;
                font-weight: bold;
                transition: 0.3s;
            }
            .stButton button:hover {
                background-color: #45a049;
            }
            .stTextInput, .stSelectbox, .stNumberInput {
                font-size: 16px;
                padding: 8px;
                border-radius: 5px;
            }
            .generated-password {
                font-size: 20px;
                font-weight: bold;
                color: #d35400;
                background: #fce4d6;
                padding: 8px;
                border-radius: 8px;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

# Function to generate password
def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Add CSS styling
add_custom_css()

# Streamlit App Title
st.title("🔑 Password Generator")

# User Inputs
length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special_chars = st.checkbox("Include Special Characters")

# Generate Button
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_chars)
    st.markdown(f'<div class="generated-password">{password}</div>', unsafe_allow_html=True)

st.write("---")
st.write("✨ Built by [Muhammad Talha](https://github.com/Muhammad-Talhas) ✨")
