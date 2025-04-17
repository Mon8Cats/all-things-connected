# MCP Summary

- Agentic Loops
- Structure Workflow
- Commit fitfalls
- MCP is API server, endpoint is defined as tool, resource, prompt, 
- LLM decides to call tools
- MCP server with standard input and output
- MCP server with Server-Sent Events (SSE)
- Own Agent or Clients?
- Structure
  - assets/
  - client/
    - agents/
    - utils/
    - simple_client.py
    - client.py
    - llm.py
    - agents.py
  - server/
  - tasks/

## MCP client
  
- client
  - init(self, server_url)
    - server_url, session, exit_stack
    - connect_to_sse_server(self)
      - self.__stream__context = 
      - self.__session__context = 
    - call_tools(self, tool_name, tool_input)
      - self.session.call_tool(,)
    - cleanup(self)
      - self._session_context.__aexit__() or self.__steams_context.__aexit__()
- main()
  - clinet
  - client.connect_to_sse_server()
  - response = await client.call_tools(tool_name, tool_input)
  - print
  - client.cleanup() 


or
client instance
model instance 
query instance
client_manager instance
client_manager.load_servers()
client_manager.connect_to_server()
response = client.chat.completion.create(
    model, 
    message_from_query, 
    tools=client_manager.tools,
    tool_choice="auto",
    temperature=0.0 )

results = await client.manager.process_tool_call(
    response.choices[0].message.tool_calls
)

client_manager.tools
client_manager.process_tool_call()
client_manager.cleanup()



Key Differences Summarized (for AI Agent MCP):

Feature	Session (AI Agent Context)	Stream (AI Agent Context)
Focus	The overall interaction and maintained context	The continuous flow of data (input or output)
Persistence	Lasts for the duration of the interaction	Exists within a session for a specific task/output
State	Actively manages and utilizes context	Is the result of processing context; may not inherently manage long-term state
Purpose	Enables context-aware and coherent interactions	Provides continuous feedback and handles continuous data
Multiplicity	One main session per continuous interaction	A session can involve multiple input and output streams