import streamlit as st
import json
import os
from datetime import datetime
import time

# Setup
DATA_FILE = "data/responses.json"
os.makedirs("data", exist_ok=True)

def save_response(data):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            responses = json.load(f)
    else:
        responses = []
    responses.append(data)
    with open(DATA_FILE, "w") as f:
        json.dump(responses, f, indent=4)

st.title("Healthy Bites Usability Testing Tool")

# Consent and Demographics
st.header("Consent and Demographics")
consent = st.checkbox("I agree to participate in this usability study.")
if consent:
    name = st.text_input("First Name")
    age = st.slider("Age", 18, 80, 25)
    background = st.selectbox("Field of Work", ["Accounting", "Healthcare", "Education", "Retail", "Other"])

    st.divider()

    # Task 1
    st.header("Task 1: Search for a food and view gut health rating")
    st.caption("Imagine you searched for 'banana' and viewed its gut rating.")
    task1_success = st.radio("Did you complete this task?", ["Yes", "No"], key="task1_success")
    task1_difficulty = st.slider("Rate difficulty (1 = easy, 5 = hard)", 1, 5, key="task1_difficulty")
    task1_time = st.number_input("Time taken (in seconds)", min_value=0.0, step=1.0, key="task1_time")

    st.divider()

    # Task 2
    st.header("Task 2: Interpret nutritional chart")
    st.caption("Imagine you interpreted a pie chart showing fiber and sugar content.")
    task2_success = st.radio("Did you complete this task?", ["Yes", "No"], key="task2_success")
    task2_difficulty = st.slider("Rate difficulty (1 = easy, 5 = hard)", 1, 5, key="task2_difficulty")
    task2_time = st.number_input("Time taken (in seconds)", min_value=0.0, step=1.0, key="task2_time")

    st.divider()

    # Task 3
    st.header("Task 3: Submit feedback through the app")
    st.caption("Imagine you typed a comment and clicked submit.")
    task3_success = st.radio("Did you complete this task?", ["Yes", "No"], key="task3_success")
    task3_difficulty = st.slider("Rate difficulty (1 = easy, 5 = hard)", 1, 5, key="task3_difficulty")
    task3_time = st.number_input("Time taken (in seconds)", min_value=0.0, step=1.0, key="task3_time")

    st.divider()

    # Exit Feedback
    st.header("Final Feedback")
    feedback = st.text_area("Any final comments or suggestions about your experience?")

    # Save
    if st.button("Submit All Responses"):
        data = {
            "timestamp": datetime.now().isoformat(),
            "participant": {
                "name": name,
                "age": age,
                "background": background
            },
            "tasks": {
                "task1": {
                    "success": task1_success,
                    "difficulty": task1_difficulty,
                    "time": task1_time
                },
                "task2": {
                    "success": task2_success,
                    "difficulty": task2_difficulty,
                    "time": task2_time
                },
                "task3": {
                    "success": task3_success,
                    "difficulty": task3_difficulty,
                    "time": task3_time
                }
            },
            "feedback": feedback
        }
        save_response(data)
        st.success("Thank you! Your responses have been saved.")
