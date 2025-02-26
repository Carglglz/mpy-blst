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

# -- Aggregation ---

# Signature A
msgA = b"hello"
sigA = blst.sign(tsk, msgA)
print(f"TEST MESSAGE A: {msgA}")
print(f"SIGNATURE A: {sigA.hex()}")


# Signature B
msgB = b"world"
sigB = blst.sign(tsk, msgB)
print(f"TEST MESSAGE B: {msgB}")
print(f"SIGNATURE B: {sigB.hex()}")

vs = blst.verify(pk, sigA, msgA) and blst.verify(pk, sigB, msgB)
res = "OK" if vs else "FAIL"
print(f"VERIFIED SIGNATURES (A,B) [{res}]")

assert vs is True

agg_sig = blst.aggregate([sigA, sigB])
print(f"AGGREGATED SIGNATURE: {agg_sig.hex()}")
pks = [pk, pk]
msgs = [msgA, msgB]

# Aggregate Verification
print(f"AGGREGATED SIGNATURE VERIFIED: {blst.aggregate_verify(pks, msgs, agg_sig)}")

# Master Key (EIP2333)
mk = blst.keygen_dm_eip2333(seed)

assert len(mk) == 32
print(f"TEST MASTER SECRET KEY: {mk.hex()}")


# Child Key (EIP2333) # INDEX 42
ck = blst.keygen_dc_eip2333(mk, 42)

assert len(ck) == 32
print(f"TEST CHILD SECRET KEY: {ck.hex()}")
