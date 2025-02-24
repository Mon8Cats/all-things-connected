# Terraform

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
