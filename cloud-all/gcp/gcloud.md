# Interact with GCP

## What is gcloud CLI?

The gcloud CLI (Command-Line Interface) is the official command-line tool for managing Google Cloud Platform (GCP) resources. It allows users to interact with GCP services from the terminal, automate tasks, and configure infrastructure without using the GCP Console.
But some GCP services have specific CLI tools.

- Cloud Storage, gsutil is used.
- Cloud BigQuery, bq is used.
- Cloud Bigtable, cbt is used.
- Kubernetes, kubectl is used.

### Some Commands

```bash
     gcloud config set project dole-dole
     gcloud auth login # authorize my session?
     gcloud auth list # all accounts authenticated with the gcloud




    gcloud group subgroup action ...
    gcloud --version
    gcloud init 
    gcloud auth login
    gcloud config list
    gcloud config set project [project-id]
    gcloud projects list
    gcloud config set compute/region us-central1
    gcloud config set compute/zone us-central1-a
    
    gcloud compute instances list
    gcloud compute instances create my-vm --zone=us-cental1-a
    gcloud compute instances start my-vm
    gcloud compute instances stop my-vm
    gcloud compute instances delete my-vm

    gcloud container clusters list
    gcloud container clusters create my-cluster --zone us-central1-a
    gcloud container clusters get-credentials my-cluster --zone us-central1-a
    gcloud container clusters delete my-cluster --zone us-central1-a

    gcloud run deploy my-service -image gcr.io/my-project/my-image \
        --region us-central1
    gcloud run services list
    gcloud run services delete my-service

    gcloud functions deploy my-function --runtime python39 \
        --trigger-http --allow-unauthenticated 
    gcloud functions list
    gcloud functions delete my-function 

    gcloud storage buckets list
    gcloud storage buckets create my-bucket \
        --location=us-central1
    gcloud storage cp file.txt gs://my-bucket/
    gcloud storage rm gs://my-bucket/file.txt
    gclopud storage buckets delete my-bucket 

    gcloud sql instances list
    gcloud sql instances create my-db \
        --tier=db-fi-micro --region=us-central1
    gcloud sql users set-password root \
        --instance=my-db --password=mypassword
    gcloud sql instances delete my-db

    gcloud iam service-accounts list
    gcloud projects add-iam-policy-binding my-project \
        --member="user:steve@exaple.com" \
        --role="roles/editor"
    gcloud iam roles list
    gcloud iam service-accounts create my-sa \
        --display-name "my service account" 
    gcloud iam service-accounts delete my-sa 
    gcloud projects add-iam-policy-binding \
        my-project \
        --member="serviceAccount:my-sa@my-project.im.gserviceaccount.com \
        --role="roles/storage.admin"
    gcloud iam service-accounts add-iam-policy-binding \
        ci-sa@my-project.iam.gserviceaccount.com \
        --member="user:johndoe@gmail.com" \
        --role="roles/iam.serviceAccountTokenCreator"
    gcloud projects remove-iam-policy-binding my-project \
        --member="serviceAccount:my-sa@my-project.im.gserviceaccount.com \
        --role="roles/storage.admin"
    gcloud projects get-iam-policy my-project

    gcloud builds list
    gcloud builds submit --tag gcr.io/my-project/my-image
    gcloud builds submit --config=cloudbuild.yaml . 


kubectl 
```

## Cloud Shell

GCP Cloud Shell is an interactive command-line environment that runs in a web browser and provides a pre-configured Linux shell with the gcloud CLI, SDKs, and common development tools pre-installed.

- Pre-configured GCP Environment – Comes with gcloud, kubectl, terraform, git, python, and other tools.
- No Setup Required – Runs directly in the browser with no installation needed.
- Secure and Temporary – Runs in an ephemeral VM that resets after 20 minutes of inactivity.
- Persistent 5GB Home Directory – Stores files and scripts persistently (/home/user).
- Integrated Web Preview – Allows testing web applications in a browser.
- Connect to Compute Engine & Kubernetes – Easily manage VM instances and GKE clusters.
- Supports SSH and Port Forwarding – Securely access GCP resources remotely.