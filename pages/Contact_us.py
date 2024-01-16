import streamlit as st
from send_email import send_email
st.header("Contact Me")

with st.form(key="email_form"):
    email_input=st.text_input("Enter your email here:")
    raw_message=st.text_input("Enter message here:")
    message = f"""\
Subject: New email from {email_input}

From: {email_input}
{raw_message}"""
    buttton=st.form_submit_button("Submit")
    if buttton:
        send_email(message)
        st.info("Email was sent successfully")

