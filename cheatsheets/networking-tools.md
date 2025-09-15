# Networking Tools Cheatsheet

## Tcpdump
- `tcpdump` - start capture
- Filters:
  - `host <IP>` | `port <PORT>` | `tcp`
  - use `and`, `or`, `not`
- Display: `-q`, `-e`, `-A`, `-xx`, `-X`

## Nmap
- `nmap 192.168.1.0/24` - scan subnet
- `-sL` - list hosts
- `-sn` - ping scan (no services)
- `-sT` - connect scan
- `-sS` - SYN (stealth) scan
- `-sU` - UDP scan
- `-O` - OS detection
- `-sV` - service version detection
- `-A` - aggressive (OS, services, traceroute)
- Timing: `-T0`..`-T5`
- Verbose: `-v`, Debug: `-d`

## Other
- `telnet <host> <port>` - test remote connection
- `whois <domain>` - domain registry info