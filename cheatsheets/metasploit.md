# Metasploit Cheatsheet

## Msfconsole Basics
- `msfconsole` - main CLI
	- supports `ping`, `clear`, `help`, `history`
	- `show options` - exploit options
	- `show payloads` - lists usable payloads
	- `back` - exits the exploit context
	- `info` - module information
	- `search` - search for exploits etc (e.g. `search ms17-010`)

## Parameters and Sessions
- `set PARAMETER_NAME VALUE`
	- `RHOSTS`, `RPORT`, `PAYLOAD`, `LHOST`, `LPORT`, `SESSION`
- `unset` - removes parameter
- `unset all` - removes all parameters
- `setg` - set global -> `unsetg`
- `exploit` - same as `run`
- `check` - some modules, checks the system for vunerabilities
- `background` - puts session in background, also **CTRL+Z**
- `sessions` - shows active sessions, also `sessions -i NUM`

## Port Scanning
- `search portscan` - lists port scanning modules
- port scanner module key options:
 - `CONCURRENCY` - no. of simultaneous goals
 - `PORTS` - port range
 - `RHOSTS` - target network
 - `THREADS` - no. of threads, more = faster scanning
- `scanner/discovery/udp_sweep` - fast UDP services scan (DNS, NetBIOS, etc.)
- `scanner/smb/smb_version` - specific service scanner

## Msfvenom
- `msfvenom` - generated payloads
	`--list formats`

## Meterpreter
- `getpid` - ID of Meterpreter process 
- `ps` - lists all active processes
- multiple versions:
	- `msfvenom --list payloads | grep meterpreter`
- `help` - list all commands
- some helpful commands: `getuid`, `migrate`, `hashdump`, `search`, `shell`