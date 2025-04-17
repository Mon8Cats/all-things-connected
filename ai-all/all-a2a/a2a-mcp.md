# A2A and MCP

Agent - {MCP Client - MCP protocol - MCP Server - tools, resources}^n

Agent - {[A2A protocol] - Agent}^n
    how discovery of agents happens? - via configuration file
    agent_card_path="/.well-known/agent.json"

```bash
agents
    crewai/
    google_adk/
    langraph/
        __pycache__
        __init__.py
        __main__.py
        agent.py
            @tool
            internally call apis or mcp server?
        task_manager.py
common
    __pycache__
    client/
        __pycache__
        __init__.py
        card_resolver.py
            checking agent.json - it has info about agents under the agents folder (or external agents)
        client.py
    server/
    utils/
    __init__.py


run a agent (or multiple agents) and run client 

```