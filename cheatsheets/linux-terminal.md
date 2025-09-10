# Linux Cheatsheet

## Terminal Commands:
- `ls` - list files and directories, use `ls -la` to list hidden
- `cat` - **concatenate** - read files in order and can output them to another, e.g. `cat file1.txt file2.txt > combined.txt`
- `pwd` - print working directory
- `find` - finds files, lot of options
- `grep` - searches **inside** files
- `touch` - create empty files
- `mkdir` - create empty directory
- `rm` - removes directories and files, use `rm -r` to delete not empty directories
- `cp` - copies stuff
- `mv` - move or rename files/directories
- `file` - describes the file
- `su` - login as another user in the current environment
- `su -l` - login as another user but in their own environment

## Operators:
- `&` - puts the command in background immediately, e.g. `firefox &`
- `&&` - runs the second command only if the first succeeded (`command 1 && command2`)
- `>` - redirect output and **overwrite**
- `>>` - redirect output and **append**

## Switches/Options/Flags:
- `-a`, `-all` - show all (options, files etc. )
- `--help` - show usage for a command

## System directories:
- `/etc` - system configuration files
- `/var` - variable data (logs, caches, databases)
- `/root` - home directory for root user
- `/tmp` - temporary files, cleared on reboot, world-writable

## Tools:
- `nano` - text editor
- `vim` - advanced text editor
- `wget` - download files via HTTP
- `scp` - secure copy (using SSH)
- `apt` - Advance Package Tool - also gets updated

## Process Management:
- **kernel** - talkes to hardware, schedules processes, manages memory...
- **PID** - Process ID
- **CTRL + Z** - put running process in background
- `ps` - displays processes
- `ps aux` - displays processes from other users and system processes
- `top` - real-time process statistics
- `kill` - terminate process
- `systemctl` - interact with the **systemd** process
- `fg` - make process run in foreground again
- `cron` - schedule tasks