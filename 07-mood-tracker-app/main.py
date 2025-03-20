import streamlit as st # for creating web interface
import pandas as pd # for data manipulation
import datetime # for date and time
import csv # for reading and writing to CSV files
import os # for file path operations

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv" 

# function to read mood data from the CSV file 
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date" , "Mood"])
    return pd.read_csv(MOOD_FILE)
# function to add new mood entry to CSV file 

def save_mood_data(date, mood):
    with open(MOOD_FILE, "a") as file:

        writer = csv.writer(file)
        writer.writerow([date, mood] )

        
st.title("Mood Tracker App")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry","Stressed","Anxious","Excited","Content"])

if st.button("log Mood"):
    save_mood_data(today, mood)
    st.success("Mood logged successfully!")

data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trends over Time")

    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)

st.write("Build with ❤️ by [Shahab](https://github.com/Shahab155)")    