import os
import re
import json
import google.generativeai as genai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


previous_prompts = []
previous_schemas = []

# Configure the Gemini API
def configure_gemini():
    api_key = ""
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    genai.configure(api_key=api_key)

# Function to extract JSON from the response text
def extract_json_from_response(text):
    # Remove Markdown-style code blocks
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return text.strip()

# Function to calculate similarity between two prompts
def calculate_similarity(prompt1, prompt2):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([prompt1, prompt2])
    return cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

# Function to find the best matching prompt from previous prompts
def find_best_matching_prompt(new_prompt):
    for idx, old_prompt in enumerate(previous_prompts):
        similarity = calculate_similarity(new_prompt, old_prompt)
        if similarity >= 0.80:
            return previous_schemas[idx], similarity
    return None, 0

# Function to generate a schema based on the prompt
def generate_schema(prompt: str) -> dict:
    configure_gemini()

    try:
        best_schema, similarity = find_best_matching_prompt(prompt)
        print(f"Previous prompts stored: {len(previous_prompts)}")
        print(f"Similarity with previous prompts: {similarity*100:.2f}%")
        if best_schema:
            print(f"Reusing schema from previous prompt with similarity: {similarity*100:.2f}%")
            prompt = f"Using the following schema: {json.dumps(best_schema)}. Now enhance the form based on the new description: {prompt}"

        model = genai.GenerativeModel('gemini-2.0-flash')

        response = model.generate_content(
            f"""You are a form generator. Given a user's description, output a JSON schema.
            Respond ONLY with a JSON object with: title, fields (name, type, label, required, etc.)
            User Description: "{prompt}"
            Respond with JSON only."""
        )

        raw_json = extract_json_from_response(response.text)
        
        if not raw_json:
            raise ValueError("No valid JSON schema found in the response.")

        previous_prompts.append(prompt)  # Store the current prompt
        previous_schemas.append(raw_json)  # Store the generated schema
        
        return json.loads(raw_json)

    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse the schema as valid JSON: {e}")
    except Exception as e:
        raise ValueError(f"Error during schema generation: {e}")
