import requests
import json

def query_ollama(model, prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False  # Set to True for streaming responses
    }
    try:
        response = requests.post(url, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()['response']
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return None

if __name__ == "__main__":
    model_name = "llama2"  # Change this to the model you pulled
    user_prompt = input("Enter your prompt: ")
    output = query_ollama(model_name, user_prompt)
    if output:
        print("\nOllama Output:")
        print(output)
