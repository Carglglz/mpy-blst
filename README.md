


## MicroPython bindings for BLST


This is a `USER_C_MODULE` for MicroPython using [blst](https://github.com/supranational/blst) library for BLS12-381 cryptography.


### API

`blst.keygen(seed)` --> `sk` : generates a secret key (`seed` must be at least 32 bytes)

`blst.pubkey(sk)` --> `pk`: derives the public key

`blst.sign(sk, msg)` --> `sig`:  generates a signature with a secret key 

`blst.verify(pk, sig, msg)` --> `bool`: returns `True` or `False` if the signature is verified or not. 

`blst.aggregate(sigA, sigB)` --> `aggregated_sig`: generates an aggregated signature

`blst.aggregate_verify([pubkey, ...], [message,...], aggregated_sig)` --> `bool`: verify the aggregated signature

`blst.keygen_dm_eip2333(seed)` --> `msk`: generates a master secret key

`blst.keygen_dc_eip2333(msk, child_index)` --> `csk`: derives a child secret key from master key with index `child_index`

### Tests

Tested ports:
 - unix (macos)
 - stm32 (pybV1.1)

In `./tests/` run `micropython test_blst.py`
```bash 
TEST SECRET KEY: 4ed2a0b9d018222922ac413d3f24e628233c2ce6dfd346a0f1f44289557e0455
TEST PUBLIC KEY: b3bcc6ac6091a73713218f9a3a9adba27e2a30e2a671140d18eda2862376e319f8d86ab91f0d6d9f8b8e546a61ad20d4
TEST MESSAGE: b'hello world'
SIGNATURE: abeb124cb3286065cf46971b4619074b5db17929e497a8cae5e7ce74de845f9e77b6301650beb21485abf3b2fa1c23fd042ddfbe1f5ae45e0ddb7f8a0270b1c37198e98fb0aef957930a56e4c4f150c3e565f17c051f08e2579c5c44c7a2dcee
VERIFIED SIGNATURE [OK]: True
TEST MESSAGE (NOT VALID): b'this is not the message you are looking for'
VERIFIED SIGNATURE [FAILS]: True
TEST MESSAGE A: b'hello'
SIGNATURE A: 8a65add4ee9b60dae29c6d711c4841df6d970bd13def135d8dffaf71f961ac2440fb67c95acdf6e97ff578b05585ea1111509d35b9f78157db402be77653cc6a456274bae115944589163eb2fbc25d436d8a315b260bb73ada8bf80b8768999d
TEST MESSAGE B: b'world'
SIGNATURE B: 872ef8cdb3f762eeb8af3502b42460a9cf4ee65a58a4ef326d1d8e02339bbfaaa50d60a26f46e0764fc0a66341a6da3f11a190934c0461896479fd9f313611327287a35fdf165a6ea070dd62eb47ba899d311ec5eea3a95e843aa8d3b440d5dc
VERIFIED SIGNATURES (A,B) [OK]
AGGREGATED SIGNATURE: acdda22efe6446754ed8e869c49b4e9aeff368b385481ba54a64a2aef10931dc3ec6700e01fa94b296b7d2b92924aa9a0c9ed133241512418403307dc7b47e335d40f91d6350c380b64dd3dff4cdf827da749301700ca6ee769a7594bc0c5675
AGGREGATED SIGNATURE VERIFIED: True
TEST MASTER SECRET KEY: 4ed2a0b9d018222922ac413d3f24e628233c2ce6dfd346a0f1f44289557e0455
TEST CHILD SECRET KEY: f6d55628883634b01a92a3884b377d73f45c87820af3ba8973bd64309006a661
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
