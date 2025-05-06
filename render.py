import streamlit as st

def render_text_input(label, key, default=""):
    return st.text_input(label, value=default, key=key)

def render_email_input(label, key, default=""):
    return st.text_input(label, value=default, key=key)

def render_password_input(label, key, default=""):
    return st.text_input(label, value=default, type="password", key=key)

def render_number_input(label, key, value=0):
    return st.number_input(label, key=key, value=value, step=1)

def render_checkbox(label, key, default=False):
    return st.checkbox(label, value=default, key=key)

def render_select_input(label, options, key, default=None):
    return st.selectbox(label, options, index=options.index(default) if default else 0, key=key)

def render_file_input(label, key):
    file = st.file_uploader(label, type=['jpg', 'png', 'pdf'], key=key)
    if file:
        return file.name 
    return None

def render_date_input(label, key):
    return st.date_input(label, key=key)

def render_multiselect(label, options, key):
    return st.multiselect(label, options, key=key)
