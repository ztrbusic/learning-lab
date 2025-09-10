# Windows CMD Cheatsheet

## General
- `command /?` - show help for a specific command (e.g. `ipconfig /?`)
- `cls` - clear screen
- `set` - see path and details
- `ver` - see Windows version
- `systeminfo` - see system details
- `| more` - enables flipping through long inputs
- `dir /a /s` - list files (with attributes, recursive - goes down through all subfolders)
- `tree` - display folder structure
- `mkdir` - create new directory
- `rmdir` - remove directory
- `type` - display contents of a text file
- `copy` - copy file(s) from one location to another
- `move` - move or rename file(s)
- `del` - delete file(s)
- `erase` - delete file(s) (same as `del`)

## Networking
- `hostname` - show computer’s hostname
- `whoami` - show current user
- `ipconfig` - show network configuration (IP, mask, gateway), more info with `ipconfig /all`
- `netstat` - list active network connections + ports
- `net` - manage users, shares, services
- `net help` - help for net subcommands
- `ping`
- `tracert` - traces the network route
- `nslookup` - looks up domain or host and returns IP address

## Tools
- `WF.msc` - open Windows Firewall snap-in
- `control /name Microsoft.WindowsUpdate` - open Windows Update settings