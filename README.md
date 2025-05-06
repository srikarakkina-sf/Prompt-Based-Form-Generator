
# 🧠 Prompt-Based Form Generator

This is an AI-powered Streamlit application that dynamically generates forms from natural language prompts. It is designed for rapid form prototyping and uses context-aware logic to produce accurate, relevant form fields based on your input.

## 🚀 Features

- ✅ Prompt-Based Form Generation – Generate full input forms just by describing them in plain English.
- 🧠 Context-Aware Memory (Non-Persistent) – Uses previous prompt and schema context during a session to generate more coherent and intelligent forms.
- 📦 Supports Various Field Types – Including text, email, password, numbers, checkboxes, dropdowns, file uploads, date pickers, and more.

### 📦 Installation Steps

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ````

2. **Install dependencies from `requirements.txt`:**

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Set up your API key:**

   * Visit [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
   * Generate an API key.
   * Replace the placeholder in `llm_engine.py` with your actual key.

4. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

5. **Open your browser:**
   Navigate to [http://localhost:8501/](http://localhost:8501/) and enter a prompt like:

   ```
   Create a form that collects the user's full name, email address, and password (along with a confirmation password). Include a field to input the user's age, allowing for values between 18 and 100. Add a checkbox for users to opt into a newsletter subscription, and provide an option for them to select their preferred meal choice from a list of options. Finally, include a section where users can upload a file if necessary, though this is optional. In addition, add a phone number field that validates typical phone formats, a date picker to allow users to select their date of birth, and a dropdown menu for selecting their country of residence from a predefined list.
   ```
   
---

## 🌱 Future Enhancements

* 🔌 **Integrate External Validation Tools** – e.g., for phone numbers, file types, or email verification
* 💾 **Add Persistent Memory** – Save and reuse form schemas across sessions
* 💡 **Support for Multi-Agent Architectures** – Enable modular tool/agent pipelines
