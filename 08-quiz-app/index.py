import streamlit as st
import random 
import time
import pathlib


def load_css(file_path):
    file = pathlib.Path(file_path)
    if file.exists():
        with open(file, "r") as f:
            css_content = f.read()
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

load_css("style.css")



st.title("Quiz App")

questions = [
       {   
        "question": "-> What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "-> Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "-> Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "-> What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "-> Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
]

# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    # assigns the random key of the questions list 
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question    

# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
selected_options = st.radio("Choose your option: ", question["options"])

if st.button("Submit Answer",key="green"):
    if selected_options == question["answer"]:
        st.success("✅Correct ")
    else:
        st.error(f"❌Wrong, The correct answer is **{question["answer"]}**. ")    

if st.button("Next Question", key="yellow"):
    st.toast("Next Question is displayed😍")  
    st.session_state.current_question = random.choice(questions)      
    st.rerun()