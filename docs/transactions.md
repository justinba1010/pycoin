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
  * First 32 bytes public x
  * Second 32 bytes public y
  * Third 32 bytes signature r


## Serialized Unsigned Transactions
---
* 1 byte -> number of inputs
* 1 byte -> number of outputs
* 64 bytes -> each input
* 64 bytes -> each output

## Serialized Signed Transaction
---
* Serialized tx
* 1 bytes -> number of signatures
* 128 bytes -> each signature
