import streamlit as st
import requests

st.title("TravelAI Agent Hub 🌍🤖")

location = st.text_input("Enter travel destination")
days = st.number_input("Enter number of days", min_value=1, max_value=30)
interests = st.text_area("Enter interests (comma-separated)")

if st.button("Generate Itinerary & Content"):
    payload = {
        "location": location,
        "days": days,
        "interests": [i.strip() for i in interests.split(",")]
    }
    response = requests.post("http://localhost:8000/generate_itinerary", json=payload)
    data = response.json()

    st.subheader("Itinerary")
    for day, plan in data["itinerary"].items():
        st.write(f"{day}: {plan}")

    st.subheader("Content")
    for day, text in data["content"].items():
        st.write(f"{day}: {text}")