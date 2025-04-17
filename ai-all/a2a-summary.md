# A2A

## Agent types

- Base Agent
- LLM Agents
  - Reasoning
  - Tools
  - Transfer
- Workflow Agents
  - Sequential Agent
  - Parallel Agent
  - Loop Agent
    - name, max_iterations, sub_agents
- Custom Agents
  
## ADK Agent Core

- ADK Agent core (agent.py) <-- from 
  - cli (adk run), web ui (adk web), api server (adk api_server), api (python)
- user <---> ADK (runner, execution logic, services) <---> storage 
- runner (event processor) <--{event loop}--> execution logic (agent, llm invocation, tools,etc.)

## Structure

- Agent
  - model
  - name
  - description
  - instruction
  - sub_agent = []
  - tools = [AgentTool(agent=...), AgentTool(agent=...)]
  - before_agent_callback=
  - generate_content_config=
- AgentTool
  - agent=...
  