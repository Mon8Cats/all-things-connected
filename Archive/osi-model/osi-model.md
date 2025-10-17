# OSI model

## Terms for the information at different stages 

- Application, Presentation, Session Layers
  - pass the raw data
- Transport Layer
  - data into segments (TCP) or datagrams (UDP)
  - header (port number, sequence number) + payload
- Network Layer
  - packet
    - header (IP addresses)
    - payload: (segment or datagram)
- Data Link Layer
  - frame:
    - header (MAC addresses)
    - payload (packet)
    - trailer (error checking logic)
- Physical Layer
  - a stream of raw bits <- frame
  - sender over the physical medium
- Physical Layer
  - receiving the raw bits
  - a frame < - raw bits
- Data Link Layer
  - frame trailer : verify the frame's integrity
  - frame header : check the destination MAC address
  - frame payload -> a packet
- Network Layer
  - packet header: check IP address
  - packet payload -> a segment
- Transport Layer
  - segment header -> sequence number
  - assemble segment payload in order 
- Application Layer
  - the original data -> the receiving application


## Protocols used in each layer

- Application Layer
  - HTTP/HTTPS, FTP, SMTP, DNS, Telnet/SSH
- Presentation Layer
  - SSL/TLS, MIME, JPEG, MPEG, GIF
- Session Layer
  - NetBIOS, RPC, PPTP
- Transport Layer
  - TCP, UDP
- Network Layer
  - IP, ICMP, OSPF/BGP
- Data Link Layer
  - Ethernet, PPP, Wi-Fi, MAC
- Physical Layer
  - Ethernet cables, USB, Bluetooth, Fiber Optics