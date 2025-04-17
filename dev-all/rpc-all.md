# RPC (gRPC)

client -> client stub -> rpc protocol (rpc runtime)
-> network -> 
rpc protocol (rpc runtime) -> server stub -> server

- rpc handles marshalling and un-marshalling
serialization (marshalling): object -> byte stream
de-serialization (un-marshalling): byte stream -> object

- Stubs are pieces of code that act as proxies for remote procedures
- Translate local function calls into remote executions across network boundaries
  
## RPC systems use a client-server architecture 

- The client makes a request to execute a function 
- The server hosts the implementation 
- Stubs are generated on both side based on a shared contract 
- The contract is typically defined using IDL files in systems like gRPC

## Why RPCs are better than REST for internal systems

- REST: manipulating resources, statelessness, standard HTTP methods
- RPC: method-oriented, good for internal use, function level granularity, 
- protocol buffers - define precise input and output schemas 
- Json (test based) or Protobuf (binary)
- HTTP/2 provides multiplexing and header compression (for js, css, png 1 tcp connections then 3 connections)
- Interceptors for logging, authentication, retries and rate limiting



## RPC and REST

REST (Representational State Transfer) and RPC (Remote Procedure Call) are two distinct architectural styles used for designing communication between software systems, particularly for web services and APIs. Here's a breakdown of each:   

REST (Representational State Transfer)
Concept: REST is an architectural style that treats every piece of data or functionality as a resource. These resources are identified by URIs (Uniform Resource Identifiers). Clients interact with these resources using standard HTTP methods to perform actions.   

Key Characteristics:

Resource-Oriented: The core of REST is the concept of resources. Interactions revolve around manipulating these resources.   
Stateless: Each request from a client to a server contains all the information needed to understand the request. The server does not store any client context between requests. This makes RESTful services more scalable and reliable.   
Uniform Interface: REST defines a set of well-defined interfaces using standard HTTP methods (GET, POST, PUT, DELETE, etc.). This uniformity makes it easier for clients to understand and interact with the API.   
Representations: Resources can have multiple representations (e.g., JSON, XML, HTML). Clients can request the format they prefer.   
Layered System: The architecture can be composed of multiple layers (client, server, proxies, etc.), and each layer should not need to know about layers beyond the immediate one it interacts with.   
Cacheable: Responses can be cached by clients and intermediaries, improving performance.   
HATEOAS (Hypermedia as the Engine of Application State): Ideally, a RESTful API should provide links within its responses that allow clients to discover available actions and related resources dynamically. This makes the API more self-descriptive.   
How it Works:

A REST client sends a request to a specific URI using an HTTP method that indicates the desired action:   

GET: Retrieve a resource.
POST: Create a new resource.
PUT: Update an existing resource.
DELETE: Remove a resource.   
The server processes the request and sends back a response with a status code and a representation of the resource (if applicable).   

Example:

To retrieve information about a user with ID 123:

GET /users/123
To create a new user:

POST /users
Content-Type: application/json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
RPC (Remote Procedure Call)
Concept: RPC is a protocol that allows a program to execute a procedure (function, subroutine) on another computer (the server) as if it were a local procedure call. The programmer doesn't need to explicitly code the network communication details.   

Key Characteristics:

Procedure-Oriented: RPC focuses on executing specific functions or actions on the server.   
Tight Coupling: Clients often need to know the specific names and parameters of the remote procedures they want to call, leading to tighter coupling between client and server.
Stateful or Stateless: RPC can be either stateful (server maintains information about the client's session) or stateless, depending on the design.   
Variety of Protocols and Formats: RPC can use various underlying transport protocols (like TCP/IP) and data formats (like XML-RPC, JSON-RPC, gRPC's Protocol Buffers).
Explicit Operations: The operations available are explicitly defined by the server's procedures.
How it Works:

The client makes a call to a client stub (a local proxy for the remote procedure).   
The client stub marshals (packages) the procedure name and arguments into a message.   
This message is sent over the network to the server.
The server receives the message and a server stub unmarshals (unpackages) the procedure name and arguments.   
The server stub calls the actual server procedure.
The server procedure executes and its results are marshaled back into a response message by the server stub.   
The response message is sent back to the client.
The client stub unmarshals the results and returns them to the client application as if it were a local procedure call.   
Example (Conceptual):

Let's say a server has a procedure called getUserDetails that takes a userID as input. An RPC client might make a call like:

result = callRemoteProcedure("getUserDetails", 123)
The underlying RPC mechanism handles the networking and data serialization/deserialization.

Key Differences Summarized:
Feature	REST	RPC
Focus	Resources	Procedures/Actions
Interaction	Manipulating resources using HTTP verbs	Executing remote functions
Addressing	URIs	Procedure names and parameters
Coupling	Looser	Tighter
State	Stateless (required)	Stateful or Stateless
Interface	Uniform (HTTP methods)	Explicitly defined procedures
Data Format	Flexible (JSON, XML, etc.)	Varies by RPC implementation
Discoverability	HATEOAS (ideally)	Often requires separate documentation

Export to Sheets
When to Use Which:
REST: Generally preferred for public-facing web APIs, especially when dealing with standard CRUD (Create, Read, Update, Delete) operations on data. Its stateless nature and use of standard HTTP make it well-suited for scalability and interoperability on the web.   
RPC: Often used for internal communication between microservices or in systems where performance and tight control over the interface are critical. It can be more efficient for specific, action-oriented tasks that don't naturally map to CRUD operations on resources. Frameworks like gRPC are gaining popularity for their speed and support for various languages.   
Both REST and RPC have their strengths and weaknesses, and the best choice depends on the specific requirements of the system being built. In some cases, hybrid approaches might also be used.

Let's break down gRPC, Protocol Buffers (protobuf), and HTTP/2:

gRPC (gRPC Remote Procedure Calls)
What it is: gRPC is a modern, open-source, high-performance Remote Procedure Call (RPC) framework. It was initially developed by Google and is now part of the Cloud Native Computing Foundation (CNCF).   
Core Idea: gRPC allows client and server applications to communicate transparently as if they were making local function calls, even though they might be running on different machines or in different languages. It handles the underlying complexities of network communication, serialization, and deserialization.   
Key Features and Characteristics:
High Performance: gRPC is designed for speed and efficiency. It leverages Protocol Buffers for serialization, which is faster and more compact than text-based formats like JSON or XML. It also utilizes HTTP/2 for its transport protocol, enabling features like multiplexing and header compression.   
Contract-First API Design: gRPC uses Protocol Buffers as its Interface Definition Language (IDL). You define the structure of your data and the service contracts in .proto files. This contract is language-agnostic, and gRPC tooling can generate client and server code in many programming languages (e.g., Go, Java, Python, C++, C#, Node.js, Ruby). This ensures strong typing and clear API contracts.   
Language Agnostic: gRPC supports a wide range of programming languages, making it ideal for building polyglot microservice architectures.   
HTTP/2 Based: gRPC uses HTTP/2 as its transport layer. This provides several advantages over HTTP/1.1, including:
Multiplexing: Multiple requests and responses can be sent over a single TCP connection concurrently, reducing latency and improving efficiency.   
Header Compression (HPACK): HTTP headers are compressed, reducing bandwidth usage.   
Server Push: The server can proactively send data to the client that it anticipates the client will need, further improving performance.
Binary Protocol: HTTP/2 is a binary protocol, which is more efficient to parse than the text-based HTTP/1.1.   
  
Streaming: gRPC supports various streaming capabilities:
Unary RPCs: Standard request-response model.
Server Streaming RPCs: The server sends a stream of messages to the client in response to a single request.   
Client Streaming RPCs: The client sends a stream of messages to the server, which processes them and returns a single response.   
Bidirectional Streaming RPCs: Both the client and the server can send streams of messages to each other simultaneously.   
  
Built-in Features: gRPC provides built-in support for features like authentication, authorization, tracing, load balancing, and health checking.   
Code Generation: The gRPC tooling automatically generates client stubs and server skeletons from the .proto definitions, significantly simplifying development.
Protocol Buffers (protobuf)
What it is: Protocol Buffers (often shortened to protobuf) is a language-neutral, platform-neutral, extensible mechanism for serializing structured data developed by Google. Think of it as a more efficient and powerful alternative to XML or JSON for serializing data.   
Key Features and Characteristics:
Definition Language: You define the structure of your data using a simple, language-agnostic .proto file. This file describes the fields in your messages, their types, and their unique identifiers.   
Code Generation: The protoc compiler (protobuf compiler) can generate source code in various programming languages (C++, Java, Python, Go, C#, etc.) from your .proto definitions. This generated code provides efficient methods for serializing and deserializing your data.   
Binary Serialization: Protobuf serializes data into a compact binary format, which is typically much smaller and faster to parse than text-based formats like JSON or XML. This reduces network bandwidth usage and improves performance.   
Extensibility and Backward/Forward Compatibility: You can evolve your data structures over time by adding new fields without breaking existing code that uses older versions of the data. Fields have unique identifiers, so even if the order or presence of fields changes, the data can still be interpreted correctly.   
Strongly Typed: The generated code provides strong typing for your data structures, reducing the chances of runtime errors.   
Not Self-Describing: Unlike JSON or XML, the binary format of protobuf is not self-describing. To interpret a protobuf message, you need the .proto definition.   
HTTP/2
What it is: HTTP/2 is a major revision of the HTTP network protocol used by the World Wide Web. It was derived from Google's earlier experimental SPDY protocol and standardized by the Internet Engineering Task Force (IETF).   
Primary Goals: The primary goals of HTTP/2 are to reduce latency and improve web performance by addressing the limitations of HTTP/1.1.   
Key Features and Characteristics:
Binary Protocol: Unlike HTTP/1.1, which is text-based, HTTP/2 is a binary protocol. Binary protocols are more efficient to parse and less error-prone.   
Multiplexing: This is a key feature. HTTP/2 allows multiple requests and responses to be sent over a single TCP connection concurrently. This eliminates the "head-of-line blocking" problem in HTTP/1.1, where a slow or blocked request could delay all subsequent requests on the same connection.   
Header Compression (HPACK): HTTP/2 uses a header compression algorithm called HPACK, which significantly reduces the size of HTTP headers transmitted between the client and server. Headers can be repetitive in a series of requests, and HPACK eliminates this redundancy.   
Server Push: HTTP/2 allows the server to proactively send resources to the client (e.g., CSS, JavaScript) that it anticipates the client will need for subsequent requests, without the client explicitly asking for them. This can improve page load times.   
Stream Prioritization: HTTP/2 allows clients to prioritize the importance of different requests. This enables the server to send the most important data first, improving the perceived performance of web pages.   
Single TCP Connection: HTTP/2 aims to use a single TCP connection between the client and the server for all communication, reducing the overhead of establishing multiple connections.   
In the context of gRPC:

gRPC leverages the strengths of both Protocol Buffers and HTTP/2 to provide a robust and efficient RPC framework:   

Protocol Buffers act as the interface definition language and the data serialization format, ensuring efficient data exchange and clear API contracts.   
HTTP/2 serves as the transport protocol, providing features like multiplexing for concurrent requests, header compression for reduced overhead, and server push (though less commonly used directly by gRPC applications) for potential performance benefits.   
This combination makes gRPC a powerful choice for building high-performance, scalable, and language-interoperable microservices and distributed applications.


Okay, here are some examples illustrating how Protocol Buffers (protobuf) are used to define data structures and the kind of code they generate:

1. A Simple Person Message:

.proto file (person.proto):

Protocol Buffers

syntax = "proto3";

message Person {
  string name = 1;
  int32 id = 2;
  string email = 3;
}
Explanation:

syntax = "proto3";: Specifies the protobuf version being used.
message Person { ... }: Defines a message type named Person. Messages are the basic unit of data in protobuf.
string name = 1;: Defines a field named name of type string. The = 1 assigns a unique field number. These numbers are used in the binary encoding and should not be changed once in use.
int32 id = 2;: Defines a field named id of type 32-bit integer.
string email = 3;: Defines a field named email of type string.
Generated Code (Example in Python):

After compiling person.proto with the protoc compiler, you would get a Python file (e.g., person_pb2.py). This file would contain a class Person with methods for:

Python

class Person(message.Message):
  __slots__ = ("name", "id", "email")
  NAME_FIELD_NUMBER = 1
  name = proto.pydot_ng.messages.StringField(1, descriptor_pool=_DESCRIPTOR)
  ID_FIELD_NUMBER = 2
  id = proto.pydot_ng.messages.Int32Field(2, descriptor_pool=_DESCRIPTOR)
  EMAIL_FIELD_NUMBER = 3
  email = proto.pydot_ng.messages.StringField(3, descriptor_pool=_DESCRIPTOR)
  -- # ... other methods for serialization, deserialization, etc.
Usage in Python:

Python

import person_pb2

-- # Create a Person object
person = person_pb2.Person()
person.name = "Alice"
person.id = 123
person.email = "alice@example.com"

-- # Serialize the object to a binary string
serialized_data = person.SerializeToString()
print(f"Serialized data: {serialized_data}")

-- # Deserialize the binary string back to a Person object
new_person = person_pb2.Person()
new_person.ParseFromString(serialized_data)
print(f"Name: {new_person.name}, ID: {new_person.id}, Email: {new_person.email}")
2. Message with Nested Types and Enums:

.proto file (contact.proto):

Protocol Buffers

syntax = "proto3";

message ContactInfo {
  enum PhoneType {
    MOBILE = 0;
    HOME = 1;
    WORK = 2;
  }

  message PhoneNumber {
    string number = 1;
    PhoneType type = 2;
  }

  string name = 1;
  repeated PhoneNumber phones = 2; // 'repeated' means it's a list
}
Explanation:

enum PhoneType { ... }: Defines an enumeration with possible phone types.
message PhoneNumber { ... }: Defines a nested message type PhoneNumber within ContactInfo.
repeated PhoneNumber phones = 2;: Defines a field named phones which is a list (repeated field) of PhoneNumber messages.
Generated Code (Conceptual - will vary by language):

The generated code would include classes for ContactInfo, PhoneNumber, and the PhoneType enum. You would be able to create lists of PhoneNumber objects within a ContactInfo object.

Usage (Conceptual Python):

Python

import contact_pb2

contact = contact_pb2.ContactInfo()
contact.name = "Bob"

mobile_phone = contact.phones.add()
mobile_phone.number = "123-456-7890"
mobile_phone.type = contact_pb2.ContactInfo.MOBILE

work_phone = contact.phones.add()
work_phone.number = "987-654-3210"
work_phone.type = contact_pb2.ContactInfo.WORK

-- # Serialize and deserialize as before
serialized_contact = contact.SerializeToString()
new_contact = contact_pb2.ContactInfo()
new_contact.ParseFromString(serialized_contact)

print(f"Contact Name: {new_contact.name}")
for phone in new_contact.phones:
  print(f"  Number: {phone.number}, Type: {contact_pb2.ContactInfo.PhoneType.Name(phone.type)}")
3. Message with Optional Fields (Proto3):

In Proto3, all fields are implicitly optional. You can still explicitly mark them with optional for clarity or when transitioning from Proto2.

.proto file (product.proto):

Protocol Buffers

syntax = "proto3";

message Product {
  string name = 1;
  int32 product_id = 2;
  optional string description = 3; // Explicitly marked as optional
  float price = 4;
}
Explanation:

optional string description = 3;: The description field is optional. If it's not set when creating a Product object, it will have a default value (empty string for strings).
4. Using oneof for Exclusive Fields:

The oneof keyword allows you to define a set of fields where only one of them can be set at a time.

.proto file (payload.proto):

Protocol Buffers

syntax = "proto3";

message Payload {
  int32 request_id = 1;
  oneof data {
    string message = 2;
    int32 value = 3;
    bytes raw_data = 4;
  }
}
Explanation:

oneof data { ... }: Defines a oneof field named data. Only one of message, value, or raw_data can be set in a Payload object. If you set one, the others will be automatically unset.
Generated Code (Conceptual):

The generated code will likely have methods to check which field in the oneof is set.

Usage (Conceptual Python):

Python

import payload_pb2

payload1 = payload_pb2.Payload()
payload1.request_id = 100
payload1.message = "Hello!"

payload2 = payload_pb2.Payload()
payload2.request_id = 200
payload2.value = 42

-- # Only one of payload1.message, payload1.value, payload1.raw_data will be set
print(f"Payload 1 message: {payload1.message}")
print(f"Payload 2 value: {payload2.value}")
These examples demonstrate the basic syntax and features of Protocol Buffers for defining structured data. The protoc compiler then takes these .proto files and generates efficient code in your chosen programming language to work with this data for serialization, deserialization, and data access. This makes it a powerful tool for data interchange, especially in high-performance and cross-language applications like those built with gRPC.

