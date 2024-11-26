import streamlit as st
import pandas as pd
import numpy as np


# Centered Title
st.markdown(
    """
    <div style="text-align: center;">
        <h1>✨ ReVive ✨</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Centered Introduction
st.markdown(
    """
    <div style="text-align: center;">
        Welcome to the Future of Easy, Sustainable Fashion with ReVive!  
    </div>
    """,
    unsafe_allow_html=True,
)

# Subheading
st.subheader("We’re reimagining the way you buy, sell, and swap second-hand clothes—stylishly, sustainably, and effortlessly."
)

# Body Text
st.write(
    "**We’re conducting research to create a platform that prioritizes style, environmental impact, and quick transactions.**")

st.write("Your input will help us build Revive into the ultimate marketplace for sustainable fashion lovers like you."
)

st.write(
    "We want to know what works, what doesn’t, and what’s missing in your experience with current second-hand platforms."
)

# Bulleted List
st.write("- **Confidentiality guaranteed:** Your responses will remain anonymous and are used only to guide our development process.")
st.write("- **Thank you gift:** Complete the survey and gain early access to ReVive when it launches.")

# Call to Action
st.write("*Your ideas will make a difference! Join us in shaping the future of ReVive by participating in our survey.*")

# Embedding Google Forms Survey
st.markdown(
    """
    <div style="text-align: center;">
        <h3>Take our Survey!</h3>
        <iframe src="https://forms.gle/R8CiB1xiiwJ72vtk9" width="640" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div>
    """,
    unsafe_allow_html=True,
)

# Survey Form
# st.write("### Survey")

# name = st.text_input("What's your name?")
# email = st.text_input("What's your email?")
# experience = st.radio("How would you rate your experience with current second-hand platforms?", ["Excellent", "Good", "Average", "Poor"])
# improvements = st.text_area("What improvements would you like to see in a second-hand clothing platform?")
# opt_in = st.checkbox("I agree to participate in the research and receive early access to ReVive.")

# # Submit Button
# if st.button("Submit"):
#     if name and email and experience and opt_in:
#         st.success("Thank you for completing the survey! Your responses have been recorded.")
#     else:
#         st.error("Please fill in all the required fields and agree to participate.")


# st.write(
   # "For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

