import json
import requests

def load_mcp_config(filepath="mcp.json"):
    """Loads the MCP server configuration from the JSON file."""
    try:
        with open(filepath, 'r') as f:
            config = json.load(f)
            return config.get("mcp_servers", [])
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}.")
        return []

def find_best_server(query, mcp_servers):
    """
    Analyzes the query and finds the most relevant MCP server based on keywords.
    This is a basic example; you can implement more sophisticated logic.
    """
    best_server = None
    max_keyword_matches = 0

    query_lower = query.lower()
    query_keywords = query_lower.split() # Simple keyword extraction

    for server in mcp_servers:
        matches = 0
        if "keywords" in server:
            for keyword in server["keywords"]:
                if keyword in query_keywords or keyword in query_lower:
                    matches += 1

        if matches > max_keyword_matches:
            max_keyword_matches = matches
            best_server = server

    return best_server

def forward_query(query, server_config):
    """Forwards the query to the selected MCP server and returns the response."""
    if not server_config or "host" not in server_config:
        print("Error: No suitable server found or server configuration is incomplete.")
        return None

    api_endpoint = f"{server_config['host']}/your_query_endpoint" # Define your API endpoint on MCP servers
    payload = {"query": query}

    try:
        response = requests.post(api_endpoint, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with {server_config['name']} ({server_config['host']}): {e}")
        return None

if __name__ == "__main__":
    mcp_servers = load_mcp_config()

    if not mcp_servers:
        print("No MCP servers configured. Exiting.")
    else:
        user_query = input("Enter your query: ")
        best_server = find_best_server(user_query, mcp_servers)

        if best_server:
            print(f"Forwarding query to: {best_server['name']} ({best_server['host']})")
            response = forward_query(user_query, best_server)
            if response:
                print("\nResponse from MCP Server:")
                print(response)
        else:
            print("No suitable MCP server found for your query.")
