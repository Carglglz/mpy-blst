import os
import blst

# Keygen
sk = blst.keygen(os.urandom(32))
print(f"NEW SECRET KEY: {sk.hex()}")

# Pubkey
pk = blst.pubkey(sk)
print(f"NEW PUBLIC KEY: {pk.hex()}")

# Signature
msg = b"hello world"
sig = blst.sign(sk, msg)

print(f"SIGNATURE: {sig.hex()}")

# Verify

valid = blst.verify(pk, sig, msg)

print(f"VERIFIED SIGNATURE [OK]: {valid}")
assert valid is True


# Verify Bad signature
msg_bad = b"this is not the message you are looking for"

not_valid = blst.verify(pk, sig, msg_bad)

print(f"VERIFIED SIGNATURE [FAILS]: {not not_valid}")
assert not_valid is not True
