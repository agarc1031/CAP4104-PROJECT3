import streamlit as st
import time
import json
import os
from datetime import datetime

# Set up data path
DATA_FILE = "data/responses.json"
os.makedirs("data", exist_ok=True)

# Save response to file
def save_response(data):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            responses = json.load(f)
    else:
        responses = []
    responses.append(data)
    with open(DATA_FILE, "w") as f:
        json.dump(responses, f, indent=4)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 'consent'
if 'responses' not in st.session_state:
    st.session_state.responses = {}

st.title("Healthy Bites Usability Testing Tool")

# Step: Consent
if st.session_state.step == 'consent':
    st.header("Consent Form")
    if st.checkbox("I agree to participate in this usability study."):
        st.session_state.step = 'demographics'
        st.experimental_rerun()

# Step: Demographics
elif st.session_state.step == 'demographics':
    st.subheader("Demographic Information")
    st.session_state.responses['name'] = st.text_input("First Name")
    st.session_state.responses['age'] = st.slider("Age", 18, 80, 25)
    st.session_state.responses['background'] = st.selectbox("Field of Work", 
        ["Accounting", "Healthcare", "Education", "Retail", "Other"])
    if st.button("Continue to Task 1"):
        st.session_state.step = 'task1_start'
        st.experimental_rerun()

# Step: Task 1 Start
elif st.session_state.step == 'task1_start':
    st.subheader("Task 1: Search for a food and view gut health rating")
    if st.button("Start Task 1"):
        st.session_state.task1_start = time.time()
        st.session_state.step = 'task1'
        st.experimental_rerun()

# Step: Task 1
elif st.session_state.step == 'task1':
    st.success("Imagine you searched for 'banana' and viewed its gut rating.")
    success = st.radio("Did you complete this task?", ["Yes", "No"])
    difficulty = st.slider("Rate difficulty (1 = easy, 5 = hard)", 1, 5)
    if st.button("Continue to Task 2"):
        st.session_state.responses['task1'] = {
            'success': success,
            'difficulty': difficulty,
            'time': round(time.time() - st.session_state.task1_start, 2)
        }
        st.session_state.step = 'task2_start'
        st.experimental_rerun()

# Step: Task 2 Start
elif st.session_state.step == 'task2_start':
    st.subheader("Task 2: Interpret nutritional chart")
    if st.button("Start Task 2"):
        st.session_state.task2_start = time.time()
        st.session_state.step = 'task2'
        st.experimental_rerun()

# Step: Task 2
elif st.session_state.step == 'task2':
    st.success("Imagine you interpreted a pie chart about fiber and sugar.")
    success = st.radio("Did you complete this task?", ["Yes", "No"])
    difficulty = st.slider("Rate difficulty (1 = easy, 5 = hard)", 1, 5)
    if st.button("Continue to Task 3"):
        st.session_state.responses['task2'] = {
            'success': success,
            'difficulty': difficulty,
            'time': round(time.time() - st.session_state.task2_start, 2)
        }
        st.session_state.step = 'task3_start'
        st.experimental_rerun()

# Step: Task 3 Start
elif st.session_state.step == 'task3_start':
    st.subheader("Task 3: Submit feedback through the app")
    if st.button("Start Task 3"):
        st.session_state.task3_start = time.time()
        st.session_state.step = 'task3'
        st.experimental_rerun()

# Step: Task 3
elif st.session_state.step == 'task3':
    st.success("Imagine you typed a comment and clicked submit.")
    success = st.radio("Did you complete this task?", ["Yes", "No"])
    difficulty = st.slider("Rate difficulty (1 = easy, 5 = hard)", 1, 5)
    if st.button("Finish"):
        st.session_state.responses['task3'] = {
            'success': success,
            'difficulty': difficulty,
            'time': round(time.time() - st.session_state.task3_start, 2)
        }
        st.session_state.step = 'feedback'
        st.experimental_rerun()

# Step: Feedback
elif st.session_state.step == 'feedback':
    st.subheader("Final Feedback")
    feedback = st.text_area("Any final comments?")
    st.session_state.responses['feedback'] = feedback
    st.session_state.responses['timestamp'] = datetime.now().isoformat()

    save_response(st.session_state.responses)
    st.success("Thank you! Your data has been saved.")
    st.balloons()
    st.session_state.step = 'done'

# Step: Done
elif st.session_state.step == 'done':
    st.write("Test complete. You may close the browser or refresh to start again.")
