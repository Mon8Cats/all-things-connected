# Agent Development Kit

## Quick Start

1. Setup Environment and Install ADK
   1. python -m venv .venv
   2. source .venv/bin/activate or .venv/Scripts/activate.bat
   3. pip install google-adk
2. Create Agent Project
   1. mkdir multi_tool_agent
   2. cd multi_tool_agent
   3. echo "from . import agent" > __init__.py 
   4. touch agent.py
   5. add code into agent.py 
   6. touch .env 
   7. add API keys into .env file 
3. Setup the model
   1. Get an API key from Google AI Studio
   2. add key to .env file
4. Run my Agent
   1. adk web (or adk run multi_tool_agent)
   2. exit: cmd/ctl+c
   

## Streaming Quick Start

1. Setup Environment and Install ADK
2. Project Structure
   1. adk-streaming/app/[.env, google_search_agent/[__init.py, agent.py]]
   2. agent.py
      1. root_agent = Agent(name="unique-name", model="llm model", 
         1. description="aaa", instruction="aaa" # these are used to find agent?
         2. tools=[google_search, other_tool]) # a list of tools
   3. __init__.py
      1. from . import agent
3. Setup Gemini API key
   1. Get an API key from Google AI Studio
   2. add the key into .env file
4. Try the agent with adk web
   1. cd app
   2. adk web
5. Building a Custom Streaming App
   1. adk-streaming/app/[main.py, static/[index.htm]]
   2. main.py
   3. index.htm
6. INteract with my Streaming app
   1. goto adk-streaming/app
   2. uvicorn main:app --reload

## Agent Team: A Progressive Weather Bot with ADK
