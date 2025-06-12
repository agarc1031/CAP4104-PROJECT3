import streamlit as st
import time
import json
import os
from datetime import datetime

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

# Initialize session state variables
if 'task' not in st.session_state:
    st.session_state.task = 0
if 'responses' not in st.session_state:
    st.session_state.responses = {}

st.title("Healthy Bites Usability Testing Tool")

# Consent
st.header("Consent Form")
if st.checkbox("I agree to participate in this usability study."):
    
    # Demographic Information
    st.subheader("Demographic Questionnaire")
    st.session_state.responses['name'] = st.text_input("First Name", st.session_state.responses.get('name', ''))
    st.session_state.responses['age'] = st.slider("Age", 18, 80, st.session_state.responses.get('age', 25))
    st.session_state.responses['background'] = st.selectbox("Field of Work", 
        ["Accounting", "Healthcare", "Education", "Retail", "Other"],
        index=["Accounting", "Healthcare", "Education", "Retail", "Other"].index(st.session_state.responses.get('background', 'Accounting'))
    )

    # Task 1
    if st.session_state.task == 0:
        st.subheader("Task 1: Search for a food and view gut health rating")
        if st.button("Start Task 1"):
            st.session_state.task1_start = time.time()
            st.session_state.task = 1

    if st.session_state.task == 1:
        st.success("Imagine you searched for 'banana' and viewed its gut rating.")
        task1_success = st.radio("Did you complete this task?", ["Yes", "No"], key="t1s")
        task1_difficulty = st.slider("Rate task difficulty (1 = easy, 5 = hard)", 1, 5, key="t1d")
        if st.button("Next to Task 2"):
            st.session_state.responses["task1"] = {
                "success": task1_success,
                "difficulty": task1_difficulty,
                "time": round(time.time() - st.session_state.task1_start, 2)
            }
            st.session_state.task = 2

    # Task 2
    if st.session_state.task == 2:
        st.subheader("Task 2: Interpret nutritional chart")
        if st.button("Start Task 2"):
            st.session_state.task2_start = time.time()
            st.session_state.task = 3

    if st.session_state.task == 3:
        st.success("Imagine you interpreted a pie chart about fiber and sugar.")
        task2_success = st.radio("Did you complete this task?", ["Yes", "No"], key="t2s")
        task2_difficulty = st.slider("Rate task difficulty (1 = easy, 5 = hard)", 1, 5, key="t2d")
        if st.button("Next to Task 3"):
            st.session_state.responses["task2"] = {
                "success": task2_success,
                "difficulty": task2_difficulty,
                "time": round(time.time() - st.session_state.task2_start, 2)
            }
            st.session_state.task = 4

    # Task 3
    if st.session_state.task == 4:
        st.subheader("Task 3: Submit feedback through the app")
        if st.button("Start Task 3"):
            st.session_state.task3_start = time.time()
            st.session_state.task = 5

    if st.session_state.task == 5:
        st.success("Imagine you typed a comment and clicked submit.")
        task3_success = st.radio("Did you complete this task?", ["Yes", "No"], key="t3s")
        task3_difficulty = st.slider("Rate task difficulty (1 = easy, 5 = hard)", 1, 5, key="t3d")
        if st.button("Finish Test"):
            st.session_state.responses["task3"] = {
                "success": task3_success,
                "difficulty": task3_difficulty,
                "time": round(time.time() - st.session_state.task3_start, 2)
            }
            st.session_state.task = 6

    # Feedback and save
    if st.session_state.task == 6:
        st.subheader("Exit Feedback")
        feedback = st.text_area("Any final comments about your experience?")
        st.session_state.responses["feedback"] = feedback
        st.session_state.responses["timestamp"] = datetime.now().isoformat()

        save_response(st.session_state.responses)
        st.success("Thank you! Your responses were saved.")
        st.session_state.task = 7

    if st.session_state.task == 7:
        st.balloons()
        st.write("You may now close this window or refresh to start a new session.")
