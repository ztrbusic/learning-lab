# Windows PowerShell Cheatsheet

## Basics
- **PowerShell** - CLI + scripting language built on .NET
- Object-oriented (works with objects, not plain text)
- **Cmdlet** - small commands in PowerShell
- Commands use **Verb-Noun** format (e.g. `Get-Process`)

## Core Commands
- `Get-Alias` - list command aliases
- `Get-ChildItem` - list files/folders (like `dir` or `ls`)
- `Set-Location -Path ".\Documents"` - change directory (like `cd`)
- `New-Item -Path "<path>" -ItemType "<type>"` - create new item (file/dir)
- `Remove-Item` - delete item (like `del` or `rmdir`)
- `Copy-Item` - copy item(s)
- `Move-Item` - move/rename item(s)
- `Get-Content` - show file contents (like `type` or `cat`)

## Piping
- `|` - pass output of one command as input to another
  - `Get-ChildItem | Sort-Object -Length`
  - `Get-ChildItem | Where-Object -Property "Extension" -eq ".txt"`

## Searching
- `Select-String` - search inside files (supports regex, like `grep` or `findstr`)

## System Info & Networking
- `Get-ComputerInfo` - detailed system info
- `Get-LocalUser` - list local users
- `Get-NetIPConfiguration` - network config (like `ipconfig`)
- `Get-Process` - list processes
- `Get-Service` - list services
- `Get-NetTCPConnection` - list active TCP connections

## Security
- `Get-FileHash` - calculate file hash
- **IOC** - Indicator of Compromise (forensics term)
- `Invoke-Command` - run commands remotelys