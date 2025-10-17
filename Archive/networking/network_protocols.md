# Protocols

HTTP, DNS, IP, BGP, TCP, UDP, FTP, ARP

Pizza Order

- DNS: phone book that translates the restaurant's name into its internet address
- IP: acts as a traffic controller, it ensures my request finds its way through the internet.
- TCP: when my order reaches, TCP double checks that it arrived correctly.
- HTTPS: keeps my credit card info safe.
- UDP: sends me quick updates of my order.

## What are protocols and why do we need them?

- What are protocols? 
  - Rules for communication between devices on a network
- Why do we need them?
  - To ensure devices can understand each other and work together
- Analogy:
  - Protocols are like languages and etiquette for computers
  - Just as humans need common languages and social rules, computers need protocols

## HTTP, HTTPS

- HTTP:
  - Fetches web pages when I type a URL
  - My browser sends an HTTP request to a web server
  - The server responds with the requested web page
  - The foundation of data exchange on the web
- HTTPS: 
  - Same as HTTP, but with added security
  - Encrypts the data exchanged between my browser and the web server

## DNS, IP

- DNS:
  - Translates human-related website names to IP addresses
  - The internet's phone book
- IP:
  - Ensures data reaches the correct destination on the internet
  - Assigns a unique address (IP address) to each device on a network
  - Routes data packets to their intended destination
  - The postal system for the internet
  - IPv4 (4 groups) and IPv6 (8 groups)
  
## TCP, UDP

- TCP:
  - Transmission control protocol
  - Provides reliable, ordered delivery of data
  - Breaks data into small packets
  - Numbers each packet
  - Checks for errors and missing pieces
  - Requests retransmission of lost packets
  - TCP is like a careful package handler
  - Ideal for applications where accuracy is crucial
- UDP:
  - User Data gram Protocol
  - Delivers data quickly, but less reliably than TCP
  - Sends data packets without checking if they arrive or arrive in order
  - Great for real-time applications like video streaming or online gaming
- Web Browsing:
  - DNS -> IP -> TCP -> HTTP/HTTPS

## FTP, SFTP

- FTP (File Transfer Protocol)
  - Move files between computers over a network
  - Establish a connection between two computers
  - Authenticate the user
  - Allows for uploading, downloading, and managing files
  - Basic FTP is not secure; consider using SFTP for sensitive files
- SFTP
  - Same as FTP, but with added security
  - Uses encryption to protect the entire file transfer session
  - Often uses SSH (Secure Shell) for authentication

## SMTP, POP3

- SMTP (Simple Mail Transfer Protocol)
  - My email client prepares the message
  - SMTP server receives the message and finds the recipient's server
  - Transfer the email to the recipient's server
  - SMTP only handles sending; other protocols handle receiving
- POP3 (Post Office Protocol version 3)
  - Retrieves emails from the server to my device
  - Works well with limited internet connectivity
  - Can be problematic if I use multiple devices to check email
- IMAP (Internet Message Access Protocol)
  - Manage emails on teh server
  - Connects to the email server
  - Sync the current state of my mailbox across all devices
  - Keeps messages on the server
  - Great for users who access email form multiple devices


## DHCP, SNMP, SSH, ICMP

- DHCP (Dynamic Host Configuration Protocol)
  - Automatically assigns IP addresses to devices on a network
  - Device joins network and request an IP address
  - DHCP server assigns an available IP address
  - Also provides other network configuration information
  - Simplifies network administration and prevents IP conflicts
- SNMP (Simple Network Management Protocol)
  - Monitors and manages network devices
  - Collects data from various network devices
  - Allow administrators to modify device settings remotely
  - Managing routers, switches, servers, printers, etc.
- SSH (Secure Shell)
  - Provides secure remote access to another computer
  - Establishes an encrypted connection between two computers
  - Allow command execution, file transfers, and tunneling
  - Essential for secure remote system administration
  - SSH can also be used to create secure tunnels for another protocols
- ICMP (Internet Control Message Protocol)
  - Tests network connectivity and reports errors
  - Send echo requests and listens for echo replies
  - Used by the "ping" command
  - Diagnosing network connectivity issues
  - ICMP is also used for the "traceroute" command to map network paths
- ARP (Address Resolution Protocol)
  - Finds the physical address (MAC) of a device on a local network
  - Devices needs to send data to an IP address on the local network
  - APR broadcasts a request asking "Who has this IP address?"
  - Device with that IP responds with its MAC address
  - Translates IP addresses to MAC addresses on a local network
  - Essential for communication on local networks
- RIP (Routing Information Protocol)
  - Determines the best path for data across a network
  - Routes share their routing tables with neighbors
  - Uses "hop count" to measure distance
  - Updates every 30 seconds
  - Simple to configure and implement
  - Good for small networks
  - Limited scalability due to hop count restriction
- OSFP (Open Shortest Path First)
  - Finds the best path for data within a network
  - Routers share information about the network topology
  - Calculates the shortest path to each destination
  - Commonly used in large enterprise networks
  - Quickly adapts to changes in network topology
- BGP (Border Gateway Protocol)
  - Manges routing between different networks
  - Exchanges routing and reachability information between autonomous systems
  - Makes routing decisions based on paths, network policies, and rule-sets
  - Critical for the functioning of the global internet
  - Called the Glue of the Internet


## Key Protocols

- HTTP/HTTPS
- DNS and IP
- TCP and UDP
- FTP and SFTP
- SMTP, POP3, IMAP

## Network Management and Security Protocols

## Review

- Web Browsing
  - DNS -> IP -> ICP -> HTTP/HTTPS
- Email
  - SMTP (sending) -> POP3/IMAP (receiving)
- File Transfer:
  - FTP/SFTP
- Network Management:
  - DHCP, SNMP
- Security:
  - SSH, SSL/TLS
- Diagnostics: 
  - ICMP, ARP
- Routing:
  - OSPF (internal), BGP (between networks)