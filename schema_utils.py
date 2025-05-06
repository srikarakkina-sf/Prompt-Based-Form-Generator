import streamlit as st
from render import (
    render_text_input, render_email_input, render_password_input,
    render_number_input, render_checkbox, render_select_input, render_file_input,
    render_date_input, render_multiselect
)
from validations import validate_form

def render_form(schema: dict):
    st.subheader(schema.get("title", "Generated Form"))

    if "form_data" not in st.session_state:
        st.session_state.form_data = {}

    responses = st.session_state.form_data

    for field in schema.get("fields", []):
        field_type = field.get("type", "text").lower()
        label = field.get("label", field.get("name", ""))
        required = field.get("required", False)
        key = field["name"]
        default = field.get("default", "")
        value = responses.get(key, default)

        if field_type == "text":
            responses[key] = render_text_input(label, key, value)
        elif field_type == "email":
            responses[key] = render_email_input(label, key, value)
        elif field_type == "password":
            responses[key] = render_password_input(label, key, value)
        elif field_type == "number":
            responses[key] = render_number_input(label, key, int(value) if value else 0)
        elif field_type == "checkbox":
            responses[key] = render_checkbox(label, key, value)
        elif field_type == "select":
            options = field.get("options", [])
            responses[key] = render_select_input(label, options, key, value)
        elif field_type == "file":
            responses[key] = render_file_input(label, key)
        elif field_type == "date":
            responses[key] = render_date_input(label, key)
        elif field_type == "multiselect":
            options = field.get("options", [])
            responses[key] = render_multiselect(label, options, key, value)
        else:
            responses[key] = render_text_input(label, key, value)

    if st.button("Submit"):
        errors = validate_form(responses)
        if errors:
            st.error("\n".join(errors))
        else:
            st.session_state.form_data = responses
            st.success("Form submitted successfully!")
            st.write("Form Responses:")
            st.json(responses)