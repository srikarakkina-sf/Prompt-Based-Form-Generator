def validate_form(responses):
    errors = []
    
    if responses.get("password") != responses.get("confirm_password"):
        errors.append("Passwords do not match.")
    
    if not responses.get("uploaded_file"):
        errors.append("Please upload a file.")

    return errors
