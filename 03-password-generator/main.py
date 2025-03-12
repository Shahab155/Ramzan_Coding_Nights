import streamlit as st
import random # Importing the random library for generating random characters
import string # Import the string for using string characters


def generate_password(length,use_digits,use_special):
    characters = string.ascii_letters # provides uppercase and lowercase characters (a-z) (A-Z)

    if use_digits:
        characters += string.digits # provides number from  0 to 9

    if use_special: 
        characters += string.punctuation  # provides special characters 
# This line generate the random passwor based on user preferences 
    return ''.join(random.choice(characters) for _ in range(length))
#  underscore(_)  tells python that loop does not have length(specified) 

st.sidebar.title("💥Welcome to my App")
name = st.sidebar.text_input("Name: ")
email = st.sidebar.text_input("Email: ")
message = st.sidebar.text_area("Comments: ")

if st.sidebar.button("Submit"):
    st.sidebar.success(f"Welcome! {name}")


st.title("🔒 Random Password Generator")

length = st.slider("Select Password Length", min_value=4 , max_value=50, value=12) # value 12 for by default values

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.text_input("Generated Password: ", password, type="password")
    st.success("Password generated Successfully✅")
    st.toast("🔔Password is ready!")
    
st.subheader("Build with 💖 by Shahab")

