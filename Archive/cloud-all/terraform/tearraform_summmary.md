# Terraform

## Using Terraform

- IaC: benefits and principles
  - tools: build, change, mange my infrastructure
  - old way:
  - new way (IaC):
    - consistency, time savings, documented in code, version controlled
    - tf files 
    - init, validate, plan, apply, destroy
- Terraform ecosystem and core concepts
  - write, plan, apply cycle
  - providers: interacting with cloud platforms exposing resources for management
  - resources: describe infrastructure objects
  - data sources: information defined outside of terraform
  - state file: tracks the current state of managed resources
    - stored in my terraform cloud space (remote backend)
    - sensitive date?
- deploy dev project
  - Company Terraform Architecture?
    - GitHub -> Private Module Registry (proof, consistent, tested)? 
      - computer run terraform -> terraform state file (encrypted)
      - providers? cloud platform, scanning software? best practices, 
      - PMR (public or private module registry)
      - native tools or third party tools
      - security tools between each steps
  - Innovation vs Sandbox
  - Deploying a Storage Account
  - GitHub enterprise/GitHub org/Team or App Git Repo/Dev, QA, Prod Branch
  - GitHUb OIDC Auth
  - Terraform Cloud Service Account Workload Identity Federation for Auth
  - Terraform Cloud for Business
  - Cloud Service Provider
  - Projects/Resource Groups,
  - Cloud and on-prem
  - Azure EntralID Auth
  - HashCorp Vault
  - Private Module Registry
  - Some Steps
    - GitHub
    - Workspace
    - Private MOdule Registry
    - Sentinel Policy Checks (Sentinel scanning, security check)
    - Cloud Service (via Workload Identity Federation)
    - HashCorp Vault for Secret Manage
    - Wiz.io security scanning = scanning code
    - Security policy
  - Environment Requirements
    - Install Terraform
    - Install a IDE (VSCode)
    - Request local permission?
    - download terraform? - find the correct one for use (1.11.4 linux, windows)
  - Developer platform
    - company version of starting point
    - Dev environment, sandbox environment
      - dev - precursor for actual app environment
      - create a project for me
      - catalog entry?
      - github repository, dev branch 
      - deploying storage account?
    - Create a storage
      - go to terraform registry, find module - copy (1)
      - clone the git repository locally
      - go to main.tf
        - add the terraform module code (1)
      - go to provider.tf
        - workspace -- check or update
      - tf init -->, (pull in all providers) HashCorp terraform extension 
      - tf plan --var-file=environments/dev.tfvars (env specific)
      - my terraform work space -> hit this space -> how to setup credentials
      - git -> commit 
      - go to github repo
      - actions/workflow -already setup -> 
      - promote code?
      - some additional testing?
      - add individual users?
      - deploy to infrastructure project? working directory?
- terraform plan
- sentinel policy
- modules
- workflows, ci/cd pipelines
- version control practices

## Capability Packages

- a super module: a versioned collection of Terraform resources and modules interconnected.
- save time 
- module = capability package for now
- Starred Templates
- Launch Template
- setup, load balancer, frontend, backend, cloud sql, cloud storage, review (cloud run?)
  - select project
  - load balancer (internal), certificate -> need team email
  - front end: cloud run -> user interaction?
    - give name (actual cloud run instance name, service name)
    - dns zone : external (servicename.hca.cloud) or internal (app.hca.cloud)
  - back end:
    - enable SQL access? (not check)
    - enable identity aware proxy (IAP) (check)
    - Azure AD group: set a member for this - base group?
    - Additional AD group
    - URL routing: (not yet, check= add additional host)
    - Custom Routing 
    - Overview 
  - Run
    - all steps: 
    - success: send email, documentation, 
      - approve PR?
      - create cicd pipeline
      - pull request (PR)
        - resource change summary 
  
## App Dev

- dev.tfvars - service definition
- create cicd
- dev/create/search cicd template/click
  - dev envronment
  - get our product, project
  - service name
  - component type: web site
  - url: from the service definiton
  - sql: none 
  - language: Neutron React
  - Enable ApigeeX : no
  - it shows summary
  - create github repository (with workflow...)
  - terraform login?





## Terraform Backend

A Terraform backend defines where Terraform stores its state file. When I use a remote backend (like Google Cloud Storage), it enables features such as state locking and remote state sharing.
Before I create a bucket to use as my Terraform backend, I need to ensure that the Cloud Storage API is enabled for my project. In Google Cloud, the service name is storage.googleapis.com.

```bash
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }

  backend "gcs" {
    bucket = "a unique bucket name"
    prefix = "terraform/state"
  }
}

provider "google" {
  project     = var.project_id
  region      = var.region
  credentials = file(var.credentials_file)
}


# Enable the Cloud Storage API
resource "google_project_service" "enable_storage" {
  service            = "storage.googleapis.com"
  disable_on_destroy = false
}

# Create the Cloud Storage bucket for Terraform backend
resource "google_storage_bucket" "terraform_backend" {
  name          = var.bucket_name
  location      = var.bucket_location
  force_destroy = true

  # Ensure the API is enabled before creating the bucket.
  depends_on = [google_project_service.enable_storage]
}

# 
terraform init -migrate-state
```

### Backend Config Files

Once the bucket exist, update my main configuration to use a remove backend. Since I can't use viariable directly, I have two options.

1. Hard-code the values in the backend block: Edit my main.tf to include a static block. Then run "terraform init -migrate-state". This command will initialize the remote backend and migrate my state form local to GCS.
2. Use a Backend Configuration File: Instead of hardcoding, I can place the backend configuration in a separate file (e.g., backend.tfvars). Then initialize Terraform with "terraform init -backend-config=backend.tfvars". This  approach keeps sensitive or environment-specific information outside of my main configuration.
