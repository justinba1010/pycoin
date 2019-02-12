# Transaction

## Transactions
---
* Header 2 bytes
* Inputs - 64 bytes each
  * First 32 bytes -> tx-id of input
  * Second 32 bytes -> address of using input
* Outputs - 64 bytes each
  * First 32 bytes -> address of output
  * Second 32 bytes -> amount being sent(64 bits unsigned, should be maxed out at 0x8000000000000000, this was a major bug in Bitcoin, with negatives passing the tx verification, but it would actually create a lot of bitcoin for the addressholder) if I remember this bug came out in like 2010/2011, and it was patched very fast.
    * This gives us an upper limit of 9223372036854775808 denominations with 63 bits
* Signatures
  * Each input appends its signature of the hash(SHA256) of the unsigned serialization
* Signed Serialization
  * Each signature is 64 bytes in the order of the inputs
    * First 32 bytes is the r to the signature
    * Second 32 bytes is the s to the signature
  * It is appended to the end of the serialization to make a valid tx


## Serialized Unsigned Transactions
---
* 1 byte -> number of inputs
* 1 byte -> number of outputs
* 64 bytes -> each input
* 64 bytes -> each output

## Serialized Signed Transaction
---
* Serialized tx
* 8 bytes -> each signature of the hash of the serialized tx in the order of inputs
