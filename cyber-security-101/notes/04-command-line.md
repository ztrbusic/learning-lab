# Command Line

## Windows Command Line
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

## Windows PowerShell
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
- **IOC** - indicator of compromise
	- `Invoke-Command`

## Linux Shells
- when interacting with a shell, I need to be in the directory where I want to perform operations
- **Bash** - Bourne Again Shell
	- scripting capabilitie
- **Fish** - Friendly Interactive Shell
- **Zsh** - Z Shell
- **scripting**
	- every script starts with _shebang_ - e.g. `#!/bin/bash`
	- `chmod` - give permission to script