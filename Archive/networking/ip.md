# Protocols

## Public and Private IPs

- IPv4: 4.3 billion
- LAN: use private IPs
  - 192.168.0.0 to 192.168.255.255
  - 10.0.0.0 to 10.255.2
  - 172.16.0.0 - 172.16.255.255
  - ipconfig
- To communicate over internet
  - private IP address should be translated 
  - Network Address Translation (NAT)
  - my device (private ip) -> router (private ip) - public ip - internet
  - NAT device records machine and its private ip -> convert public ip of router?
  - response comes -> check the table -> return to the original device



## DHCP

- Dynamic Host Configuration Protocol
- IP addresses -> DHCP server -> Router -> devices (assign dynamic ips)

## IP Packet Header

- Version, IHL, Type of Service, Total Length,
- Identification, Flags, Fragment Offset,
- Time to Live, Protocol, Header Checksum,
- Source Address,
- Destination Address,
- Options, Padding

## TCP header

- Source Port Number, Destination Port Number,
- Sequence Number, 
- Acknowledgement Number,
- Header Length, Reversed, URG,ACK,PSH,RST,SYN,FIN, Window Size,
- TCP Checksum, Urgent Pointer,
- Options,
- Data


## Three-way Handshake

- client -(syn)-> server
- client <-(syn/ack)- server



## UDP (User Datagram Protocol)

## ARP (Address Resoultion Protocol) - within a network

- Check MAC address?
- ARP table
  - interface, IP address, Physical Address, Type, Expiry
- device 1 communicates device 2
- if cannot find mac address then
- broadcast - ask who as ip address of <address>
- the device 2 see this message and responds
- i have ip address <address> and my MAC address is <address>