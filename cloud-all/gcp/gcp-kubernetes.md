# Google Kubernetes

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
