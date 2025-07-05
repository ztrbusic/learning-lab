# Windows and AD Fundamentals

- Windows notes:
	- **NTFS** - New Technology File System
	- **FAT** - File Allocation Table
	- **HPFS** - High Performance File System
	- **ADS** - Alternate Data Streams - file attribute in NTFS ($DATA)
	- **WMI** - Windows Management Instrumentation
	- **VSS** - Volume Shadow Copy Service
- `cmd` commands:
	- `hostname`, `whoami`, `ipconfig`, `netstat`, `net`, `net help`
	- `/?` - command to retrieve help manual for a command (e.g. `ipconfig /?`)
	- `cls` - clear command prompt screen

- Windows advanced notes:
	- `control /name Microsoft.WindowsUpdate`
	- firewall
		- **domain** - networks where the host can authenticate to domain controller
		- **private** - private or home networks
		- **public** - e.g. WiFi hotspots, airports etc.
		- `WF.msc`

- Windows Active Directory:
	- **Domain Controller**
	- **Active Directory Domain Service (AD DS)**
	- Users - **security principals**
	- Group Policy Management
	- **GPO** - Group Policy Objects
		- collection of settings for OUs
		- configures only computers or users
	- **SYSVOL** - network share for GPO distribution

- Protocols for network authentication on Windows:
	- **Kerberos** - new
	- **NetNTLM** - legacy

- **Kerberos**
	- assigns tickets
	- **KDC** - Key Distribution Center - installed on the Domain Controller
	- **TGT** - Ticket Granting Ticket
	- **TGS** - Ticket Granting Service

- **NetNTLM**
	- works using challenge-response system

- **trees** - domains can be split, e.g. _thm.local_ can be split into _uk.thm.local_ and _us.thm.local_
- **Enterprise Admin** - he who controls the entire enterprise network (all uk., us. etc)
- **forest** - different namespaces e.g. _THM_ and _MTH_