# Networking in Google Cloud and GKE

## Google Cloud Networking Fundamentals

- Virtual Private Cloud (VPC):
  - The foundation of networking in Google Cloud. A VPC network is a globally scalable, virtual network that provides private IP address space for your resources.
  - It allows you to create isolated network environments, define subnets, and control traffic flow.
- Subnets:
  - Subdivisions of a VPC network. They define IP address ranges and are associated with specific regions.
  - Resources within a subnet can communicate with each other using private IP addresses.
- Firewall Rules:
  - Control inbound and outbound traffic to and from VM instances and other resources within a VPC network.
  - They define rules based on IP addresses, ports, and protocols.
- Routes:
  - Determine the path that network traffic takes to reach its destination.
  - Routing tables direct traffic within the VPC network and to external networks.
- Cloud NAT:
  - Provides outbound internet connectivity to resources without external IP addresses.
- Cloud DNS:
  - A scalable and reliable managed DNS service for managing domain names and private DNS zones.
- VPC Peering:
  - Allows you to connect two VPC networks, enabling private IP address communication between resources in those networks.
- Cloud VPN/Interconnect:
  - Enable secure connectivity between your on-premises network and your VPC network.

## GKE Networking

- GKE builds upon Google Cloud's VPC networking to provide Kubernetes-specific networking capabilities.
- Inside a GKE Cluster (Pod-to-Pod, Pod-to-Service):
  - VPC Subnet:
    - The GKE cluster resides within a VPC subnet, providing the underlying IP address space.
  - CNI Plugin (e.g., Calico, Cilium):
    - Provides pod networking and implements Network Policies.
    - Handles pod IP address allocation and routing within the cluster.
  - Kubernetes Services:
    - Provide stable IP addresses and DNS names for sets of pods.
    - kube-proxy or similar service mesh components manage service traffic routing.
  - CoreDNS:
    - Provides cluster-internal DNS resolution, allowing pods to discover services by name.
  - Network Policies:
    - Control pod-to-pod and pod-to-service traffic based on labels and namespaces.
    - iptables rules implemented by the CNI plugin enforce the network policies.
- Between Different GKE Clusters:
  - VPC Peering:
    - Connects the VPC networks of the two clusters, enabling private IP address communication.
  - Service Mesh (e.g., Istio):
    - Provides advanced traffic management, security, and observability across clusters.
  - Shared VPC:
    -Allows multiple GKE clusters to reside within the same VPC network.
- A GKE Cluster and Non-Cluster Resources (e.g., Cloud SQL, Compute Engine):
  - VPC Network:
    - The GKE cluster and non-cluster resources reside within the same VPC network, allowing private IP address communication.
  - Private Services Access:
    - Allows GKE to access managed services like Cloud SQL using private IP addresses.
  - Internal Load Balancers:
    - Used to expose services running in GKE to other resources within the VPC network.
- Access To/From Outside (Internet, On-Premises, Different Networks):
  - External Load Balancers:
    - Expose services running in GKE to the internet.
    - They provide public IP addresses and distribute traffic across pods.
  - Cloud NAT:
    - Provides outbound internet access for pods without external IP addresses.
  - Cloud DNS:
    - Manages domain name resolution for services exposed to the internet.
  - Cloud VPN/Interconnect:
    - Provides secure connectivity between the GKE cluster's VPC network and on-premises networks.
  - Firewall Rules:
    - Control inbound and outbound traffic to and from the GKE cluster's nodes.
  - VPC Peering:
    - Allows communication with other VPC networks, including those in different Google Cloud projects.
  - Ingress:
    - Manages external access to services within the cluster, often used in conjunction with load balancers.
- Key Points:
  - GKE networking is deeply integrated with Google Cloud's VPC networking.
  - Kubernetes-specific components like CNI plugins and CoreDNS provide pod-level networking.
  - Google Cloud services like Cloud NAT and Cloud DNS extend GKE's connectivity to external networks.
  - Firewall rules are critical for security at the VM level.
  - Routing tables determine the network path of packets.
  
## Communication between the control plane and worker nodes

- API Server Communication (Nodes to Control Plane):
  - Worker nodes need to communicate with the control plane's API server to:
    - Register themselves with the cluster.
    - Report their status and health.
    - Receive instructions for running pods.
    - Update the API server with pod status changes.
  - This communication is primarily initiated by the kubelet process running on each node.
  - The kubelet establishes a secure connection to the API server, typically using TLS.
  - This communication flows from the worker nodes to the control plane.   
- Control Plane to Nodes (API Server to Kubelet):
  - The control plane needs to communicate with the kubelet on worker nodes to:
    - Schedule pods onto nodes.   
    - Instruct nodes to start, stop, or update pods.   
    - Retrieve node and pod status information.
  - This communication is also primarily handled through the API server.
  - The API server initiates connections to the kubelet on worker nodes.
  - This communication flows from the control plane to the worker nodes.
  - The communication is secured by TLS.
- Network Communication:
  - Underlying network connectivity is essential for the control plane and worker nodes to communicate.
  - This communication occurs within the VPC network where the GKE cluster is deployed.
  - Firewall rules are configured to allow necessary traffic between the control plane and worker nodes. - The control plane and the nodes are within the same VPC, allowing private IP communication.
- Security:
  - TLS Encryption:
    - All communication between the control plane and worker nodes is secured using TLS encryption. This ensures that data is protected from eavesdropping and tampering.
  - Authentication and Authorization:
    - Kubernetes uses authentication and authorization mechanisms to control access to the API server.   
    - Worker nodes authenticate themselves to the API server using certificates.
    - Role-Based Access Control (RBAC) is used to control what actions worker nodes are authorized to perform.   
- Key Components Involved:
  - API Server:
    - The central component of the control plane.
    - Handles all API requests from worker nodes and other clients.   
  - Kubelet:
    - An agent that runs on each worker node.   
    - Communicates with the API server and manages pods on the node.   
  - VPC Network:
    - Provides the underlying network infrastructure for communication.
  - Firewall Rules:
    - Control network traffic between the control plane and worker nodes.   
- In summary:
  - The communication between the GKE control plane and worker nodes is a secure and essential process that enables the cluster to function correctly. 
  - The API server acts as the central communication hub, and the kubelet acts as the agent on each node. 
  - The underlying VPC network and security mechanisms ensure reliable and secure communication.

## VPC networks

- It's a common misconception that the control plane and worker nodes reside within the exact same user-managed VPC network. Here's the accurate breakdown:
- The Control Plane's Location:
  - Google-Managed VPC:
    - In a GKE private cluster, the control plane is hosted in a Google-managed VPC network. This is separate from your own user-managed VPC network where your worker nodes reside.   
    - This is a security measure to isolate the control plane and ensure its stability.
- Communication and VPC Peering:
  - VPC Peering Is Essential:
    - To enable communication between your worker nodes in your VPC and the control plane in Google's managed VPC, GKE automatically establishes a VPC peering connection.
    - This peering connection allows private IP address communication between the two VPC networks.   
  - How It Works:
    - When you create a private GKE cluster, Google Cloud automatically sets up a VPC peering connection between your VPC and the Google-managed VPC that hosts the control plane.
    - This peering connection is managed by Google Cloud, so you don't need to manually configure it.
    - This peering connection is what enables the worker nodes to communicate with the control plane's internal IP addresses.
- Why This Architecture?
  - Enhanced Security:
    - Isolating the control plane in a Google-managed VPC enhances security by reducing the attack surface.   
  - Control Plane Stability:
    - It also helps ensure the stability and reliability of the control plane by separating it from user-managed resources.
  - Managed Service:
    - This allows google to manage the control plane, and provide a managed kubernetes service.
- In summary:
  - Worker nodes and the control plane in a GKE private cluster reside in different VPC networks.
  - A Google-managed VPC peering connection facilitates private IP address communication between them.
  - Therefore, yes, VPC peering is absolutely necessary for the communication between worker nodes and the control plane in a private GKE cluster.
  
## IP Masquerading 

- An IP masquerade agent, often referred to simply as IP masquerading, is a network address translation (NAT) technique that allows multiple devices on a private network to share a single public IP address when communicating with the internet or other external networks.
- How it Works:
  - Private Network:
    - Devices on a private network (e.g., your home or office network) typically use private IP addresses (e.g., 192.168.x.x, 10.x.x.x, 172.16.x.x).
  - Public IP Address:
    - When a device on the private network needs to communicate with a device on the internet, it sends a request.
  - Masquerading:
    - The IP masquerade agent (usually a router or firewall) intercepts the request.
    - It replaces the private source IP address of the request with its own public IP address.
    - It also changes the source port number to keep track of the different connections.
    - It then forwards the request to the destination on the internet.
  - Response:
    - When the destination device responds, it sends the response to the public IP address of the masquerade agent.
  - Demasquerading:
    - The masquerade agent receives the response.
    - It uses the port number to determine which device on the private network initiated the request.
    - It replaces the destination IP address (its own public IP) with the private IP address of the originating device.
    - It then forwards the response to the device on the private network.
- Key Functions:
  - Sharing a Single IP:
    - Allows multiple devices to share a single public IP address, conserving public IP addresses.
  - Security:
    - Provides a basic level of security by hiding the private IP addresses of devices on the network.   
  - Network Address Translation (NAT):
    - It is a form of Network Address Translation.
- In GKE Context:
  - When a GKE node needs to connect to the internet, but only has an internal IP address, cloud NAT acts as an IP masquerade agent.   
  - Also, within the GKE nodes, there are iptable rules that perform IP masquerading for pod traffic. This allows pods that have internal only IP addresses to connect to external resources.
- Essentially:
  - An IP masquerade agent acts as a translator, allowing devices on a private network to communicate with the outside world using a shared public IP address.

## Expose Services

In Google Kubernetes Engine (GKE), you can expose your services to external traffic (internet) or internal traffic (within your VPC) using several methods, each with its own characteristics and use cases. Here's a breakdown:

- LoadBalancer Service:
  - How it Works:
    - When you create a Kubernetes Service of type LoadBalancer, GKE provisions an external (or internal) load balancer in Google Cloud.
    - For external load balancers, a public IP address is assigned.   
    - For internal load balancers, an internal IP address is assigned within your VPC.
    - Traffic coming to that IP address is then forwarded to the pods backing your service.   
  - Use Cases:
    - Directly exposing a single service to the internet or within the VPC.
    - Simple and straightforward for basic load balancing.
  - Pros:
    - Easy to implement.
    - Automatically provisions and manages load balancers.   
  - Cons:
    - Each LoadBalancer service gets its own external IP, which can be costly at scale.
    - Limited routing capabilities compared to Ingress or Gateway API.
- Ingress Object:
  - How it Works:
    - An Ingress object defines rules for routing external traffic to different services within your cluster.   
    - It typically works in conjunction with an Ingress controller (e.g., GKE Ingress controller, Nginx Ingress controller).
    - The Ingress controller manages the actual load balancing and routing based on the rules defined in the Ingress object.   
    - Ingress allows for host-based and path-based routing.   
  - Use Cases:
    - Exposing multiple services behind a single external IP address.
    - Host-based and path-based routing.   
    - SSL termination.
  - Pros:
    - Conserves external IP addresses.
    - Provides flexible routing capabilities.   
    - Supports SSL termination.   
  - Cons:
    - Requires an Ingress controller.   
    - Configuration can be more complex than LoadBalancer services.
- Gateway API:
  - How it Works:
    - Gateway API is a newer, more flexible, and extensible API for managing external access to services.   
    - It is designed to be a successor to Ingress.   
    - It introduces concepts like GatewayClasses, Gateways, and Routes, which provide more granular control over routing and traffic management.   
    - Gateway API is implemented by Gateway controllers.   
  - Use Cases:
    - Advanced traffic management, including HTTP routing, TCP/UDP routing, and TLS routing.   
    - Multi-tenant environments.
    - Extensible and customizable routing.
  - Pros:
    - More expressive and flexible than Ingress.
    - Supports advanced routing scenarios.   
    - Role-oriented design.
  - Cons:
    - Relatively new, so adoption is still growing.
    - Requires a Gateway API controller.
    - Configuration can be more complex.
- Key Considerations:
  - External vs. Internal:
    - Choose between external (internet-facing) and internal (VPC-only) load balancing based on your requirements.
  - Security:
    - Implement appropriate security measures, such as SSL/TLS encryption and firewall rules.   
  - Cost:
    - Be mindful of the cost implications of external IP addresses and load balancers.
  - Complexity:
    -Choose the method that best balances your needs with the complexity of configuration and management.
- In summary:
  - For simple service exposure, LoadBalancer services are a good choice.
  - Ingress is a great option for exposing multiple services with flexible routing.   
  - Gateway API is the future of service exposure, offering the most advanced features and extensibility.

## Load Balancer, IPtable, NEG

- Let's break down these essential components of network traffic management and load balancing:
- Load Balancer:
  - Purpose:
    - A load balancer distributes network traffic across multiple backend servers (instances, pods, etc.) to improve application availability, scalability, and performance.   
    - It prevents any single server from becoming overloaded.   
  - Types:
    - External Load Balancer: Distributes traffic from the internet to your backend servers.   
    - Internal Load Balancer: Distributes traffic within your VPC network.   
    - HTTP(S) Load Balancer: Handles HTTP and HTTPS traffic, providing advanced features like SSL termination and content-based routing.
    - Network Load Balancer: Handles TCP/UDP traffic, providing high-performance load balancing at Layer - TCP/UDP Internal Load Balancer: Distributes TCP/UDP traffic within your VPC.   
  - Key Functions:
    - Traffic distribution.
    - Health checks (to ensure traffic is sent to healthy backends).
    - SSL termination (for HTTPS load balancers).   
    - Session persistence (to maintain user sessions).   
- Instance Group:
  - Purpose:
    - An instance group is a collection of virtual machine (VM) instances that are managed as a single entity.   
    - It simplifies the deployment, scaling, and management of applications running on VMs.
  - Types:
    - Managed Instance Group (MIG): Automatically scales and manages instances based on defined policies.   
    - Unmanaged Instance Group: A group of existing instances that you manage manually.   
  - Key Functions:
    - Scaling (automatic or manual).   
    - Health checking.
    - Rolling updates.
    - Integration with load balancers (MIGs can be used as backend services for load balancers).   

- iptables:
  - Purpose:
    - iptables is a user-space utility that allows system administrators to configure the Linux kernel's netfilter firewall.   
    - It's used to define rules that control network traffic, including packet filtering, network address translation (NAT), and port forwarding.   
  - Key Concepts:
    - Tables: Organize rules into different categories (e.g., filter, nat, mangle).
    - Chains: Sequences of rules within tables.
    - Rules: Define matching criteria and actions (e.g., ACCEPT, DROP, REJECT).
  - Key Functions:
    - Packet filtering.
    - NAT (including IP masquerading).
    - Port forwarding.
    - Used in GKE nodes to implement network policies, and to perform NAT for pods.
- Network Endpoint Group (NEG):
  - Purpose:
    - A NEG is a group of backend endpoints that can be used as backend services for load balancers.   
    - It provides more granular control over backend endpoints compared to instance groups.
  - Types:
    - Zonal NEG: Contains endpoints within a single zone (e.g., VM instances, container endpoints).
    - Serverless NEG: Contains serverless endpoints (e.g., Cloud Functions, Cloud Run).
    - Internet NEG: contains internet based endpoints.   
    - Private Service Connect NEG: contains private service connect endpoints.   
  - Key Functions:
    - Flexible backend endpoint management.
    - Container-native load balancing (using container NEGs).   
    - Serverless load balancing.
    - Allows loadbalancing directly to pods in GKE.
  - GKE context:
    -Container NEGs are very useful for loadbalancing directly to pods, and bypassing the kube-proxy service.   
- In summary:
  - Load balancers distribute traffic.   
  - Instance groups manage VM instances.   
  - Iptables filters and manipulates network traffic.   
  - NEGs provide granular control over backend endpoints.   
  

## BGP (Border Gateway Protocol) Session


BGP (Border Gateway Protocol) sessions and dynamic advertisements are fundamental concepts in how the internet routes traffic. Here's a breakdown:   

BGP Sessions:

What They Are:
BGP is a path-vector routing protocol used to exchange routing information between autonomous systems (AS). An AS is a large network or group of networks under a single administrative domain (e.g., an internet service provider or a large corporation).   
A BGP session is a TCP connection between two BGP routers (called "peers"). These sessions are used to exchange routing information.   
How They Work:
BGP peers establish a TCP connection (port 179).   
They exchange BGP messages to establish and maintain the session.
They exchange routing information (prefixes and attributes) to build routing tables.   
BGP sessions can be:
EBGP (External BGP): Between routers in different ASes. This is how ISPs exchange routing information across the internet.   
IBGP (Internal BGP): Between routers within the same AS. This is used to distribute routing information within a large network.   
Key Aspects:
BGP sessions are reliable because they use TCP.   
BGP sessions are long-lived, meaning they stay up for extended periods.
Dynamic Advertisements (BGP Updates):

What They Are:
BGP routers advertise network prefixes (IP addresses and subnet masks) to their peers. These advertisements are called "BGP updates."   
These updates are "dynamic" because they change as network conditions change.
How They Work:
When a BGP router learns about a new network prefix or a change in an existing prefix, it sends an update message to its peers.   
The update message includes the prefix and attributes that describe the path to reach that prefix.   
BGP attributes include:
AS_PATH: A list of ASes that the prefix has traversed. This is used to prevent routing loops and to select the best path.
NEXT_HOP: The IP address of the next router in the path.
LOCAL_PREF: Used within an AS to select the best path.
MED (Multi-Exit Discriminator): Used between ASes to influence path selection.
BGP routers use the information in update messages to build their routing tables.   
When a BGP router receives a packet, it uses its routing table to determine the best path to the destination.
Key Aspects:
BGP updates are used to distribute routing information across the internet.
BGP updates allow the internet to adapt to changing network conditions.
BGP updates are the mechanism that enables the internet to be so resilient.
In essence:

BGP sessions are the communication channels between BGP routers.   
Dynamic advertisements (BGP updates) are the messages that carry routing information over those channels.   
Together, they allow the internet to route traffic efficiently and reliably.

Sources and related content

### Subnet is an IP segment in VPC

A single Google Cloud VPC can span multiple regions without communicating across the public internet.
Shared VPC, Cloud Router, Firewall Rules, VPC peering, Cloud VPN.
Dynamically advertising routes across the VPC.

In Google Cloud Platform (GCP), "advertising routes across the VPC" refers to the process of making your Virtual Private Cloud (VPC) network's subnets and custom routes known to other networks, either within GCP or external to it. This allows traffic to flow between those networks and your VPC.   

Here's a breakdown of what that means:

1. VPC Networks and Routes:

VPC Networks:
A VPC network is a global, virtual network that provides isolated networking functionality within GCP.   
It consists of subnets, which are IP address ranges within the VPC.   
Routes:
Routes define how traffic is directed within your VPC and to destinations outside of it.
GCP automatically creates some default routes, and you can also create custom routes.   
2. Advertising Routes:

Sharing Routing Information:
"Advertising routes" essentially means making your VPC's routing information available to other networks.
This allows those networks to know how to reach the IP address ranges within your VPC.
Scenarios:
VPC Peering:
When you peer two VPC networks, you can configure them to exchange routes.
This allows resources in one VPC to communicate with resources in the other VPC.   
You control which subnets are advertised during the peering process.   
Cloud VPN and Cloud Interconnect:
When you connect your on-premises network to your VPC using Cloud VPN or Cloud Interconnect, you can advertise routes from your VPC to your on-premises network.
This allows traffic from your on-premises network to reach resources in your VPC.   
Conversely, you also recieve route advertisements from your on premise network.
Router Advertisements:
Cloud Routers are used to dynamically exchange routes with on-premise networks, or with other VPC networks.   
They use BGP to advertise and receive routes.   
Dynamic Routing:
Advertising routes often involves dynamic routing protocols like BGP.
This allows routes to be automatically updated as network conditions change.   
3. Why It's Important:

Connectivity:
Advertising routes is essential for establishing connectivity between different networks.
Without it, traffic wouldn't know how to reach its destination.
Hybrid Networking:
It's crucial for hybrid networking scenarios, where you connect your on-premises network to your cloud environment.
Inter-VPC Communication:
It enables seamless communication between different VPC networks.
In essence:

Advertising routes across your VPC in GCP is about making your VPC's network topology 
known to other networks, enabling traffic to flow between them. 
It's a fundamental aspect of network connectivity and is essential for 
both cloud-only and hybrid deployments.



## Networking

Networking is the backbone of any cloud infrastructure. 

- Private IP and Public IP
  - Whenever we create a GCE VM instance in Google Cloud it will be created with 1 Public IP and 1 Private IP by default ( Unless we opt to use only internal IP).
  - The public IP address that is visible to the public and is used for communication between devices on different networks. 
- VPC ( Virtual Private Cloud)
  - With VPC, you can create and control your own private IP space, subnets, and routing tables within Google Cloud. You can also create firewall rules to control incoming and outgoing traffic to and from your VPC.
- Subnet
  - Subnets are used to segment a VPC into smaller networks for better organization and management of resources.
- CIDR
  - Classless Inter-Domain Routing (CIDR) is a range of IP addresses a network uses.
  - 192.0.2.0/24 — (32–24= 8) → 2⁸ = 256 IP addresses
- Firewalls
  - VPC firewall rules let you allow or deny traffic to or from virtual machine (VM) instances in a VPC network based on port number, tag, or protocol.
- Identity-Aware Proxy
  - IAP in Google Cloud provides a way to secure access to your applications and resources based on identity. 
  - Enable Cloud Identity Aware Proxy API
  - Assign roles/iap.tunnelResourceAccessor role to the user
  - Create a firewall rule to allow ssh traffic from IP range 35.235.240.0/20 this is a fixed IP range provided by google.
- Cloud NAT
  - Cloud NAT (Network Address Translation) is a service that allows you to provide Internet connectivity to instances that have only private IP addresses, without exposing those addresses to the Internet.
- VPC Peering
  - VPC Network Peering enables you to connect VPC networks so that workloads in different VPC networks can communicate internally.
- Shared VPC
  - Shared VPC allows an organization to connect resources from multiple projects to a common Virtual Private Cloud (VPC) network, so that they can communicate with each other securely and efficiently using internal IPs from that network.
- Hybrid network connectivity
  - Cloud VPN: Cloud VPN is a service that allows you to create secure, encrypted connections between your on-premises data center and your Google Cloud VPC networks. Cloud VPN uses the IPsec protocol to create a secure tunnel between your on-premises VPN gateway and the Cloud VPN gateway in Google Cloud.
  - Dedicated Interconnect: Dedicated Interconnect is a service that allows you to establish a direct physical connection between your on-premises data center and Google Cloud. Dedicated Interconnect provides a dedicated, high-bandwidth connection that is not shared with other customers, ensuring reliable and consistent network performance.
  - Partner Interconnect: Partner Interconnect is a service that allows you to connect to Google Cloud through a partner network, providing a private and secure connection to your Google Cloud resources. Partner Interconnect is ideal for customers who need to connect to Google Cloud from locations where Dedicated Interconnect is not available.
  - Cloud Router: Cloud Router is a service that allows you to dynamically exchange routes between your on-premises network and your Google Cloud VPC networks. Cloud Router enables you to create dynamic routing policies that can optimize traffic flows and ensure high availability.
- Load Balancer
  - Load Balancing is a service that enables you to distribute incoming network traffic across multiple instances of your application, improving performance, availability, and scalability.
  