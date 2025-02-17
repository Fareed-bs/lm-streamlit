📌 Step 1: Clone the Repo to Your Laptop
Once the file is added, you can clone the repo to your laptop:

Open Terminal and navigate to the folder where you want to clone the repo:

cd path/to/your/desired/directory
Clone the repository:

git clone https://github.com/your-username/streamlit-app.git
Navigate to the cloned directory:

cd streamlit-app
📌 Step 2: Install Required Software
1️⃣ Install Python (if not installed)
First, ensure Python is installed. You can check by running:

python --version
If not installed, download from python.org and install it.

2️⃣ Install Streamlit
Streamlit is the UI framework we used. Install it globally or in a virtual environment:

pip install streamlit

3️⃣ Install LM Studio
Download LM Studio from: lmstudio.ai
Install it and download an LLM model (e.g., Llama-3.2-1b-instruct).
Start LM Studio and enable the API Server.

📌 Step 3: Run LM Studio API
Open LM Studio.
Go to the API Server tab (if not visible, update LM Studio).
Click Enable API Server.
Note the API URL (default is http://localhost:1234).
Open a browser and check if models are loaded by visiting:

http://localhost:1234/v1/models
Expected Output:
json
Copy
Edit
{
   "data": [
      {
         "id": "llama-3.2-1b-instruct",
         "object": "model",
         "owned_by": "organization_owner"
      }
   ],
   "object": "list"
}
If this appears, the API is working correctly.
📌 Step 4: Write the Streamlit App (app.py), save that in GitHub repository
We created a simple Python script to interact with the LM Studio API.

🔥 Final Streamlit Code (app.py)

import requests
import streamlit as st

# Set the API URL
url = "http://localhost:1234/v1/completions"  # Ensure LM Studio is running

# Streamlit UI
st.title("LM Studio API Chatbot")
st.write("Ask a question, and the model will respond.")

# User input (no default text)
user_input = st.text_input("Enter your question:")

# API Request Data
data = {
    "model": "llama-3.2-1b-instruct",  # Model ID from LM Studio
    "prompt": f"Provide a short and factual answer. Just give the answer without explanations.\n\nQ: {user_input}\nA:",  
    "max_tokens": 20,  # Limit response length
    "temperature": 0.2,  # Reduce randomness for accuracy
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
                st.success(result)  # Display answer in a success box
            else:
                st.error(f"Error: {response.status_code}")
                st.write(response.text)  # Display error details

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {str(e)}")
    else:
        st.warning("Please enter a question before submitting.")
        
📌 Step 5: Run the Streamlit App
🔹 Run Using Python Module (Recommended)
To ensure the correct environment, use:

python -m streamlit run app.py
or simply:

streamlit run app.py
(If streamlit is globally installed)

📌 Step 6: Interact with the Chatbot
Open the Streamlit web interface (automatically launches in a browser).
Enter a question (e.g., "What is the capital of France?").
Click "Get Answer".
The model responds (e.g., "Paris").
