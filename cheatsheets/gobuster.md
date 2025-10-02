# Gobuster Cheatsheet

- `gobuster --help`
- `dir`, `dns`, `vhost`
- useful flags:
	- `-t` - threads
	- `-w` - wordlist
	- `-o` - output
	- `--delay`
	- `--debug`
	- `-u` - target URL

- `dir` flags:
	- `-c` or `--cookies` - pass a cookie
	- `-x` or `--extensions` - which extensions to scan for
	- `-H` or `--headers` - pass a header
	- `-k` or `--no-tls-validation` - skip https certificatate
	- `-n` or `--no-status` - stop printing all status messages
	- `-P` or `password` - send password (if I have it)
	- `-s` or `--status-codes` - which status codes do I want to see
	- `-b` or `--status-codes-blacklist` - which status codes I don't want to see
	- `-U` or `--username` - for auth
	- `-r` or `--followredirect` - if server redirects - follow

- `dns` flags:
	- `-c` or `--show-cname` - shows CNAME records
	- `-i` or `--show-ips` - show resolved IPs
	- `-r` or `--resolver` - configures custom DNS for resolving
	- `-d` or `--domain` - which domain I want to enumerate

- `vhost` flags:
	- `-u` or `--url` - base URL
	- `--append-domain` - appends domain onto wordlist
	- `-m` or `--method` - GET, POST, etc.
	- `--domain` - appends domain onto wordlist
	- `--exclude-lenght`
	- `-r` or `--follow-redirect`