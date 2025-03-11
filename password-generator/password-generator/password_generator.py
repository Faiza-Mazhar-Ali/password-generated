import streamlit as st  # type: ignore
import random
import string

def password_generator(length, use_digits, use_special, use_uppercase):
    # Initialize charactors with lowercase letters
    charactors = string.ascii_lowercase

    # Add uppercase letters if selected
    if use_uppercase:
        charactors += string.ascii_uppercase
     
      # Adds numbers (0-9) as well if selected 
    if use_digits:
        charactors += string.digits

    # Adds special characters  (!, @, #, $, %, ^, &, *, etc.) if selected
    if use_special:
        charactors += string.punctuation 

# Ensure the characters set is not empty
    if not charactors:
        return "Please select at least one character type!"

    # Generate the password
    return ''.join(random.choice(charactors) for _ in range(length))

st.title("🔐Password Generator")

length = st.number_input("Select the lenght of your password", min_value=8, max_value=32, value=16)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

use_uppercase = st.checkbox("Include Uppercase Letters")

if st.button("Generate Password"):
    password = password_generator(length, use_digits, use_special, use_uppercase)
    st.success(f"Generated Password: {password}")

    st.write("🔑 Save your password securely!")

    st.write("Build with ❤️ by [Faiza Mazhar Ali](https://github.com/faiza-mazhar-ali)")






