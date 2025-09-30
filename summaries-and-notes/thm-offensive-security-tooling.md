# Offensive Security Tooling - Summary

- **Hydra** - A fast online password-cracking tool for performing brute-force and dictionary attacks against network services and protocols.  
- **Gobuster** - A tool for enumerating directories, DNS records, and virtual hosts. It uses wordlists to brute-force paths and hosts; essential for web-app reconnaissance.  
- **Shell types & listeners** - Common shell techniques and helpers:  
  - **Reverse shell (connect-back)** - The compromised host initiates a connection back to the attacker. The attacker accepts the connection by _listening_ (e.g., with `netcat`).  
  - **Bind shell** - Binds a shell to a port on the target and waits for an incoming connection. Less commonly used because it requires an externally reachable port and is easier to detect.  
  - **Advanced listeners / helpers** - Tools that improve interactivity and reliability: `rlwrap`, `ncat`, and `socat`.  
- **SQLMap** — An automated tool for detecting and exploiting SQL injection vulnerabilities and interacting with vulnerable databases.