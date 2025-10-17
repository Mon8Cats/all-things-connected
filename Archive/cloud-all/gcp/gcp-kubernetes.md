# Google Kubernetes

## Workload Identity

Workload Identity (now officially known as Workload Identity Federation for GKE) in Google Cloud is the recommended and more secure way for applications running in Google Kubernetes Engine (GKE) to access Google Cloud services. It allows your Kubernetes Service Accounts (KSAs) to act as Google Cloud IAM Service Accounts (GSAs), eliminating the need to manage and store sensitive GSA keys within your Kubernetes cluster.   

Here's a breakdown of how it works and its benefits:

The Problem it Solves:

Traditionally, GKE workloads needed to authenticate to Google Cloud services using one of these less-than-ideal methods:   

Node's Compute Engine Service Account: Granting broad permissions to the underlying Compute Engine instances, violating the principle of least privilege as all pods on the node would inherit these permissions.
Service Account Keys: Creating and storing GSA keys as Kubernetes Secrets, which introduces significant security risks (key management, rotation, potential for leaks).   
How Workload Identity Federation for GKE Works:

Workload Identity Federation for GKE establishes a trust relationship between your GKE cluster and Google Cloud IAM. Here's the process:   

Enable Workload Identity on the GKE Cluster: When you enable Workload Identity on a GKE cluster, GKE does the following:

Creates a unique workload identity pool for your Google Cloud project.
Registers the GKE cluster as an identity provider in this pool.   
Deploys the GKE metadata server (as discussed previously) on each node. This server intercepts requests for credentials.   
 Associate Kubernetes Service Accounts with Google Cloud Service Accounts: You create an IAM policy binding that links a specific KSA in your GKE cluster to a specific GSA in your Google Cloud project. This binding essentially grants the KSA the permission to impersonate the GSA.   

Annotate Kubernetes Pods: You annotate the Pod specification (or the Service Account used by the Pod) with the email address of the GSA you want the Pod to impersonate.

Workload Authentication: When a Pod with the correct annotation needs to access a Google Cloud API:

Its request for credentials is intercepted by the GKE metadata server.   
The GKE metadata server exchanges the KSA's JWT (JSON Web Token) with Google's Security Token Service.   
The Security Token Service verifies the KSA's identity based on the trust established with the GKE cluster.
If the KSA is authorized to impersonate the linked GSA (due to the IAM policy binding), the Security Token Service issues a short-lived federated access token associated with the GSA.   
The GKE metadata server provides this token to the Pod.   
The Pod can then use this short-lived token to authenticate to Google Cloud APIs as the GSA.   
Key Benefits of Workload Identity Federation for GKE:

Enhanced Security: Eliminates the need to store and manage long-lived service account keys, significantly reducing the attack surface.   
Principle of Least Privilege: Allows you to grant specific IAM permissions to individual Kubernetes Service Accounts, ensuring that each application has only the necessary access.
Improved Auditability: Provides a clearer audit trail of which application (identified by its KSA) is accessing Google Cloud resources.
Simplified Management: Centralizes identity and access management through IAM policies.   
No Code Changes (Mostly): In many cases, existing Google Cloud client libraries automatically handle the token exchange, requiring minimal to no code changes in your applications.   
Workload Identity Federation Beyond GKE:

It's important to note that Workload Identity Federation is a broader Google Cloud IAM feature that extends beyond GKE. It allows workloads running in other environments (like AWS, Azure, on-premises, or other identity providers) to access Google Cloud resources using their existing identities, without needing GSA keys. In these scenarios, you configure identity pools and providers to establish trust with the external identity provider.   

In summary, Workload Identity Federation for GKE is the modern and secure way for your GKE applications to authenticate to Google Cloud services. By leveraging the identity of Kubernetes Service Accounts and federating it with Google Cloud IAM, it enhances security, simplifies management, and adheres to the principle of least privilege.   



## Workload Identity

- When enable workload identity and the first cluster in a project, GKE automatically creates the pool by using the format PROJECT_ID.svc.id.goog 
- any ne node pools that I create have workload identity enabled by default.
- containers deployed to those node pools are then able to use its service account credentials to authenticate to Google Cloud services.
- create a new node pool -> enable workload identity -> configure application authentication -> assign kubernetes service account ->
- create a new namespace for the service account -> create a new k8s service account for my application -> create an IAM allow policy that references the K8s sa

```bash
gcloud projects add-iam-policy-binding 
  myProjectId
  --role="ROLE_NAME"
  --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/
    workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME
  --condition=None
```

- grant the required roles to the sa.

```bash
gcloud projects add-iam-policy-binging myProjectID
gcloud storage buckets add-iam-policy-binding
  gs://BUCKET
  --role=roles/storage.objectViewer
   --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/
    workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME
  --condition=None
```

- add the name of the sa and identify which specific nodes the Pod should be scheduled to run
- 

## Access Control and Security

- K8s Authentication and Authorization
- K8s RBAC and Google IAM
- Workload Identity
- Pod Security Standard and Admission
- Role-Based Access in GKE
- Individual user accounts (humans), K8s service accounts (applications)
- Cloud Identity Domain: user accounts
- IAM: permissions to user accounts and groups
- Workload Identity:
  - pod starts -> it receives SA credentials from the GKE metadata server
  - GKE metadata server?
- IAM (out of cluster), RBAC (within cluster level)
- RBAC:
  - who (users, groups, SAs) can do what (actions allowed) on which resource (K8s objects)
  - Roles: connect API resources and verbs
  - RoleBindings: connect roles to subjects
  - use RBAC to grant users access to specific K8s namespaces
  - namespaced=true - namespaced resources
  - namespaced=false - cluster-wide resources

## Namespace

Ah, namespaces in Kubernetes (and therefore GKE, which is a managed Kubernetes service) are a fundamental concept for organizing and isolating resources within a single cluster. Think of them as virtual clusters within your physical cluster.   

Here's a breakdown of what they are and why they're important:

What is a Namespace?

A Kubernetes namespace provides a mechanism to:

Logically partition resources: You can group related resources (like Deployments, Services, Pods, Secrets, ConfigMaps, etc.) together into a namespace. This makes it easier to manage and understand your cluster, especially as it grows in complexity.   
Provide scope for names: Resource names within a namespace must be unique, but the same name can be used in different namespaces without conflict. This allows different teams or applications to use intuitive names without worrying about collisions.   
Enforce resource quotas: You can set resource quotas at the namespace level to limit the total amount of CPU, memory, and storage that can be consumed by all resources within that namespace. This helps prevent one team or application from monopolizing cluster resources.   
Implement access control policies: You can use Role-Based Access Control (RBAC) to define what actions users or service accounts can perform on resources within specific namespaces. This allows for granular security and isolation between different teams or environments.   
Why are Namespaces Important?

Organization: As your Kubernetes cluster scales, managing hundreds or thousands of resources in a single flat structure becomes incredibly difficult. Namespaces provide a way to bring order and structure to this complexity.
Isolation: Namespaces allow you to isolate different teams, projects, or environments (e.g., development, staging, production) within the same physical cluster. This prevents accidental interference and helps maintain stability.   
Resource Management: Resource quotas on namespaces ensure fair resource allocation and prevent resource starvation for critical applications.   
Security: RBAC policies applied at the namespace level provide a strong security boundary, limiting access to resources based on roles and responsibilities.   
Multi-tenancy: Namespaces are a key building block for achieving multi-tenancy in a Kubernetes cluster, allowing multiple independent users or teams to share the same underlying infrastructure in a controlled and isolated manner.   
Common Use Cases for Namespaces:

Environment Separation: Creating namespaces like development, staging, and production to isolate different stages of your application lifecycle.
Team-Based Organization: Assigning a namespace to each development team to manage their own applications and services.
Application Isolation: Deploying different applications or microservices into separate namespaces to improve organization and prevent conflicts.   
Testing and Experimentation: Creating temporary namespaces for testing new features or configurations without impacting production environments.
Default Namespaces:

Kubernetes comes with several default namespaces:

default: This is the namespace where resources are created if you don't explicitly specify one. It's generally recommended to avoid using the default namespace for production workloads.   
kube-system: This namespace contains core Kubernetes system components, such as the API server, controller manager, scheduler, and kube-proxy. You should generally not modify or deploy your own applications in this namespace.
kube-public: This namespace is readable by all users (including unauthenticated ones) and is typically used for resources that need to be publicly accessible within the cluster.   
kube-node-lease: This namespace is used by the kubelet to publish heartbeat Leases associated with each node in the cluster.   
In the context of GKE:

GKE fully supports Kubernetes namespaces and encourages their use for the same reasons mentioned above. When you create a GKE cluster, these default namespaces are automatically provisioned. You can then use kubectl (the Kubernetes command-line tool) or the Google Cloud Console to create and manage your own namespaces within your GKE cluster.

In summary, namespaces in Kubernetes and GKE are a powerful abstraction that allows you to logically organize, isolate, manage resources, and enforce policies within a shared cluster environment. They are essential for building scalable, secure, and maintainable containerized applications.   


Sources and related content



## Metadata Server

The GKE metadata server is a crucial component in Google Kubernetes Engine (GKE) clusters, especially when Workload Identity (now known as Workload Identity Federation for GKE) is enabled. It acts as an interceptor for requests made by pods to the underlying Compute Engine metadata server of the GKE nodes.   

Here's a breakdown of its purpose and function:

Problem it solves:

By default, pods running on GKE nodes have access to the Compute Engine metadata server. This server contains potentially sensitive information about the node, including:   

Kubelet credentials: These could be used for privilege escalation attacks within the cluster.   
VM instance identity tokens: These can be used to impersonate the underlying Compute Engine instance, potentially leading to instance-level escalation.
Node's service account credentials: If the node has a service account attached (which is common), these credentials could be accessed by any pod on that node, violating the principle of least privilege.
How the GKE Metadata Server works:

When Workload Identity is enabled on a GKE cluster:

Deployment: GKE automatically deploys a DaemonSet called gke-metadata-server in the kube-system namespace. This ensures that a gke-metadata-server pod runs on each node in the cluster.
Interception: These gke-metadata-server pods run on the host network and intercept all HTTP requests from other pods (not running on the host network) that are directed to the standard Compute Engine metadata server endpoint (metadata.google.internal).
Workload Identity Integration: When a pod configured to use Workload Identity makes a request for credentials:
The gke-metadata-server intercepts this request.
It requests a Kubernetes Service Account token (a JWT) from the Kubernetes API server, which identifies the requesting workload.   
The gke-metadata-server then exchanges this JWT with Google's Security Token Service for a short-lived federated access token that is associated with the intended Google Cloud service account linked to the Kubernetes Service Account via IAM policies.
Finally, the gke-metadata-server returns this short-lived Google Cloud service account token to the requesting pod.
Filtering (Without Workload Identity): Even without Workload Identity fully configured, the GKE metadata server, when enabled, can be configured to filter access to sensitive metadata paths like kube-env and the VM's instance identity token, offering a degree of protection.
Benefits of the GKE Metadata Server:

Enhanced Security: By intercepting and potentially filtering access to the underlying Compute Engine metadata server, it prevents unauthorized access to sensitive credentials and reduces the risk of privilege escalation attacks from compromised pods.   
Facilitates Workload Identity: It is a fundamental component required for Workload Identity to function correctly, enabling pods to securely authenticate to Google Cloud services using Kubernetes Service Accounts instead of node-level or less secure methods like service account keys.   
Improved Auditability: Using Workload Identity in conjunction with the GKE metadata server provides a more auditable way to track which application (pod/Kubernetes Service Account) is accessing which Google Cloud resource.
Principle of Least Privilege: Workload Identity, enabled by the GKE metadata server, allows you to grant specific IAM permissions to individual Kubernetes Service Accounts, adhering to the principle of least privilege.   
In essence, the GKE metadata server is a security enhancement for GKE clusters. When used with Workload Identity, it provides a secure and manageable way for your containerized applications to authenticate to Google Cloud services while protecting sensitive node-level metadata from being accessed by workloads that shouldn't have access.   


--


kubectl get daemonsets // long running process in all nodes 
kubectl get deamonsets -n kube-system // name space
monitoring 



- secret management
- secret manager
- standard
- autopilot
- deploying workloads
  - yaml - simple format 
- first pod, auto scaled pods
- kubectl config get context 
- kubectl get nodes
- cd yaml/ yamls folder -
- selector: 
  - matchLabels:
    - app: demo-api
  - tempate:
    - name
- kubectl apply -f internaldeployment.yaml
- kubectl get deployment
- 








We also have 2 pluralsight training channels that could be very useful:
Kubernetes for Developers - https://app.pluralsight.com/channels/details/1c6021ec-d7a0-4a80-8bfe-5344eb1cde26
Kuberenets for DevOps Engineers - https://app.pluralsight.com/channels/details/ac74e987-c9da-43ea-a694-162e38d5dad3

References:

https://confluence.app.medcity.net/c/pages/viewpage.action?pageId=237536511

https://confluence.app.medcity.net/c/pages/viewpage.action?pageId=237536511&preview=/237536511/258407786/GKE%20Self-Service%20Guide.pdf

https://hcahealthcare.sharepoint.com/sites/Corp-CloudCenterofExcellence/SitePages/Cloud-Delivery.aspx?e=4%3a1fb1eb2d7c0b4561bdcabca0cbb4895a&web=1&sharingv2=true&fromShare=true&at=9&CID=f6c5451f-b36a-44dd-a26f-3566e2e0e260

- node pools
- node 
- networking
- security
- metadata
- autopilot cluster 

## K8s Session 

### (1) Topics

- containers, k8s
- create configure GKE clusters
- strategies for deploying/managing workloads
- Scale in GKE
- cluster maintenance 

### (2) VM or Container

- VM-centric or Container-centric
- [app/user space/dependencies]^2 / container runtime / kernel / hardware + hypervisor
- process isolation, file system isolation, resource limits, 
- shared kernel, minimal overhead, startup in seconds

## Docker file

```base
Dockerfile
docker build -t api:v1 .
docker images
docker run -d -p 8082:8082 api:v1
docker ps
docker images
docker run -d -p 8080:8080 --network="host" ui:v1
got to the port 8080
how to manage multiple image, 
how to talk to each other

linux process
linux namespaces
linux cgroups
union file system
container runtime: Docker or containerd 
```

### Container Orchestration

- manage a whole group
- figure out where in group to launch my app
- watch my app and restart
- add or remove copies
- automatically configure app load balancers
- automate rolling upgrades and rollbacks


### k8s

- open source, orchestration tool
- orchestration, manage
- a set of APIs to deploy containers on a set of nodes (a cluster)
- a set of primary components


## K8s Operations

- kubectl commands
- user -> kubectl (location, credentials) -> kube APIserver (Control plane)
- $HOME/.kube/config. # configuration file
  - the list of clusters
  - the credentials that will be attached to each
- GKE provides the credentials through the gcloud command
- kubectl get pods -> kubectl -> API call through HTTPS -> cluster/control plane/kube-apiserver
- connect kubectl to a GKE cluster
  - gcloud container clusters get-credentials cluster_name --region region_name 
  - it write configuration info into a config file
- kubeclt
  - can't create new clusters
  - can't change the shape of existing clusters
  - [command] what do you want to do?
    - get, describe, logs, exec,
  - [type] on which type of object?
    - pods, deployments, nodes,
  - [name] what is the object's name?
    - kubectl get pod my-test-app
  - [flags] any special requests?
    - kubectl get pod my-test-app -o=yaml
  - kubectl commands for creating, viewing, deleting k8s objects
  - viewing or exporting config files
  - parameters: --kubeconfig or --context
  - kubectl get pods
  - kubectl describe pod pod-name
  - kubectl exec [pod-name] -- [command] # run a single command inside a container
    - kubectl exec demo -- env
    - kubectl exec demo -- ps aux
    - kubectl exec demo --cat /proc/1/mounts
    - kubectl exec demo -- ls /  
  - kubectl exec -it [pod-name] --[command] # run a command within a pod
    - kubectl exec -it demo -- /bin/bash 
  - kubectl logs [pod-name]

## k8s Manifest file

```bash
apiVersion: v1
kind: Pod
metadata:
  name: nginx <- all object are identified by name>
  uid: a unique identifier generated by  K8s
  labels: key-value pairs to tag
spec:
  containers:
  - name: nginx
    image: nginx: latest 

#object controllers: deployments, StatefulSets, DaemonSets, and jobs
#deployment controller creates a child object (a replica set)
#replica set controller check the running pods

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx: latest



```
## K8s Architecture 

- K8s Concepts: 
  - K8s object model: Cluster: control plane + Node(pod -> container -> app)s
    - object spec, object status: 
      - desired state, 
      - current state
      - compare the desired state with the current state
    - object -> kind ->pod : 
      - shared networking : unique IP address, shared network namespace 
      - shared storage :
      - containers :
  - Declarative management
- K8s components (under cluster)
  - control plan:
    - kube-APIserver: interaction with user/system via kubectl command
    - etcd : store the state of the cluster
    - kube-scheduler : schedule (not launch) pods onto the nodes
    - kube-controller-manager : monitor the sate of a cluster,
      - objects are managed by loops of code (controllers)
      - a deployment controller object: runs, scales
      - the node controller (a system object): monitor and respond when a node is offline
    - kube-cloud-manager
      - interact with underlying cloud providers
  - Node:
    - kubelet = an K8s agent on each node, 
      - interact with kube-APIserver
      - uses the container runtime to start the pod and monitors its lifecycle
    - Container runtime: 
      - a software used to launch a container from a container image
      - uses containerd
    - Kube-proxy: 
      - maintain network connectivity among the pods in a cluster
      - network connectivity is accomplished by using the firewall in capabilities of IP tables
      - (which built into the linux kernel)
    - Pod
- K8s and GKE
  - Autopilot: GKE manages the underlying infrastructure
    - node configuration, auto-scaling, auto-upgrades, networking configuration.
  - Standard: 
- Autopilot mode:
  - optimizes the management of Kubernetes
  - Less management overhead
  - less configuration options
  - only pay for what I use
  - (restrictions, no SSH, no privilege escalation, limit on node affinity)
- Standard mode:
  - configure in many different ways
  - management overhead
  - fine-grained control
  - pay for all of the provisioned infrastructure


## Cloud Computing

- get resources on-demand, self-service
- access resources over the internet
- resources allocated out of pool.
- resources are elastic 
- pay as use or reserve as go

## Google Services, Products

- Computer Engine
  - IaaS: compute, storage, network
  - Predefined/customized VMs
  - Persistent disks and local SSDs
  - Managed instance groups
  - Per-second billing
  - complete control
  - on-prem workloads -> lifted shifted easily
- GKE
  - runs containerized applications 
  - code packaged with all its dependencies 
- App Engine
  - PaaS
  - bind code to libraries
  - focused on application logic
  - infrastructure provided by Google
  - integrated with Google tools
  - version control and traffic splitting 
- Cloud Run Functions
  - event-based, asynchronous compute solution 
  - executes code in response to events
  - functions as a service offering
- Cloud Run
  - managed computer platform 
  - runs stateless containers
  - serverless 
  - built on knative
  - charges only for resources used 

## Google Network

- Geographical locations
- locations, regions, zones

## Resource Management

- Organization - folder - project - resources 
- Project Name, ID, Number
- IAM : Identity and Access Management
- Who can do what on which resources 
- Cloud Provider: hardware, networks, physical security
- Customer: configurations, access policies, user data

## Billing 

- billing is established at the project level
- a billing account can be linked to zero or more projects
- billing accounts, billing sub-accounts, 
- budgets, alerts, reports, quotas (rate, allocation)

## Interaction with Google Cloud

- Google Cloud Console
- Google Cloud SKD and Cloud Shell (gcloud tool, gcloud storage, bg, 5gb vm, ephemeral)
- APIs
- Google Cloud App 

## Containers and Kubernetes

- Containerization 
- Containers, Container Images, Kubernetes, GKE, Cloud Build 
- Containers?
  - Dedicated Server: hardware - kernel - dependencies - application code
  - VM: hardware + Hypervisor - kernel - dependencies - (app)^n
  - VM: hardware + Hypervisor - (kernel - dependencies - app)^n
  - VM: hardware + Hypervisor - kernel - container runtime - (dependencies - user space - app)^n
  - container: dependencies + application code
- Container Images
  - Build/run container image: docker, 
  - a container has the power of isolate workloads
  - linux process, linux namespaces, linux cgroups, union file systems, 
  - a container image is structured in layers, and the tool used to build the image
  - base image layers (R/O) + thin R/W layer(container layer)
  - docker file: each instruction specifies a layer inside the container image
  - each layer is read-only, but when a container runs form this image, it will have a writeable ephemeral topmost layer.
  - from ubuntu:18.04 -> create a base layer from a public repository
  - copy ./app -> add a new layer, which contains some files
  - rum make/app -> make command and put the results of the build into a third layer
  - cmd python/app/app.py -> specifies what command to run within the container
  - not a best practice to build my app in the same container where I ship and run it.
  - application packaging relies on a multi-stage build process
  - one container builds the final executable image
  - a separate container receives only what is needed to run the application
  - the container runtime adds a new writable layer on top of the underlying layers called the container layer
  - all changes made to the running container are written to this thin writable container layer

## Kubernetes Architecture

## Kubernetes Operations

----------------------------------------------------

While the names are similar, Google Cloud Run and Google Cloud Run Functions (formerly known as Google Cloud Functions 2nd Gen) serve different purposes and offer distinct levels of abstraction for serverless compute on Google Cloud. Here's a breakdown of their key differences:   

Google Cloud Run:

Focus: Running containerized applications. You package your application (code, dependencies, runtime) into a Docker container image and deploy that image to Cloud Run.   
Flexibility: Offers maximum flexibility as you have full control over the container image, including the operating system, programming language, libraries, and any other dependencies. You can run virtually any type of application, including web applications, APIs, background workers, and more.   
Deployment: You deploy container images stored in a container registry (like Google Container Registry or Artifact Registry).   
Abstraction Level: Lower level of abstraction compared to Cloud Run Functions. You manage the containerization process.   
Use Cases: Best suited for:
Deploying existing containerized applications.   
Applications requiring specific runtime environments or dependencies not directly supported by Cloud Run Functions.   
Longer-running services and web applications.   
More complex application architectures.
Scaling: Automatically scales based on incoming requests, including scaling to zero when there's no traffic.   
Billing: Billed based on the compute resources (CPU, memory, network) consumed during request processing. You also pay for idle instances if you configure a minimum number of instances.   
Google Cloud Run Functions (formerly Cloud Functions 2nd Gen):

Focus: Running single-purpose, event-driven functions directly from source code. You write code in a supported language (like Node.js, Python, Go, Java, .NET) and Cloud Run Functions handles the containerization and infrastructure.   
Simplicity: Offers a higher level of abstraction and a simpler development experience for event-driven scenarios. You focus on writing code for specific events without managing containers.   
Deployment: You deploy source code directly. Google Cloud builds a container image for you behind the scenes using buildpacks.   
Abstraction Level: Higher level of abstraction compared to Cloud Run. Google manages the containerization and underlying infrastructure.   
Use Cases: Best suited for:
Responding to events from other Google Cloud services (e.g., Cloud Storage, Pub/Sub, Firestore).   
Creating lightweight APIs and webhooks.   
Serverless event processing and data transformation.   
Quickly building and deploying simple backend logic.
Scaling: Automatically scales based on the number of events or requests, including scaling to zero when idle.   
Billing: Billed based on the function's execution time, the number of invocations, and the resources (CPU, memory) consumed during execution. You pay only when your function is actively running.   
Here's a table summarizing the key differences:

Feature	Google Cloud Run	Google Cloud Run Functions (formerly Cloud Functions 2nd Gen)
Deployment Unit	Container Image	Source Code (function)
Containerization	You manage the Dockerfile and build.	Google Cloud handles it automatically.
Flexibility	High (full control over environment)	Lower (limited to supported languages and runtimes)
Abstraction	Lower	Higher
Primary Use Case	Containerized apps, web services, APIs	Event-driven functions, lightweight APIs, event processing
Complexity	More complex to set up initially	Simpler to get started with
Control	More control over infrastructure	Less control, focus on code
Billing	Based on resource consumption & idle instances (if configured)	Based on execution time, invocations, and resource usage

Export to Sheets
In essence:

Choose Cloud Run when you need the flexibility and control of containers for deploying various types of applications.
Choose Cloud Run Functions when you want a simpler, event-driven serverless experience focused on running individual functions in response to events or HTTP requests, without managing containers.
It's also worth noting that Google has been converging its serverless offerings. Cloud Run Functions now leverages the underlying infrastructure of Cloud Run, giving it access to some of Cloud Run's advanced features.   


Sources and related content
