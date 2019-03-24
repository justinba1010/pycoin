# pycoin

## Installing

System is required to have Python 3.7 or greater to install.
Run `make install`. (This installs )
Latest version of Python can be downloaded from https://www.python.org/downloads/

## Running

 Run `make` to generate an address.
`make` generates a new key-pair and outputs the public key (address) in decimal. 

Run `make clean-keys` to clean up.

Run `make test` to run test script.

## Current Status

`make test`

```
[~/pycoin]$ make test
pushd ./src/; python3 ./test.py; popd
~/pycoin/src ~/pycoin
Private key: 20427134077001397945081865387912523699333319475742231022241618842586752704140
Public x: 11449916952927893355361329347826704898780667194675547290487673615542212837979
Public y: 102570172851815691251195335681346609244269102659316846975126414286114831922275
Wallet Address 0: b'DaYHTgkf8EcfccsiRgbW5tn5mqMEa7WepogqY6SJszzgNDRhP'
Wallet Address 1: b'2YZ5GvKz4XmDCFoXqFkVoXrZcbugceMLaaaVsjn1s95XUzi4J9'
Wallet Address 2: b'2tn4TAAWrAxkzufdsd3CVBSEnKPUw5SFpfktWDe3sQC4cmoNNQ'
Wallet Address 3: b'i7hWj84Vt586YaJNh8cmopYuwBcZd7RaSJ6JSXZvvcYdcJFyW'
Wallet Address 4: b'fqerRbaqfeUz8qpr9N3uAEsgcT1JaRMtZtzK9Dxiyp9KpnzKC'
Wallet Address 5: b'C9cjVdTgYD8qnQX5zX1Kxq982y6zahhQgZzzAJwUjLAgyRGrU'
This is our signed transaction:

00000000: 01 00 00 01 19 50 6C 5F  DD D9 B5 20 4A 55 6F FA  .....Pl_... JUo.
00000010: 03 9B 25 2C 08 80 FA 68  09 2A 3F 7F AF A2 64 57  ..%,...h.*?...dW
00000020: 20 43 42 5B E2 C4 A9 18  30 B5 5B C2 76 50 1A 2E   CB[....0.[.vP..
00000030: 66 F5 A9 14 47 EC D5 7E  32 52 4A B6 D8 BA 0E 55  f...G..~2RJ....U
00000040: 3A 86 F4 63 FF 61 2B 96  69 A4 E0 B8 20 5D 0D 7A  :..c.a+.i... ].z
00000050: 6A 34 BE 66 91 D1 41 3A  3A 7D FF 8F 83 6F 72 F9  j4.f..A::}...or.
00000060: BA 55 85 01 C7 4C 9B 0A  45 F5 43 80 5F 16 05 C1  .U...L..E.C._...
00000070: 4C 65 92 44 E5 CB 1C 23  3A CA EC 17 3E B4 4C D0  Le.D...#:...>.L.
00000080: 94 5D 8C FD                                       .]..

The new TX hash is: 
x22938a4b71ccd716d82518948cdf6dcc59c09cb244ffb6b43762e4cb5ebe5cc5
We will make a block: 570f4acf482aff5efbf2f801be4d84a4c25551de9e2816159c822acd64228811
We will add the tx: 8200f06088afb24a7c95c3365d78a05b2126488ee925b7840b3b6a27af2ac0f7

This is the block contents 
00000000: FA DE FA DE 01 00 00 00  00 00 00 00 00 00 00 00  ................
00000010: 00 CC 32 18 0C 13 E0 09  98 24 6D AC F0 BF A5 FE  ..2......$m.....
00000020: 5D 71 F7 6B CB 04 A1 68  37 57 E3 AF 17 B0 FA CE  ]q.k...h7W......
00000030: 5E 00 00 00 00 5C 96 EE  DB FF FF FF FF 10 00 00  ^....\..........
00000040: 00 01 01 00 00 01 19 50  6C 5F DD D9 B5 20 4A 55  .......Pl_... JU
00000050: 6F FA 03 9B 25 2C 08 80  FA 68 09 2A 3F 7F AF A2  o...%,...h.*?...
00000060: 64 57 20 43 42 5B E2 C4  A9 18 30 B5 5B C2 76 50  dW CB[....0.[.vP
00000070: 1A 2E 66 F5 A9 14 47 EC  D5 7E 32 52 4A B6 D8 BA  ..f...G..~2RJ...
00000080: 0E 55 3A 86 F4 63 FF 61  2B 96 69 A4 E0 B8 20 5D  .U:..c.a+.i... ]
00000090: 0D 7A 6A 34 BE 66 91 D1  41 3A 3A 7D FF 8F 83 6F  .zj4.f..A::}...o
000000A0: 72 F9 BA 55 85 01 C7 4C  9B 0A 45 F5 43 80 5F 16  r..U...L..E.C._.
000000B0: 05 C1 4C 65 92 44 E5 CB  1C 23 3A CA EC 17 3E B4  ..Le.D...#:...>.
000000C0: 4C D0 94 5D 8C FD                                 L..]..

We will now mine it until the first 4 hex digits are 0
The block finished mining at nonce: 67532
The new hash is: 0000d450019c80218aaaf3c3b60335ae6e8d5b7daf7e978bfca4afa8b883d647
Saving keys, keys made for blocks are automatically saved.
```
