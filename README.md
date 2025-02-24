


## MicroPython bindings for BLST


This is a `USER_C_MODULE` for MicroPython using [blst](https://github.com/supranational/blst) library for BLS12-381 cryptography.


### API

`blst.keygen(seed)` --> `sk` : generates a secret key (`seed` must be at least 32 bytes)

`blst.pubkey(sk)` --> `pk`: derives the public key

`blst.sign(sk, msg)` --> `sig`:  generates a signature with a secret key 

`blst.verify(pk, sig, msg)` --> `bool`: returns `True` or `False` if the signature is verified or not. 

### Tests

Tested ports:
 - unix (macos)
 - stm32 (pybV1.1)

In `./tests/` run `micropython test_blst.py`
```bash 
TEST SECRET KEY: 4ed2a0b9d018222922ac413d3f24e628233c2ce6dfd346a0f1f44289557e0455
TEST PUBLIC KEY: b3bcc6ac6091a73713218f9a3a9adba27e2a30e2a671140d18eda2862376e319f8d86ab91f0d6d9f8b8e546a61ad20d4
TEST MESSAGE: b'hello world'
SIGNATURE: 87b87831e4ac4216a474a9cc9e010cd11f0a32688b5b715a1023da2c8782a93c95f979b37878663739390947373b399514d8f0013c479733e81d72a09d133a4726bef9bd5c177cc7ab7cb37c4a49c9663b55a724e32bf464b705081c08a02e28
VERIFIED SIGNATURE [OK]: True
TEST MESSAGE (NOT VALID): b'this is not the message you are looking for'
VERIFIED SIGNATURE [FAILS]: True

```

or run MicroPython test suite e.g. :
```bash
$ ./run-tests.py ../../user_modules/mpy-blst/tests/*.py -r .

platform=darwin arch=x64
pass  ../../user_modules/mpy-blst/tests/test_blst.py
1 tests performed (7 individual testcases)
1 tests passed

```

### References


[IETF-BLS](https://www.ietf.org/archive/id/draft-ietf-cose-bls-key-representations-04.html)
