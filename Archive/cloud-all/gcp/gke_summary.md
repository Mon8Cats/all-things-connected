# GKE

## Default Node Pool

When I  create a GKE cluster, a node pool is automatically created unless I specify otherwise.
The default node pool refers to the initial set of nodes that are created when I provision a new GKE cluster.

```bash
gcloud container clusters create my-cluster --no-enable-autoprovisoning
gcloud container clusters create my-cluster --no-enable-default-node-pool
gcloud container node-pools create my-node-pool \
    --cluster=my-cluster \
    --num-nodes=3 \ 
    --machine-type=e2-standard-2
```

## Default Service Account and Agents

```bash
# the Google-managed GKE Service Agents for Control Plane
service-<PROJECT_NUMBER>@container-engine-robot.iam.gserviceaccount.com
# the Compute Engine default service account for Worker Nodes
PROJECT_NUMBER-compute@developer.gserviceaccount.com
# the Google-managed service agent for GKE API
service-<PROJECT_NUMBER>@gcp-sa-gke.iam.gserviceaccount.com
```

## Create a Custom Service Account for Worker Nodes

```bash
gcloud iam service-accounts create gke-node-sa \
    --display-name "GKE Node Service Account"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:gke-node-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/container.nodeServiceAccount"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:gke-node-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/logging.logWriter"

```

## Connect to the Kubernetes Cluster

```bash
gcloud container clusters get-credentials my-cluster \
    --zone use-central1-c \
    --project my-project-id

# fetching cluster endpoint and auth data
# kubeconfig entry generated for my-cluster
```

## Deploy Microservice to Kubernetes

```bash
kubectl create deplyment hello-world-api \
    --image=gcr.io/google-samples/hello-app:1.0
kubectl get deployment
kubectl expose deployment hello-world-api \
    --type=LoadBalancer \
    --port=8080
kubectl get services 
# the get external ip
kubectl get services --watch
# ctrl-c to stop watch
curl <external-ip:port>
curl <external-ip:port>/hello-world

# create hello-world.yaml deployemnt and service
kubectl apply -f hello-world.yaml
kubectl get svc hello-world-service
curl http://<EXTERNAL-IP>

kubectl scale deployment hello-world --replicas=3
kubectl get deployment
kubectl get pods 

gcloud container clusters resize my-cluster --node-pool default-pool \  
    --num-nodes=2 --zone=us-central1-c

# auto scaling for microservice 
kubectl autoscale deployment hello-world-api --max=10 --cpu-percent=70

# auto scaling for Kubernetes cluster
gcloud container clusters update my-cluster \
    --enable-autoscaling --min-nodes=1 --max-nodes=10

kubectl create configmap hello-world-config \
    --from-literal=RDS_DB_NAME=todos

kubectl get configmap hello-world-config 
kubectl describe configmap hello-world-config 

kubectl create secret generic hello-world-secret \
    --from-literal=RDS_PASSWORD=dummytodos 

kubectl get secret 
kubectl describe secret hello-world-secret

kubectl apply -f deployment.yaml

```

## Exploring GKE in GCP Console

Kubernetes Engine/ Kubernetes cluster/ Details, Nodes, Storage, Logs
Cluster, Workloads, Services & Ingress, Applications, Configuration, Storage, Object Browser, Migrate to containers


## Kubernetes

- open source container orchestration tool
- helps manage containerized applications

## Control Plane

- API server: entrypoint to K8s cluster <-> UI, API, CLI
- Controller Manager: keeps track of what happening in the cluster
- Scheduler: ensures Pods placement
- etcd: Kubernetes backing store
- Control Plan <-> Virtual Network <-> Nodes
- Virtual Network: creates one unified machine?

## Main Kubernetes Components

- Pod
- Services
- Ingress
- ConfigMap
- Secret
- Deployment
- StatefulSet
- DaemonSet

## Worker Node and Pod

- Node: virtual or physical machine
- Pod: smallest unit in kubernetes
  - An abstraction over container 
  - (or container runtime so it can replace container runtime)
  - don't need directly work with container runtime (Docker?)
  - A running environment or a layer on top of a container
  - Usually one application per pod
  - how to communicate each other (apps/components in pods)?
  - Each pod gets its own IP address
  - Pods are ephemeral - New IP address on re-creation - In-convenient

## Services and Ingress

  - Service has permanent IP address, can be attached to a pod
  - Lifecycle of Pod and Service not connected
  - Even a pod died and created, the service stayed with the same IP
  - App should be accessible through browser
  - Create external service for public access
  - Not not for database - Internal service (default)
  - The url of the external service is not practical (ip with port)
  - Ingress (friendly url) -> service -> app
