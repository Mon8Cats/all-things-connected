# API verbs

n the context of HTTP methods used in RESTful APIs, POST, PUT, and PATCH serve different purposes for managing resources:

POST
Purpose: Primarily used to create a new resource. It can also be used to submit data to be processed by the server.   
Idempotent: No. Multiple identical POST requests may result in multiple resources being created or multiple side effects.
Request Body: Usually contains the data for the new resource to be created. The server assigns the URI for the new resource.   
Response: Typically returns a 201 Created status code upon successful creation, often with a Location header specifying the URI of the new resource.
PUT
Purpose: Used to update an existing resource or create a new resource if the target URI does not exist. The client specifies the URI for the resource.
Idempotent: Yes. Multiple identical PUT requests should have the same effect as a single request. If the resource exists, it will be updated to the state described in the request body. If it doesn't exist, it will be created at the specified URI.
Request Body: Should contain the complete representation of the resource as it should exist at the target URI. Any properties not included in the request body might be considered for removal or set to default values by the server.
Response:
200 OK if an existing resource was successfully modified.
201 Created if a new resource was successfully created.
204 No Content if the update was successful but there is no content to return.
PATCH
Purpose: Used to apply partial modifications to a resource. Only the data that needs to be updated is sent in the request.   
Idempotent: Not necessarily. Whether a PATCH request is idempotent depends on the specific implementation and the nature of the changes being applied. For example, updating a counter is not idempotent, while updating a specific field to a fixed value could be.
Request Body: Contains a set of instructions describing how the resource should be modified. The format of these instructions can vary (e.g., JSON Patch, XML Patch).   
Response:
200 OK if the modifications were successfully applied.
204 No Content if the update was successful but there is no content to return.
Here's a table summarizing the key differences:

Feature	POST	PUT	PATCH
Primary Use	Create a new resource	Update an existing resource or create if it doesn't exist	Apply partial modifications to a resource
URI	Server assigns the URI	Client specifies the URI	Client specifies the URI
Idempotent	No	Yes	Not necessarily
Request Body	Data for the new resource	Complete representation of the resource	Instructions for partial modification
Impact	Creates a new resource (potentially multiple times)	Replaces the resource entirely at the specified URI	Modifies specific attributes of the resource

In practical terms:

Use POST when you want the server to create a new resource and assign its URI.
Use PUT when you want to update a resource at a known URI, and you are sending the complete updated representation. If the resource doesn't exist at that URI, you are instructing the server to create it there.
Use PATCH when you want to update only specific fields of a resource without affecting other parts of it. This is more efficient when you only have partial data to update.

