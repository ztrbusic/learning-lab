# Networking Concepts

- **OSI model** - Open Systems Interconnection
	- developed by ISO
	- _Please Do Not Throw Spinach Pizza Away_
	- conceptual model

- OSI layers:
1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

- **1. Physical**
	- _layer 1_
	- medium: electrical, optical or wireless
	- definition of binary digits 0 and 1
- **2. Data Link**
	- protocol that enables data transfer
	- e.g. Ethernet (802.3), WiFi (802.11)
		- addresses have six bytes - MAC address (Media Access Control)
			- expressed in hexadecimal format: _a4:c3:f0:85:ac:2d_
				- each two hexadecimal digits are one byte
<p align="center">
<img src="../assets/images/01-OSI-layer-2.png" alt="OSI model Layer 2" width="40%">
</p>

- **3. Network**
	- sending data between different networks
	- examples:
		- **IP** (Internet Protocol), **ICMP** (Internet Control Message Protocol)
		- VPN protocols: **IPSec** and **SSL/TLS**
- **4. Transport**
	- enables end-to-end communication between applications on hosts
	- examples: **TCP** (Transmission Control Protocol) and **UDP** (User Datagram Protocol)
- **5. Session**
	- establishing, maintaining and syncronising communication between applications on hosts
	- examples: **NFS** (Network File System) and **RPC** (Remote Procedure Call)
- **6. Presentation**
	- ensures the data is delivered in a form the application layer can understand
	- data encoding, compression, encryption
- **7. Application**
	- provides network services directly to end-user applications
	- **HTTP**, **FTP**, **DNS**, **POP3**, **SMTP**, **IMAP**

- **TCP/IP model**
	- implemented model
	- developed in the 1970s by the Department of Defense
	- allows a network to continue to function even if parts of it are out of function
	- routing protocols adapt as the network topology changes
	- **4(5) layers**
		- Application layer (from OSI: application, presentation session)
		- Transport layer (from OSI: layer 4)
		- Internet layer (from OSI: layer 3)
		- Link layer (OSI: layer 2)
		- (some textbooks also include physical layer as no. 5)
	- **IP address**
		- four octets, 32 bits (one 8-bit allows to represent a decimal number between 0 and 255)
		- 192.168.1.0 - network address
		- 192.168.1.255 - **broadcast** address - sending to the broadcast targets all hosts on the network
		- **subnet mask** (255.255.255.0 or /24 or, on Mac, 0xffffff00)
		- **private** IP addresses ranges:
			- `10.0.0.0` - `10.255.255.255`
			- `172.16.0.0` - `172.31.255.255`
			- `192.168.0.0` - `192.168.255.255`
- **UDP and TCP**
	- UDP 
		- allows to reach specified process on the target host
		- operates on layer 4
		- does not provide delivery information (greater speed)
	- ports - range between 1 and 65535, port 0 is reserved
	- TCP
		- connection-oriented
		- three-way handshake - SYN, SYN-ACK and ACK
- **encapsulation**
	- layers adding headers
- `telnet` - Teletype Network - remote terminal connection

# Networking Essentials

- **DHCP** - Dynamic Host Configuration Protocol
	- application level protocol that relies on UDP
	- steps - **D O R A** - Discover, Offer, Accept Acknowledge
- **ARP** - Address Resolution Protocol - enables to find MAC addresses of another devices on the Ethernet
- **ICMP** - Internet Control Message Protocol - network diagnostics and error reporting
	- `ping` and `traceroute`
- **Routing**
	- _OSPF_ - routing protocol that enables users to share information on the network topology and calculates the most efficient path for data transmission.













