# Networking Theory Cheatsheet

## OSI Model
- **Mnemonic** - Please Do Not Throw Spinach Pizza Away
1. Physical - wires, wireless, bits
2. Data Link - Ethernet (802.3), Wi-Fi (802.11), MAC address
3. Network - IP, ICMP, VPN (IPSec, SSL/TLS)
4. Transport - TCP, UDP
5. Session - NFS, RPC
6. Presentation - encoding, compression, encryption
7. Application - HTTP, FTP, DNS, SMTP, IMAP

## TCP/IP Model
- Layers: Application, Transport, Internet, Link (+ Physical in some books)
- IPv4: 32-bit, 4 octets
  - Network: `192.168.1.0`
  - Broadcast: `192.168.1.255`
  - Subnet mask: `255.255.255.0` or `/24`
- Private ranges:
  - 10.0.0.0/8
  - 172.16.0.0 – 172.31.255.255
  - 192.168.0.0/16

## TCP vs UDP
- **UDP** - fast, no delivery guarantee, ports 1–65535
- **TCP** - connection-oriented, 3-way handshake (SYN → SYN-ACK → ACK)

## Essentials
- **DHCP** - Dynamic IP assignment (DORA: Discover, Offer, Request, Acknowledge)
- **ARP** - IP ↔ MAC resolution
- **ICMP** - diagnostics (`ping`, `traceroute`)
- **NAT** - Network Address Translation

## Routing Protocols
- OSPF - link state, efficient
- EIGRP - Cisco proprietary
- BGP - internet backbone
- RIP - small networks

## Core Protocols
- **DNS** (L7) - A, AAAA, CNAME, MX
- **HTTP(S)** - GET, POST, PUT, DELETE | Ports: 80/443
- **FTP** - USER, PASS, RETR, STOR | Port 21
- **SMTP** - HELO, MAIL FROM, RCPT TO, DATA, . | Port 25
- **POP3** - Port 110
- **IMAP** - Port 143

## Secure Protocols
- TLS/SSL - encryption layers
- SSH - Secure Shell (port 22)
  - **SFTP** - file transfer over SSH