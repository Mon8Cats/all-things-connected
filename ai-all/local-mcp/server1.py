from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/your_query_endpoint', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({"error": "Missing 'query' in request"}), 400

    # Process the query using local Ollama or other tools
    try:
        ollama_process = subprocess.run(
            ['ollama', 'run', 'llama2', query], # Example using Ollama directly
            capture_output=True,
            text=True,
            check=True
        )
        response = ollama_process.stdout.strip()
        return jsonify({"response": response})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Ollama error: {e.stderr}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True) # Example port
    
