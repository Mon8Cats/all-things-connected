# Step By Step

## Initial Setup

### 1. GitHub

- Install Google Cloud Build App
  - Settings/ GitHub Apps/ Google Cloud Build/ installationId = 55957239
- Create GitHub Access Token
  - Settings/ Developer settings/ Personal access tokens/ Tokens (classic)/ 
    - what privileges?
      - Repository Access (Read-Only, contents rather than the repo scope)
      - Webhook Management (adimin:repo_hook)
      - Additional Permissions (Optional: read:org, wire access only if pipeline must push changes back to the repository)
- Create GitHub Projects (Infra, CI, CD)
  - GitHub Account: Mon8Cats
  - monad-infra
  - monad-cd
  - monad-ci

### 2. GCP

- Clean Up GCP Account:
  - Cancel Cloud Billing
  - Delete GCP PRojects: Select a Project/ IAM & Admin/ Settings/ Shut Down

- Create GCP Project: 
  - console.cloud.google.com/
  - dole-dole: 846737158627

## GKE Infrastructure

- Create a bucket for terraform backend
  - Clone monad-infra to the cloud shell
  - Check the bucket: Cloud Storage/ Buckets
- 


## CI Pipeline

## CD Pipeline