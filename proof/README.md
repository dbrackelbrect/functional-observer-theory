# Authorship Proof

This folder contains cryptographic proof of authorship for the Functional Observer Theory papers, authored under the pseudonym David Brackelbrect.

## Files

- `authorship.txt`  
  A declaration of authorship and the hash of the original `.tex` source files.

- `authorship.txt.sig`  
  A detached GPG signature of `authorship.txt`, signed with the Brackelbrect PGP private key.

- `Brackelbrect-public.asc`  
  The corresponding PGP public key (ASCII-armored) used to verify the signature.

## Verification

To confirm authorship and integrity, run:

```bash
gpg --import Brackelbrect-public.asc
gpg --verify authorship.txt.sig authorship.txt
