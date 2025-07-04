# Cyber Security 101 - notes

## 2025-06-27
- `dirb` - web content scanner, brute forces hidden directories and files by guessing common names from a wordlist
- **DFIR** - Digital Forensics and Incident Response
- **SIEM** - Security Information and Event Management
- Useful web search engines:
	- **Shodan** - devices
	- **Censys** - hosts, websites etc.
	- **VirusTotal** - virus scanning
	- **Have I Been Pwned (HIBP)** - email checkup
	- **Common Vunerabilities and Exposures (CVE)** - dictionary of vunerabilities
	- **Exploit Database** - code for exploiting vunerabilities
- Linux commands:
	- `ls`, `cd`, `cat`, `pwd`, `find`, `grep`
	- `touch`, `mkdir`, `rm`, `cp`, `mv`, `file`
	- `su` - login as another user in the current environment
	- `su -l` - login as another user but in their own environment
- Linux operators:
	- `&`, `&&`, `>`, `>>`
- Linux switches:
	- `-a`, `-all`, `--help`
- Linux system directories:
	- **/etc** - system files
	- **/var** - data frequently accessed/written by services or applications
	- **/root** - root user folder
	- **/tmp** - "temporary", temp data only used onece or twice, wiped out after restart, useful for pentesting as any user can write to it

## 2025-06-28
- Linux tools:
	- `nano` - text editor
	- `vim` - advanced text editor
	- `wget` - download files via HTTP
	- `scp` - secure copy (using SSH)
	- `apt` - Advance Package Tool - also gets updated
- Linux process management:
	- **kernel** - talkes to hardware, schedules processes, manages memory...
	- **PID** - Process ID
	- `ps` - displays processes
	- `ps aux` - displays processes from other users and system processes
	- `top` - real-time process statistics
	- `kill` - terminate process
	- `systemctl` - interact with the **systemd** process
	- **CTRL + Z** - put running process in background
	- `fg` - make process run in foreground again
	- `cron` - schedule tasks

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

## 2025-07-04
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
- **CLI**
	- `set` - see path and details
	- `ver` - see Windows version
	- `systeminfo` - see system details
	- `| more` - enables flipping through long inputs
	- `cls` - clean screen
	- `ipconfig` - network information, more info with `ipconfig /all`
	- `ping`
	- `tracert` - traces the network route
	- `nslookup` - looks up domain or host and returns IP address
	- `netstat` - displays current network connections and listening ports
	- working with files:
		- `cd`, `dir /a /s`, `tree`, `mkdir`, `rmdir`
		- `type`, `copy`, `move`, `del`, `erase`
		- `tasklist`
- **PowerShell**
	- CLI + scripting language on .NET framework
	- object-oriented
	- _cmdlet_ - command-lets - PS commands
	- _Verb-Noun_ - form for commands
	- `Get-Alias`
	- `Get-ChildItem` - like `dir` or `ls`
	- `Set-Location -Path ".\Documents"` - like `cd`
	- `New-Item -Path " " -ItemType " "`
	- `Remove-Item` - similar to above and `rmdir` and `del`
	- `Copy-Item`, `Move-Item`
	- `Get-Content` - like `type` and `cat`
	- `|` - **Piping** - allows the output of one command to be used as input of another
		- e.g. - `Get-ChildItem | Sort-Object -Lenght`
		- e.g. - to get just .txt files - `Get-ChildItem | Where-Object -Property "Extension" -eq ".txt"`
	- `Select-String` - similar to `grep` and `findstr`
		- supports _regex_
	- `Get-ComputerInfo`
	- `Get-LocalUser`
	- `Get-NetIPConfiguration` - like `ipconfig`
	- `Get-Process,`, `Get-Service`, `Get-NetTCPConnection`
	- `Get-FileHash`




































