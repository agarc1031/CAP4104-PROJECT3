import streamlit as st
import time
import json
import os
from datetime import datetime

# File to store results
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

# Step 1: Consent
st.header("Consent Form")
if st.checkbox("I agree to participate in this usability study."):
    
    # Step 2: Demographic Information
    st.subheader("Demographic Questionnaire")
    name = st.text_input("First Name")
    age = st.slider("Age", 18, 80)
    background = st.selectbox("Field of Work", ["Accounting", "Healthcare", "Education", "Retail", "Other"])
    
    # Step 3: Task 1
    st.subheader("Task 1: Search for a food and view gut health rating")
    if st.button("Start Task 1"):
        t1_start = time.time()
        st.success("Imagine you searched for 'banana' and viewed its gut rating.")
        task1_success = st.radio("Did you complete this task?", ["Yes", "No"])
        task1_difficulty = st.slider("Rate task difficulty (1 = easy, 5 = hard)", 1, 5)
        t1_end = time.time()
        task1_time = round(t1_end - t1_start, 2)
    
        # Task 2
        st.subheader("Task 2: Interpret nutritional chart")
        if st.button("Start Task 2"):
            t2_start = time.time()
            st.success("Imagine you interpreted a pie chart about fiber and sugar.")
            task2_success = st.radio("Did you complete this task?", ["Yes", "No"])
            task2_difficulty = st.slider("Rate task difficulty (1 = easy, 5 = hard)", 1, 5)
            t2_end = time.time()
            task2_time = round(t2_end - t2_start, 2)
            
            # Task 3
            st.subheader("Task 3: Submit feedback through the app")
            if st.button("Start Task 3"):
                t3_start = time.time()
                st.success("Imagine you typed a comment and clicked submit.")
                task3_success = st.radio("Did you complete this task?", ["Yes", "No"])
                task3_difficulty = st.slider("Rate task difficulty (1 = easy, 5 = hard)", 1, 5)
                t3_end = time.time()
                task3_time = round(t3_end - t3_start, 2)
                
                # Exit feedback
                st.subheader("Exit Feedback")
                feedback = st.text_area("Any final comments about your experience?")
                
                # Save results
                result = {
                    "timestamp": datetime.now().isoformat(),
                    "participant": {
                        "name": name,
                        "age": age,
                        "background": background
                    },
                    "tasks": {
                        "task1": {"success": task1_success, "difficulty": task1_difficulty, "time": task1_time},
                        "task2": {"success": task2_success, "difficulty": task2_difficulty, "time": task2_time},
                        "task3": {"success": task3_success, "difficulty": task3_difficulty, "time": task3_time}
                    },
                    "feedback": feedback
                }
                
                save_response(result)
                st.success("Thank you! Your responses were recorded.")
