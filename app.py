import requests
import streamlit as st

# Set the API URL
url = "http://localhost:1234/v1/completions"  # Ensure this is the correct URL

# Streamlit UI
st.title("LM Studio API Chatbot")
st.write("Ask a question, and the model will respond.")

# User input (without default text)
user_input = st.text_input("Enter your question:")

# API Request Data
data = {
    "model": "llama-3.2-1b-instruct",  # Model ID from LM Studio
    "prompt": f"Provide a short and factual answer. Just give the answer without explanations.\n\nQ: {user_input}\nA:",  
    "max_tokens": 20,  # Limit the response length
    "temperature": 0.2,  # Reduce randomness for more factual responses
    "stop": ["\n"]  # Stop after the first answer
}

# Button to submit the query
if st.button("Get Answer"):
    if user_input.strip():  # Check if input is not empty
        try:
            response = requests.post(url, json=data)

            if response.status_code == 200:
                result = response.json().get("choices", [{}])[0].get("text", "").strip()
                st.write("Response from API:")
                st.success(result)  # Display the answer in a success box
            else:
                st.error(f"Error: {response.status_code}")
                st.write(response.text)  # Display error details

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {str(e)}")
    else:
        st.warning("Please enter a question before submitting.")
