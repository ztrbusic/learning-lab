# Cryptography

## Cryptography Basics
- symmetric encryption - same key for encryption and decryption
	- **DES** - Data Encryption Standard
	- **3DES** - Triple DES
	- **AES** - Advanced Encryption Standard
- asymmetric encryption - pair of keys - one for encryption, one for decryption
	- uses public and private key
	- **RSA**
	- slower
- basic math:
	- XOR operation - "exclusive OR"
	- Modulo operation

## Public Key Cryptography Basics
- **RSA** - based on factoring two prime numbers
- **Diffie-Hellman Key Exchange**

- `ssh -i privateKeyFileName user@host`
	- specifies a key for Linux OpenSSH
- `~/.ssh` - folder for keys
- **CA** - Certificate Authority
- **PGP** - Pretty Good Privacy
	- software that implements encryption
- **GPG** - GnuPG - open-source implementation of the OpenPGP standard
	- commonly used in emails
	- `gpg --import backup.key`
	- `gpg --decrypt message.gpg`

## Hashing Basics
- **MD5** - Message-Digest Algorithm 5
	- hexadecimal encodings: _md5sum_, _sha1sum_, _sha256sum, _sha512sum_
- hash collision - two different inputs give the same output
	- _pidgeonhole effect_
	- MD5 and SHA1 - considered not secure
- _password salting_
- Linux stores passwords in `/etc/shadow`
- hashed passwords are in format: `$prefix$option$salt$hash`
- prefix - specifies the hashing algorithm
	- `$y$`, `$gy$`, `$7$` etc.
- Windows passwords - hashed using NTLM
	- stored in SAM (Security Accounts Manager)
- **hashcat**
	- syntax: `hashcat -m <hash_type> -a <attack_mode> hashfile wordlist`
- **HMAC** - Keyed-Hash Message Authentication Code
	- for verification of authenticity and integrity of data

## John the Ripper: The basics
- P an NP - two classes of problems
	- **P** - Polynomial Time - problems whose solutions can be found in polynomial time
		- e.g. sorting a list
		- hashing
	- **NP** - Non-deterministic Polynomial Time - given solution can be checked quickly, but finding it can be hard
		- unhashing
- dictionary attacks

**Using John**
- `john -wordlist=[path to wordlist] [path to file]`
- `-format=[format]` - use specific hash format
- `unshadow`
- `--single` - Single Crack mode - word mangling
- `zip2john`
- `rar2john`
- `SSH2john`