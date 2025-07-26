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
