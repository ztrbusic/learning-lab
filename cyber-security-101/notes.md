# Cyber Security 101 - notes

## 27-06-2025
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

## 28-06-2025
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

- Windows notes
	- **NTFS** - New Technology File System
	- **FAT** - File Allocation Table
	- **HPFS** - High Performance File System