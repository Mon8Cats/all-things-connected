import streamlit as st
import requests
import json

def query_ollama(model, prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, data=json.dumps(data))
        response.raise_for_status()
        return response.json()['response']
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with Ollama: {e}")
        return None

st.title("Local MCP with Ollama")
model_name = st.selectbox("Select Model", ["llama2"]) # Add more models if you've pulled them
prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating..."):
            output = query_ollama(model_name, prompt)
        if output:
            st.subheader("Ollama Output:")
            st.write(output)
    else:
        st.warning("Please enter a prompt.")
        
