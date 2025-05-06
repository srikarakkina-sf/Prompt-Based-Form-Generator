import streamlit as st
from llm_engine import generate_schema
from schema_utils import render_form

st.title("PromptFormAI - Generate Forms from Prompts")

prompt = st.text_area("Enter form description:", "Registration form with name, email, and password")

if st.button("Generate Form"):
    try:
        schema = generate_schema(prompt)
        render_form(schema)
    except Exception as e:
        st.error(f"Error: {e}")
