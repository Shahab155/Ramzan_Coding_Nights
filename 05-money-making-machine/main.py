import streamlit as st
import random 
import time
import requests

st.title("💸Money Making Machine💰")

def generate_money():
    return random.randint(1,1000)

if st.button("Generate money"):
    result = generate_money()
    st.write("Counting your money..")
    time.sleep(1)
    st.success(f"You made ${result}")

def fetch_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        hustles = response.json()
        return hustles["side_hustle"]
    except:
        return ("Freelancing.")

st.subheader("Side Hustle ideas")
if st.button("Generate Hustle"):
   hustle = fetch_side_hustles()
   st.toast("Fetching hustle...")
   time.sleep(2)
   st.success(hustle)


def fetch_money_quotes():
    try:
      response = requests.get("http://127.0.0.1:8000/money_quotes")
      quote = response.json()
      return quote["money_quote"]
    except:
        return ("Money is the root of all evil.")

st.subheader("Money Making Motivation")
if st.button("Generate Quote"):
    quote = fetch_money_quotes()
    st.toast("Fetching quote....")
    time.sleep(2)
    st.success(quote)
