# Cryptography Theory Cheatsheet

## Basics
- **Symmetric encryption** - same key for encrypt/decrypt
  - DES, 3DES, AES
- **Asymmetric encryption** - key pair (public/private)
  - RSA (slower, factoring primes)
- Math ops: XOR, Modulo

## Public Key
- **RSA** - based on factoring primes
- **Diffie-Hellman** - key exchange
- **CA** - Certificate Authority
- **PGP** - Pretty Good Privacy (encryption software)
- **GPG** - GnuPG (OpenPGP implementation)
  - `gpg --import backup.key`
  - `gpg --decrypt message.gpg`
- **SSH keys**
  - `ssh -i privateKey user@host`
  - Keys stored in `~/.ssh`

## Hashing
- **MD5, SHA1** - broken (collisions)
- **SHA256, SHA512** - secure (for now)
- Hash collisions = pigeonhole effect
- **Salting** - adds randomness to hashes
- **Linux passwords** - `/etc/shadow` → `$prefix$option$salt$hash`
- **Windows passwords** - NTLM, stored in SAM
- **Hashcat** - crack hashes
  - `hashcat -m <hash_type> -a <attack_mode> hashfile wordlist`
- **HMAC** - Hash + Key for authenticity/integrity