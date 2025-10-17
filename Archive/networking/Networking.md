# Networking

## LAN, Ethernet, MAC address, 

CSMA: carrier sense multiple access: 
Carrier, bandwidth, collision, 
random period waiting, 
exponential backoff, 
collision domain, 
internet,
routing: 
circuit switching: 
message switching: several stops, 
hop count: the number of hops a message takes along a route.
routing problem: hop count.
Hop Limit:
big transmissions into small packets.
each packet contains a destination address on the network.
so routes know where to forward them.

the format is defined by the Internet Protocol.IP
TCP/IP: 
different packets from the same message take different routes though a network.
-> packets arriving out of order -> TCP/IP handles this.
packet switching?
ICMP: internet control message protocol 
BGP: border gateway protocol 

LAN: Local Area Network

- My Home (LAN1)
- Router
  - Desk top,
  - Phone,
  - Laptop
- Network Interface Card (NIC)
  - Talk and Listen
- WAN (Wide Area Network)
  - Router (bigger?)
    - Router: machines
    - Router: machines
    - Router: machines
- MAC Address:
  - 6 bytes (48 bits) long 
- Computers Talking
  - Share medium (cable)
  - computer(NIC card) <-> Medium 
  - computer send message
    - its own MAC address
    - destination MAC address
    - message
  - all computers connected to that medium can listen
    - they check the receiver address and take it or ignore it.
- Collision Detection and Avoidance:
  
Terms

- VPN, IP, DNS, DHCP, NAT, VLAN, Routers, Firewall, 
- Switches, MAC, OSI model (7 Layers)
- WAN, Internet, 
- MAC address, 48 bit (6 bytes) <-> Data Link Layer
- NIC, 
- ARP: map IP and MAC, ARP request to find the recipient's MAC address.
- Routes rely on Mac address for communication within local networks.
- ICMP: error reporting and diagnostic purposes. 
  - ping command to checks if the device is reachable and measures latency.
- VOIP: voice communication 
- LAN:
- Load balancing:
- MFC: short distance
- MPLS: 
- SD-WAN: 
- PROXY server: 
- BGP: optimal route
- QOS: priority
- 

OSI Model

- Physical Layer: physical transmission of data over media.
- Data Link Layer: reliable communication between two devices by managing Mac address and data frames.
- Network Layer: route data to the correct destination based on IP address.
- Transport Layer: ensures reliable end to end communication providing flow control and error correction.
- Session Layer: manges sessions and maintains the state of communication.
- Presentation Layer: formats and encrypts data for the application layer.
- Application Layer: 