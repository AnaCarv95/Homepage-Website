import streamlit as st
import send_email as se

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Enter your message")
    message = f"""Subject: New email from my contact Python page

From: {user_email}

{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        se.send_email(message)
        st.info("Your email was sent! Thanks for contacting me")

