# All A2A

## Resources

- https://github.com/google/A2A
  

## Overview

- Agent
  - {A2A protocol} -> Agent(s)
  - MCP client -> {model context protocol} -> MCP server(s) (tools, resources)

## Agent 

```bash
from google.adk.agents import LlmAgent
from google.adk.tools import google_Search
dice_agent = LlmAgent(
    model="gemini-2.0-flash-exp", # required
    name="question_answer_agent", # required: unique name
    description="A helpful assistant agent that can answer questions", 
    instruction="""Respond to the query using google search""",
    tools=[google_search], # provide an instance of the tool
)

root_agent = Agent(
    name="weather_agent_v2",
    model="gemini-2.0-flash-exp",
    description="You are the main Weather Agent, coordinating a test",
    tools=[get_weather],
    sub_agents=[greeting_agent, farewell_agent]
)


def get_weather(city: str) -> Dict:
    # best practice
    city_normalized = city.lower().replace(" ", "")
    # mock weather data
    mock_weather_db = { 
        "austin": {"status":"success", "report":"the weather in ..."}
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status":"error", "error_message":"sorry, I don't have"}


```

## Delegation

Instruction and description field: the LLM relies heavily on these for understanding roles and making delegation decisions using auto delegations for sub agents.

How agent delegation works: The default agent behavior to allow delegation. When processing a user message, the LLM considers the query, the current agent's description, and the description fields of related agents.

If the LLM determines another agent is a better fit based on its description, it initiates a transfer. Clear, distinct descriptions are vital! The LLM uses them to route tasks effectively. 

## MCP vs A2A

Is an agent maybe also a tool? no
When an agent's functionality is distilled into a single, well-bounded operation with clear inputs and outputs (typically via an MCP endpoint), it servers as a tool.

When it goes beyond that - by maintaining context, initiating multi-turn conversations, and making independent decisions - it is operating in its full agent capacity.

An agent can be designed to server dual roles using MCP - it can operate as an MCP client to request services from external MCP servers and simultaneously function as an MCP host by exposing its own internal tools or data through MCP endpoints.

In addition, it can use the A2A protocol to communicate with other agents across different ecosystems (LangChain, Crew.ai, etc). This multi-layered approach allows an agent to both consume and provide functionalities while also engaging in broader inter-agent dialogues. 


## MCP Agent, Client, Server

Here's a concise summary of MCP Agent, Client, and Server:

- MCP Agent: The AI application that wants to use external resources (tools, data). It orchestrates tasks and uses one or more MCP Clients to connect to Servers. Think of it as the intelligent user.
- MCP Client: A component within the MCP Agent that manages the connection and communication with a specific MCP Server. It handles the technical details of sending requests and receiving responses. Think of it as a dedicated connector for one resource.
- MCP Server: An external resource that provides capabilities (tools, data, prompts) to MCP Agents. It listens for requests from MCP Clients, executes them, and sends back responses. Think of it as the provider of specific functionalities.

In short: The Agent (AI) uses a Client (connector) to interact with a Server (resource provider).

## A2A Protocol 

It is built upon widely adopted web standards, including HTTP for transport, JSON-RPC for message exchange, and Server-Sent Events (SSE) for real-time streaming fo long-running tasks.

A key component of A2A is the "Agent Card", a JSON file that agents host at a well-known URL to advertise their capabilities and connection details, enabling dynamic discovery by other agents.

initiate tasks, exchange messages (parts), track progress
streaming via SSE
push notifications to client-provided webhooks

Agent: <--{mcp}--> APIs, Applications
    local agents:
    vertex AI
    ADK

Agent: <--{mcp}--> APIs, Applications
    local agents:
    LLM
    Agent Framework

Agent <--{a2a protocol}--> Agent

## Conceptual Overview

- Agent Card: /.well-known/agent.json
  - capabilities, skills, endpoint URL, authentication requirements, used for discovery
- A2A server:
  - exposing an HTTP endpoint with A2A protocol methods
  - receives requests and manages task execution
- A2A client:
  - an application or another agent that consumes A2A services.
  - it sends requests (task/send) to and A2A server's URL.
- Task:
  - the cental unit of work
  - a client initiates a task by sending a message.
  - Tasks have unique IDs and process through states.
- Message:
  - represents communication turns between the client and the agent.
  - Messages contain parts.
- Part:
  - the fundamental content unit within a message or artifact.
- Artifact:
  - represents outputs generated by the agent during a task.
  - Artifacts also contain parts.
- Streaming:
  - for long-running tasks.
  - the client receives server-sent events (SSE)
- Push Notification:
  - servers supporting push notifications can proactively send task updates to a client-provided webhook url.

## Typical Flow

- Discovery : well-known url
  - client fetches the Agent Card form the server's well-known URL.
- Initiation : tasks/send, tasks/sendSubscribe
  - client sends a task/send request containing the initial user message and a unique task ID.
- Processing : streaming or non-streaming
  - server sends SSE events as the task progress
  - server processes the task and returns the final task object in the response.
- Interaction (optional) : input-required
  - the client sends subsequent messages using the same task ID via task/send
- Completion:
  - task eventually reaches a terminal state

## Google AI Studio?
