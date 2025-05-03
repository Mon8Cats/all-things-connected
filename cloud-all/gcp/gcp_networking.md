# GCP Networking

## Resources in the same VPC but different subnets using private IP addresses

- Internal Routing: automatically creates routes that enable instances in different subnets to reach each other's private IP ranges.
- Private IP addresses: a private IP address from the subnet IP ranges assigned to a resource
- Firewall Rules: need to configure firewall rules to explicitly allow the specific traffic.
  - configure ingress firewall rule on the destination
  - configure egress firewall rule on the source

## Resources in the same VPC and the same subnet: communication allowed by default

- Local Subnet Routing: 
- Implied Firewall Rules: 
  - Default VPC networks: default-allow-internal
  - Custom VPC networks: need to create an ingress firewall rule to explicitly allow











- Beginner:
  - Preparing for Your Professional Cloud Network Engineer Journey
  - Google Cloud Fundamentals: Core Infrastructure
- Intermediate:
  - Networking in Google Cloud: Fundamentals
- Advanced
  - Networking in Google Cloud: Routing and Addressing
  - Networking in Google Cloud: Network Architecture 
  - Networking in Google Cloud: Network Security 
  - Networking in Google Cloud: Load Balancing
  - Networking in Google Cloud: Hybrid and Multicloud
  - Logging and Monitoring in Google Cloud
  - Observability in Google Cloud
  
## Preparing for Your Professional Cloud Network Engineer Journey

- Introduction
- Designing and planning a Google Cloud Network
- Implementing Virtual Private Cloud (VPC) networks
- Configuring managed network services
- Implementing hybrid network interconnectivity
- Managing, monitoring, and troubleshooting network operations

## Google Cloud Fundamentals: Core Infrastructure

- Course Introduction
- Introducing Google Cloud
- Resources and Access in the Cloud
- Virtual Machines and Networks in the Cloud
- Storage in the Cloud
- Containers in the Cloud
- Applications in the Cloud
- Prompt Engineering

## Networking in Google Cloud: Fundamentals

- Welcome to Networking in Google Cloud	Module Watched	
2m 33s	
- VPC Networking Fundamentals	Module Watched	
12m 52s	
- Sharing VPC Networks	Module Watched	
23m 55s	
- Network Monitoring and Logging	Module Watched	
17m 25s	
- Course Resources		
10s	
The trademarks and tra

## Networking in Google Cloud: Routing and Addressing

- Welcome to Networking in Google Cloud		
56s	
- Network Routing and Addressing in Google Cloud		
31m 33s	
- Private Connection Options		
38m 34s	
- Course Resources

## Networking in Google Cloud: Network Architecture 

Welcome to Networking in Google Cloud	Module Watched	
49s	
Introduction to Network Architecture		
11m 39s	
Network Topologies		
19m 11s	
Course Resources

## Networking in Google Cloud: Network Security 

Welcome to Networking in Google Cloud	Module Watched	
1m 12s	
Distributed Denial of Service (DDoS) Protection	Module Watched	
17m 44s	
Controlling Access to VPC Networks		
32m 49s	
Advanced Security Monitoring and Analysis		
7m 54s	
Course Resources


## Networking in Google Cloud: Load Balancing

Welcome to Networking in Google Cloud	Module Watched	
1m 9s	
Hybrid Load Balancing and Traffic Management		
21m 31s	
Caching and Optimizing Load Balancing		
21m 15s	
Course Resources		
10s	
The trademarks and trade names of third pa

## Networking in Google Cloud: Hybrid and Multi-cloud (all use Internal IP addresses)

- Connectivity Options
  - Dedicated Interconnect 
    - at a colocation facility
    - dedicated, direct connection
    - 10 Gbps or 100 Gbps per link
    - steps: 
      - order ->
      - send LOA-CFA to the colocation facility ->
      - test connection -> 
      - create the VLAN attachment and establish BGP session ->
      - configure on-prem routers
    - MACsec: encrypts traffic
  - Partner Interconnect 
    - through a supported service provider
    - the physical connection is made
    - dedicated bandwidth
    - 50 Mbps or 50 Gbps per connection
    - use case:
      - unable to reach Google colocation facility 
      - on-prem/subnet/user - on-prem router - Partner peering edge - VPC/subnet/Router - VM
    - steps:
      - order ->
      - create a VLAN attachment -> 
      - request a connection form my service provider -> 
      - activate my connection -> 
      - configure on-prem routers
  - Cross-Cloud Interconnect 
    - to other google cloud providers directly
    - dedicated physical connection
    - 10 Gbps or 100 Gbps per connection
- Cloud VPN 
  - over the internet
  - encrypted tunnel
  - 1.5-3 Gbps per tunnel
  - need remote VPN gateway
  - use case:
    - VM -> cloud router(1) -> cloud edge router(2) -> cross cloud inter connect ->
      - other cloud: router(2) -> virtual router(1) -> VM
    - Hi-availability
      - VM -> cloud router (2) -> Google router (4) - other cloud router(4) - virtual router(1 or 2) -> VM

- Use Cases
  - faster and optimal data migration (secure:encryption)
    - on-prem/subnet/user --{cloud interconnect}--> Google/VPC/subnet/VM
    - subnet/user --{on-prem router}--colocation facility(Google Peering edge)--subnet/cloud router -- VM
      - BGP between two routers
      - establishing a VLAN attachment (linked with a cloud router)
      - the cloud router initiate a BGP session for both the VLAN
      - the cloud router receives routes advertized by the on-prem router
      - these router are integrated into my VPC network as custom dynamic routers 
      - also the cloud router advertises routes for Google Cloud ensuring bidirectional route exchange.
  - high availability with peering edge placement (99.99%)
    - create at least 4 interconnect connections, 2 in each metropolitan areas
    - in a metro, place 2 connections in different edge availability domains (routers in two zones)
    - one VM, two cloud router in different region, two Google Peering edge in a zone
      - a Cloud router with two interconnect
      - one on-prem router for Google Peering edge (total 4 on-prem routers),
      - one user on-prem 
      - each router maintaining its won independent Border Gateway Protocol (BGP session)
    - deploy a minimum of 2 Cloud Routers across at least 2 regions

- Cloud VPN
  - HA VPN topologies:
    - HA VPN supports site-to-site VPN for different configuration topologies
      - an HA VPN gateway to peer VPN devices
      - an HA VPN gateway to an AWS virtual private gateway
      - two HA VPN gateways connected to each other
      - HA VPN to Compute Engine VM instances 
    - HA VPN to VPN Peer gateway
      - resources(2) -> VPC routing - HA VPN gateway (and cloud Router) ->
        - VPN tunnels(2) (and BGP sessions) - internet -
        - on-prem VPN gateway (2) - on prem subnets/resources
      - each peer device has one interface and one external IP address
      - one tunnel to each peer device
      - HA VPN gateway - 4 tunnels (1 + 1 redundancy per resource) -> internet
      - Cloud Router - 4 BGP sessions -> internet (4 tunnels, 4 BGP sessions )
      - AWS gateway (2) -> AWS subnets
  - IPsec tunnel over the internet
  - Influencing the best path selection by setting a base priority
    - A Cloud Router advertises a route priority for each prefix to a BGP peer 
- Network Connectivity Center
  - configure network connectivity center as a transit hub
  - use case: Inter-VPC network connectivity 

## Logging and Monitoring in Google Cloud

Introduction		
2m 19s	
Introduction to Google Cloud Observability		
19m 23s	
Monitoring Critical Systems		
23m 59s	
Alerting Policies		
26m 33s	
Advanced Logging and Analysis		
33m 23s	
Working with Audit Logs		
14m 3s	
Course Summary		
43s	
Course Resources		
10s	
The trademarks and trade names of third parties m

## Observability in Google Cloud

Introduction	Module Watched	
1m 55s	
Configuring Google Cloud Services for Observability		
23m 0s	
Monitoring Google Cloud Network		
26m 5s	
Investigating Application Performance Issues		
17m 17s	
Optimizing the Costs for Google Cloud Observability		
18m 9s	
Course Summary		
51s	
Course Resources		
10s	
The trademarks and trade names of third 





## Lab

gcloud compute networks delete default



Hub

A hub is a global Google Cloud resource that supports multiple attached spokes. It provides a simple way to connect spokes together to enable data transfer across them. A hub can provide data transfer between different on-premises locations and a Virtual Private Cloud (VPC) network through its attached spokes.

Spoke

A spoke is a Google Cloud network resource connected to a hub. It is part of the hub, and can't be created without creating the hub first. A spoke routes traffic to remote network address blocks and enables the connection of multiple remote networks.

Spokes can be of one of the following types:

HA VPN tunnels
VLAN attachments
Router appliance instances that you or select partners deploy within Google Cloud