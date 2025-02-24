import blst

# TEST_SECRET_SEED
seed = b'{\xc8%\xdda\x83S\xeeCm\x028wx\xb6\xa4\x11\x01\x0c\x91\xe8\xb5"\xa6\x13\xd4K\xdao9\x0cy'
# use os.urandom(32)
# Keygen
tsk = blst.keygen(seed)
assert len(tsk) == 32
print(f"TEST SECRET KEY: {tsk.hex()}")

# Pubkey
pk = blst.pubkey(tsk)
print(f"TEST PUBLIC KEY: {pk.hex()}")
assert len(pk) == 48

# Signature
msg = b"hello world"
sig = blst.sign(tsk, msg)
print(f"TEST MESSAGE: {msg}")
print(f"SIGNATURE: {sig.hex()}")

# Verify

valid = blst.verify(pk, sig, msg)

print(f"VERIFIED SIGNATURE [OK]: {valid}")
assert valid is True


# Verify Bad signature
msg_bad = b"this is not the message you are looking for"

not_valid = blst.verify(pk, sig, msg_bad)

print(f"TEST MESSAGE (NOT VALID): {msg_bad}")
print(f"VERIFIED SIGNATURE [FAILS]: {not not_valid}")
assert not_valid is not True
