# Hydra Cheatsheet

- `hydra -l user -P passlist.txt ftp://IP_ADDRESS` - for FTP password cracking
- `hydra -l USERNAME -P FULL_PATH_TO_PASSLIST IP_ADDRESS -t 4 ssh` - for SSH connection password cracking
	- `-t` - number of threads
- `sudo hydra USERNAME WORDLIST IP_ADDRESS http-post-form "PATH:LOGIN_CREDENTIALS:INVALID_RESPONSE"` - for web forms cracking
	- `http-post-form` - for POST, not e.g. GET requests
	- `PATH` - login page URL, `/` - for homepage
