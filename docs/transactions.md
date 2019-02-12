# Transaction

## Transactions
---
* Header 2 bytes
* Inputs - 16 bytes each
  * First 8 bytes -> tx-id of input
  * Second 8 bytes -> address of using input
* Outputs - 16 bytes each
  * First 8 bytes -> address of output
  * Second 8 bytes -> amount being sent(64 bits unsigned, should be maxed out at 0x8000000000000000, so we don't have any issues on C written protocols)
    * This gives us an upper limit of 9223372036854775808 denominations with 63 bits
* Signatures
  * Each input appends its signature of the hash(SHA256) of the unsigned serialization
* Signed Serialization
  * Each signature is 16 bytes in the order of the inputs
    * First 8 bytes is the r to the signature
    * Second 8 bytes is the s to the signature
  * It is appended to the end of the serialization to make a valid tx


## Serialized Unsigned Transactions
---
* 1 byte -> number of inputs
* 1 byte -> number of outputs
* 16 bytes -> each input
* 16 bytes -> each output

## Serialized Signed Transaction
---
* Serialized tx
* 8 bytes -> each signature of the hash of the serialized tx in the order of inputs
