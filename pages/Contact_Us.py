import streamlit as st 

from send_email import send_email

st.title("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}
From: {user_email}
{raw_message}
"""
    # Add a submit button inside the form
    submit_button = st.form_submit_button(label="Submit")

    # You can handle the form submission here
    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully")
        