# GCP Resources

## Resources and VPC

In Google Cloud Platform, resource can be categorized based on their relationship with VPC networking.

| GCP Resource | VPC | Google-managed VPC | no VPC |
| :---: | :---: | :---: | :---:|
| Compute Engine (VMs) | Yes | No | No |
| GKE Standard Cluster | Yes | No | No |
| GKE Autopilot Cluster | No | Yes | No |
| Cloud SQL (Private IP) | Yes | No | No |
| Cloud SQL (Public IP) | No | Yes  | No |
| Cloud Run (Without VPC Connector) | No  | Yes | No |
| Cloud Run (With VPC Connector) | Yes | No | No |
| Cloud Functions (Without VPC) | No | Yes | No |
| Cloud Functions (With VPC Connector) | Yes | No  | No |
| App Engine (Standard) | No | Yes | No |
| App Engine (Flexible) | Yes | No | No |
| Cloud Storage (Private Access) | Yes | No  | No |
| Cloud Storage (Public) | No | No | Yes |
| BigQuery | No | Yes | No |
| IAM | No | No | Yes |
| Cloud Build | No | No | Yes |
| Artifact Registry | No | No | Yes |
| Secret Manager | No | No | Yes |
| Cloud Logging | No | No | Yes |
| Cloud VPN | Yes | No | No |

## Resources and scope of availability

Google Cloud resource are categorized based on their scope of availability.

| GCP Resource | Global | Regional | Zonal |
| :---: | :---: | :---: | :---:|
| VPC | Yes | No | No |
| Public IP Addresses | Yes | No | No |
| Cloud Storage (Multi-Region) | Yes | No | No |
| Cloud CDN | Yes | No | No |
| Artifact Registry  | Yes | No | No |
| Cloud Build | Yes | No | No |
| Secret Manger  | Yes | No | No |
| Cloud Pub/Sub | Yes | No | No |
| BigQuery | Yes | No | No |
| Cloud Storage (Regional) | No | Yes | No |
| Cloud SQL | No | Yes | No |
| Cloud Run | No | Yes | No |
| GKE Autopilot | No | Yes | No |
| Cloud Spanner | No | Yes | No |
| Cloud Dataflow | No | Yes | No |
| Cloud Function | No | Yes | No |
| Cloud Composer | No | Yes | No |
| Cloud Interconnect | No | Yes | No |
| Private Google Access | No | Yes | No |
| AI/ML Services | No | Yes | No |
| Compute Engine | No | No | Yes |
| Persistent Disk  | No | No | Yes |
| GKE Standard Cluster | No | No | Yes |
| Cloud Filestore  | No | No | Yes |
| Local SSD | No | No | Yes |
| Cloud TPU | No | No | Yes |


## Resources by Service Type

| Type | Service | Description |
| :---: | :---: | :---: |
| Compute Service | | Used for running applications, virtual machines, and containers.|
|| Compute Engine | Virtual Machines in GCP. |
|| GKE | Managed Kubernetes service for containerized apps. |
|| Cloud Run | Serverless compute for running containers. |
|| Cloud Function | Serverless event-driven compute functions. |
|| App Engine| Fully managed application platform. |
|| Bare Metal Solution | Dedicated hardware for workloads needing bare metal. |
|| Cloud GPUs/TPUs | Specialized compute for AI/ML workloads. | 
| Storage Service | | Used for storing files, objects, and structured/unstructured data.|
|| Cloud Storage | Object storage for files, images, and backups. |
|| Persistent Disk | Block storage for Compute Engine VMs. |
|| Firestore | Automates large-scale data transfers. |
|| Cloud Storage Transfer Service | Automates large-scale data transfers. |
|| Backup and DR | Backup service for VMs and databases. |
| Networking Service | | Handles VPC networking, hybrid connectivity, and load balancing.|
|| VPC | Private networking for GCP resources. |
|| Cloud Load Balancing | Global and regional load balancers. |
|| Cloud VPN | Securely connects on-prem to GCP. |
|| Cloud Interconnect | High-speed direct connection form on-prem to GCP. |
|| Private Google Access | Allows VPC resources to access Google services privately. |
|| Cloud NAT | Enables internet access for private resources. |
|| Cloud DNS | Managed domain name system service. |
| Database Services | | Fully managed relational, NoSQL, and analytical databases.|
|| Cloud SQL | Manged relational databases. |
|| Cloud Spanner | Horizontally scalable, globally distributed relational database. |
|| BigQuery | Serverless data warehouse for analytics. |
|| Firestore | NoSQL document database, real-time sync. |
|| Firebase | NoSQL database for mobile and web apps. |
|| Memorystore | Managed caching for applications. |
|| AlloyDB | PostgreSQL-compatible database optimized for performance. |
| Security & IAM | | Provides authentication, access control, and encryption.|
|| IAM | Role-based access control for users and services. |
|| IAP | Secure web applications and services. |
|| Secret Manager | Securely stores API keys, passwords, and secrets. |
|| KMS | Manges encryption keys. |
|| Security Command Center | Security insights and threat detection. |
|| Cloud Armor | DDos and web application firewall (WAF). |
| Serverless & Integration | | Event-driven and serverless services.|
|| Cloud Function | Serverless event-driven functions. |
|| Cloud Run | Serverless compute for containers. |
|| App Engine | Fully managed platform for web apps. |
|| Cloud Tasks | Managed task queues for background processing. |
|| Cloud Scheduler | Cron job scheduling services. |
|| Eventarc | Event-driven architecture for GCP services|
| DevOps & CI/CD | | Tools for automating deployments and managing infrastructure.|
|| Cloud Build | CI/CD pipeline for building and deploying apps. |
|| Artifact Registry | Stores container images and artifacts. |
|| Cloud Deploy | Automated continuous delivery for GKE. |
|| Cloud Source Repository | Private Git Repositories. |
|| Cloud Workstations | Cloud based developer environments. |
| Monitoring & Logging | | Observability tools for monitoring and debugging applications.|
|| Cloud Logging | Collects, monitors, and analyzes logs. |
|| Cloud Monitoring | Tracks performance and health of resources. |
|| Cloud Trace | Distributed tracing for analyzing latency. |
|| Cloud Debugger | Debugging tool for live applications. |
|| Cloud Profiler | Performance analysis tool. | 
| AI & ML  | | Services for training and deploying ML models. |
|| Vertex AI | Unified AI platform for training and deploying models. |
|| Auto ML | No-code ML model training. |
|| AI Platform Prediction | Deploys trained ML models for inference. |
|| Cloud Natural Language API | Text analysis and sentiment detection. |
|| Cloud Vision API | Image recognition and analysis. |
|| Cloud Speech-to-Text | Converts speech into text. |
|| Cloud Translation API | Automatic language translation. |
| Hybrid & Multi-cloud | | Solutions for integrating GCP with on-prem and other cloud platforms.|
|| Antos | Hybrid and multicloud Kubernetes management. |
|| GKE Enterprise | Multi-cluster Kubernetes management. |
|| BigQuery Ommi | Query data across AWS, Azure, and GCP. |

## Serverless Services in GCP

| Type | Service | Description |
| :---: | :---: | :---: |
| Compute | | |
|| Cloud Run | Runs containers without managing VMs or clusters. Scales to zero. |
|| Cloud Function | Event-driven serverless functions that execute only when triggered. |
|| App Engine | Fully managed PaaS for deploying web apps. |
| Databases & Storage | | |
|| Firestore | Serverless NoSQL database. |
|| BigQuery | Serverless data warehouse. |
|| Firebase DB | Serverless real-time database for mobile/web apps. |
|| Cloud Storage | Serverless object storage for files, images, and backups. | 
| Event & Messaging | | |
|| Pub/Sub | Event-driven messaging system for real-time communication. |
|| Cloud Tasks | Asynchronous task execution with retries. |
|| Eventarc | Event-driven automation. |
| DevOps & Integration | | |
|| Cloud Build | Serverless CI/CD pipeline for builds and deployments. |
|| Cloud Scheduler | Fully managed cron job scheduler. |
|| Cloud Workflows | Automates workflow across services. |


## SaaS, PaaS, IaaS

| Type | Service | Description |
| :---: | :---: | :---: |
| SaaS || GCP fully manages the service including infrastructure, scalability, security, and updates. Users simply consume the service. Application (from here) <- Runtime <- OS <- Virtualization <- Hardware <- Networking |
|| BigQuery ||
|| Google Workspace ||
|| Cloud PUb/Sub ||
|| Cloud Translation API ||
|| Cloud Vision API ||
|| Cloud Natural Language API ||
|| Cloud Speech-to-Text ||
|| Cloud Text-to-Speech ||
|| Vertex AI ||
|| Secret Manager ||
|| Cloud Logging ||
|| Cloud Monitoring ||
| PaaS || Google manages infrastructure and runtime while users manage applications and configurations. |
|| App Engine ||
|| Cloud Run ||
|| Cloud Functions ||
|| Firestore ||
|| Firebase ||
|| Cloud SQL ||
|| Cloud Dataproc ||
|| Cloud Composer || 
|| Cloud Tasks || 
|| Eventarc ||
|| Cloud Workflows || 
| IaaS || Users have control over infrastructure components like VMs, networking, storage, and security, while Google manages the underlying physical hardware. Application <- Runtime <- OS (from here) <- Virtualization <- Hardware <- Networking |
|| Compute Engine ||
|| Persistent Disk ||
|| GKE ||
|| Cloud Storage || 
|| Cloud Filestore || 
|| Local SSDs ||
|| Cloud Load Balancing ||
|| Cloud VPC ||
|| Cloud Interconnect ||
|| Cloud VPN ||
|| Cloud NAT ||
|| Cloud Amor ||
|| Antos ||
|| Cloud IAM ||
