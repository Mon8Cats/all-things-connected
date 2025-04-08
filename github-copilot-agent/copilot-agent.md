# GitHub Copilot Agent

It's important to understand that GitHub Copilot's "Agent mode" is a relatively new and evolving feature. Therefore, access and functionality may change. Here's a breakdown of how to approach using it, based on current information:

Key Points:

VS Code Insiders:
Agent mode is currently primarily available within VS Code Insiders. This means you'll likely need to be using the Insiders build of VS Code to have access to the most up-to-date Agent mode features.
The gradual roll-out to VS Code Stable is ongoing.
Copilot Edits:
Agent mode functions within the "Copilot Edits" feature of VS Code.
To access Copilot Edits, you can use the keyboard shortcut Ctrl+Shift+Alt+I.
Mode Selection:
Within the Copilot Edits view, there should be a dropdown menu that allows you to switch between "Edit" mode and "Agent" mode.
Select "Agent" mode from this dropdown.
Prompting:
In Agent mode, you can provide higher-level prompts, and Copilot will attempt to autonomously plan and execute the necessary code changes and terminal commands.
Copilot will then show you the proposed changes, and ask for your permission before executing terminal commands.
General Steps:

Install VS Code Insiders:
If you don't already have it, download and install the VS Code Insiders build.
Open Copilot Edits:
Open your project in VS Code Insiders.
Use the keyboard shortcut Ctrl+Shift+Alt+I to open the Copilot Edits view.
Select Agent Mode:
In the Copilot Edits view, find the mode dropdown and select "Agent."
Enter Your Prompt:
Enter a clear and descriptive prompt for the task you want Copilot to perform.
Review and Confirm:
Carefully review the code changes and terminal commands that Copilot proposes.
Confirm that you want Copilot to execute the commands.
Important Notes:

Agent mode is designed for more complex, multi-step tasks.
Be aware that Agent mode may use more of your Copilot quota, as it can generate multiple requests.
Keep your VS code and github copilot extentions updated.


## mcp.json?

The mcp.json file plays a crucial role in how an MCP system discovers and utilizes servers, tools, and resources. Here's a breakdown of how it works:

1. Server Discovery:

Server Configuration:
The mcp.json file contains a "server" section, which specifies the server's connection details, including the host and port.
This information is used by MCP clients (applications that need to interact with external tools) to locate and connect to the MCP server.
Client Connection:
When an MCP client needs to access a tool or resource, it reads the mcp.json file to retrieve the server's address and port.
The client then establishes a connection to the server using these details.
2. Tool and Resource Discovery:

Tool Definitions:
The mcp.json file contains a "tools" array, which lists the tools that the server exposes.
Each tool definition includes:
name: The unique identifier of the tool.
description: A human-readable description of the tool's functionality.
parameters: A JSON schema that defines the input parameters required by the tool.
handler: The identifier of the function on the server that will handle the tool's execution.
Client Awareness:
When an MCP client connects to a server, it can read the mcp.json file to discover the available tools.
The client uses the tool definitions to:
Display the available tools to the user (if applicable).
Construct requests to invoke the tools, including the required parameters.
Validate the parameters that the user has entered, before sending them to the server.
Resource Handling:
While the json file focuses primarily on tools, the handlers that are defined in the json file are what accesses the resources.
The handlers are the code that the server executes, and these handlers are what are coded to access the data.
Therefore, the json file, is the map, of how to access the resources.
Workflow Example:

Client Application: An AI-powered IDE needs to read a file from the local file system.
MCP Configuration: The IDE reads the mcp.json file, which specifies the server's address and the readFile tool.
Server Connection: The IDE connects to the MCP server using the host and port from mcp.json.
Tool Invocation: The IDE constructs a request to invoke the readFile tool, including the filePath parameter.
Server Execution: The MCP server receives the request, executes the readFileHandler function (as specified in mcp.json), and retrieves the file's content.
Response: The server sends the file content back to the IDE.
IDE Display: The IDE displays the file content to the user.
In essence:

mcp.json acts as a central registry that enables clients to discover servers and their capabilities.
It provides a standardized way to define and describe tools, making it easier for AI applications to interact with external resources.
It is the map, that allows the client to know what tools are available, and how to use them.

## MCP

When breaking down the Model Context Protocol (MCP) and its relationship to "Model," "Context," and "Protocol," it's helpful to consider how each term contributes to the overall function of MCP:

Model:
In the MCP framework, the "model" refers to the Large Language Models (LLMs) that utilize the protocol.   
MCP is designed to enhance the capabilities of these models by providing them with access to external data and tools.   
Essentially, MCP expands the "model's" ability to interact with the world beyond its pre-trained data.   
Context:
"Context" is a core element of MCP. It signifies the external data and information that LLMs require to perform tasks effectively.   
MCP facilitates the delivery of relevant "context" to LLMs by enabling them to access data from various sources, such as databases, files, and APIs.   
By providing relevant context, MCP allows the models to give much more accurate and relevant responses.
Protocol:
The "protocol" aspect of MCP refers to the standardized set of rules and guidelines that govern how LLMs interact with external data sources.   
MCP establishes a consistent way for applications to provide context and tools to LLMs, ensuring interoperability and seamless communication.   
It is the set of rules that allow the model, to access the context.
In essence, MCP is a system that allows a "model" to access needed "context" through a defined "protocol".   

## MCP Components

When discussing the Model Context Protocol (MCP), it's important to understand the key components that enable its functionality. Here's a breakdown, focusing on the core architectural elements:

Core MCP Components:

MCP Hosts:
These are the applications that need access to external data. In essence, these are the applications that "host" the need for external information.
Their role is to initiate requests for data and then process the responses received.   
A good example of this would be an AI powered IDE, that needs to access information about code repositories.   
MCP Servers:
These are lightweight servers that provide the standardized connections to the desired data sources.   
They act as intermediaries, managing the flow of information between the hosts and the actual data.   
These servers "serve" the data, to the host, in a standardized protocol.
MCP Clients:
These are the connection managers that maintain the dedicated links to the MCP servers.   
They are the "clients" that make the requests to the servers.   
These often reside within the host application.
Data Sources:
These are the local or remote locations where the data resides. They can be databases, files, external APIs, etc.   

## Iteration

Implementing or configuring an MCP (Model Context Protocol) system to iteratively search for and utilize appropriate tools and resources until a satisfactory answer is found involves a combination of intelligent planning, execution, and feedback mechanisms. Here's a breakdown of the key elements and how they can be implemented:

- Tool and Resource Discovery and Selection:
  - mcp.json as a Knowledge Base:
    - The mcp.json file serves as a central knowledge base, defining the available tools and their capabilities.
    - The MCP system should analyze the user's query and compare it to the tool descriptions and parameter requirements in mcp.json.
  - Semantic Search and Matching:
    - Implement semantic search or natural language understanding (NLU) techniques to understand the user's intent and identify relevant tools.
    - This could involve using techniques like:
      - Word embeddings (e.g., Word2Vec, GloVe) to measure the similarity between the query and tool descriptions.
      - Language models (LLMs) to classify the query and identify the required tool functionalities.
  - Parameter Extraction:
    - Use NLU to extract relevant parameters from the user's query and map them to the tool's parameter requirements.
    - Validate the extracted parameters against the JSON schema defined in mcp.json.

- Iterative Execution and Feedback:
  - Planning and Execution:
    - The MCP system should be able to plan a sequence of tool invocations to achieve the desired result.
    - This might involve breaking down the query into smaller subtasks and identifying the tools needed for each subtask.
    - Execute the tools in the planned sequence, passing the necessary parameters.
  - Result Evaluation:
After each tool invocation, evaluate the results to determine if they are relevant to the query.
This could involve:
Checking if the results meet certain criteria (e.g., data type, range).
Using LLMs to assess the relevance and quality of the results.
Feedback Loop:
Implement a feedback loop to guide the iterative search process.
If the results are not satisfactory, the system should:
Analyze the results and identify potential issues.
Adjust the tool selection or parameter values.
Invoke additional tools to gather more information.
Ask the user for clarification, if needed.
State Management:
Maintain a state or memory of the previous tool invocations and results.
This allows the system to build upon previous information and avoid redundant operations.
LLM Orchestration:
Use LLMs to orchestrate the entire process.
The LLM can be used to:
Analyze the query.
Select the appropriate tools.
Extract parameters.
Evaluate results.
Generate new queries based on the results.
Determine when a satisfactory answer has been found.
1. Implementation Considerations:

MCP Server Enhancements:
The MCP server should be designed to support iterative execution and feedback.
This might involve adding features like:
State management.
Result caching.
Error handling and reporting.
Client-Side Logic:
The MCP client (e.g., an AI-powered IDE) will need to implement the logic for planning, execution, and feedback.
LLM Integration:
Integrate LLMs into the MCP system to enhance its intelligence and adaptability.
This could involve using LLMs for:
Query understanding.
Tool selection.
Result evaluation.
Query generation.
Error handling:
Robust error handling is crucial. The system should be able to gracefully handle tool invocation failures and unexpected results.
User Interaction:
Implement user interaction mechanisms to allow users to provide feedback and guide the search process.
By combining these techniques, you can create an MCP system that can effectively iterate through tools and resources to provide accurate and satisfying answers to user queries.
