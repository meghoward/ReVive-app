import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st


# File to store visitor count
VISITOR_COUNT_FILE = "visitor_count.txt"

# Function to get the current visitor count
def get_visitor_count():
    try:
        with open(VISITOR_COUNT_FILE, "r") as file:
            count = int(file.read().strip())
    except FileNotFoundError:
        count = 0
    return count

# Function to increment and save visitor count
def increment_visitor_count():
    count = get_visitor_count() + 1
    with open(VISITOR_COUNT_FILE, "w") as file:
        file.write(str(count))
    return count

# Increment visitor count when the app loads
visitor_number = increment_visitor_count()

# Centered Title
st.markdown(
    """
    <div style="text-align: center;">
        <h1>✨ ReflectAI ✨</h1>
    </div>
    """,
    unsafe_allow_html=True,
)
# Centered Introduction
st.markdown(
    """
    <div style="text-align: center;">
        <h1>Turning Reflection Into Growth</h1>
    </div>
    """,
    unsafe_allow_html=True,
)
# Where Emotions Meet Insight.
# Empowering You to Process 

# Simplifying the Path to Emotional Well-Being
# Personalized Support for Your Emotional Health.

# Subheading
# st.subheader("We’re developing an app that helps you process your emotions and improve your mental health in a more effortless and trackable way.")
st.subheader("Do You Journal? Help Us Build a Tool That Works for You 🌱")

# Body Text
st.write(
    "We’re conducting research to build a tool that genuinely supports your emotional well-being. We understand that everyone’s journey is unique, and we want to make emotional processing more intuitive, meaningful, and approachable."
)

st.write(
    "By participating in this survey, you’re helping us uncover the gaps and challenges in current tools and shaping a solution that genuinely makes a difference. Your thoughts and experiences are at the heart of what we’re building."
)

# Bulleted List
st.write("- **Your privacy matters:** All responses are completely anonymous and used only to guide our development.")
st.write("- **Be part of the journey:** Participants will receive exclusive early access to ReflectAI, giving you the opportunity to influence the features that matter most to you.")

# Call to Action
st.write(
    "*Your voice matters. Together, we can build something that truly helps. Please take a few minutes to share your insights below.*"
)

# Embedding Google Forms Survey
st.markdown(
    """
    <div style="text-align: center;">
        <h3>Take Our Survey!</h3>
        <iframe src="https://forms.gle/SohMxvhXDMbpUsTp6" width="640" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div>
    """,
    unsafe_allow_html=True,
)

# Optional Survey Form
# Uncomment the following section if you prefer a built-in form
# name = st.text_input("What's your name?")
# email = st.text_input("What's your email?")
# experience = st.radio("How often do you engage in activities like journaling or emotional processing?", ["Daily", "Weekly", "Occasionally", "Never"])
# challenges = st.text_area("What challenges or frustrations do you encounter with current tools or methods?")
# improvements = st.text_area("If you could change one thing about the tools you currently use, what would it be?")
# opt_in = st.checkbox("I agree to participate in the research and receive early access to ReflectAI.")

# # Submit Button
# if st.button("Submit"):
#     if name and email and opt_in:
#         st.success("Thank you for completing the survey! Your responses have been recorded.")
#     else:
#         st.error("Please fill in all the required fields and agree to participate.")

# Display the visitor count on the Streamlit site
st.markdown(
    f"""
    <div style="text-align: center; font-size: small;">
        You are visitor number: <strong>{visitor_number}</strong>! Thank you so so much for contributing to ReflectAI!🥰
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown(
    """
    <div style="text-align: center; font-size: small;">
        ReflectAI © 2024 | Simplifying the Path to Emotional Well-Being.
    </div>
    """,
    unsafe_allow_html=True,
)