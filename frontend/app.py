import streamlit as st
import requests
import json

st.title("TravelAI Agent Hub 🌍🤖")

location = st.text_input("Enter travel destination")
days = st.number_input("Enter number of days", min_value=1, max_value=15)
interests = st.text_area("Enter interests (comma-separated)")

if st.button("Generate Itinerary & Content"):
    payload = {
        "location": location,
        "days": days,
        "interests": [i.strip() for i in interests.split(",")]
    }
    response = requests.post("http://localhost:8000/generate_itinerary", json=payload)
    data = response.json() #converts API response to python dict
    # print(json.dumps(data, indent=4))

    st.subheader("Full Itinerary")
    st.write(data["itinerary"])
    # for day, plan_parts in data["itinerary"].items():
    #     st.write(f"{day}:")
    #     for part in plan_parts:
    #         st.write(f"- {part}")

    # st.subheader("Content")
    # for day, enhanced_plan_parts in data["content"].items():
    #     st.write(f"{day}:")
    #     for part in enhanced_plan_parts:
    #         st.write(f"- {part}")