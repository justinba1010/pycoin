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
➜  pycoin git:(master) ✗ make test
pushd ./src/; python3.9 ./test.py; popd
~/pycoin/src ~/pycoin
Private key: 16514447587256895052352051507506187227661814046951118039794603884423640943836
Public x: 64793516373702771591568988309233756818708566869560708861959136617517812801004
Public y: 76627129490044371638576481150719892244505574490848395864797894651013047139322
Wallet Address 0: b'8eVg8hUE9FSHCgxDr5takmjp61J32fv4zx7H8iKsTs5UeQRdK'
Wallet Address 1: b'2667W5WxzjV17pQRJj346jv9DTe5daHw5eKA7RHdv2raUX9ZjC'
This is our signed transaction:

00000000: 01 00 00 01 8F 3F D4 A6  94 7D CE CC 1F 14 E9 CE  .....?...}......
00000010: C4 16 E0 75 8F D9 3B 9D  15 A4 56 5A 66 31 A2 5A  ...u..;...VZf1.Z
00000020: 6F 0F DD EC A9 69 6B 18  23 D3 28 1F 29 E9 EA EF  o....ik.#.(.)...
00000030: 1A 6C 29 8E 7B 08 08 6A  C2 CF C8 F9 64 FD 41 3D  .l).{..j....d.A=
00000040: 1F F2 3B FA CD F4 C9 23  39 3F B5 E9 C7 F7 85 33  ..;....#9?.....3
00000050: C5 1F 47 05 22 42 17 BF  7E D6 D5 BB CC 67 6C 98  ..G."B..~....gl.
00000060: DB 2E C8 CD 99 17 03 79  F6 C2 35 3C C1 E8 E0 15  .......y..5<....
00000070: 6B EC 15 B3 2A 3B 46 27  68 C5 BB 8C 81 9F 25 40  k...*;F'h.....%@
00000080: 43 01 29 D8                                       C.).

The new TX hash is: 
xb37e89d11fcb998657355d72c6b57d780e42fe7dd83a71b6d0d0a3b2cf2cb419
We will make a block: c3347bf54c506e7fc67e19a8619223e2d1c30ddfc99c859a56cc3d8bb7902122
We will add the tx: ce37eab6a24dce26e65c461407463c08993810dd52f557357bdc0c6c6ebac619

This is the block contents 
00000000: FA DE FA DE 01 00 00 00  00 00 00 00 00 00 00 00  ................
00000010: 00 E2 77 F1 14 35 54 89  EE A1 FC 2D 5A 5A 3C 42  ..w..5T....-ZZ<B
00000020: 9A DC 91 19 A3 B0 7D 6B  E2 5D 67 8A 2A 75 C7 BC  ......}k.]g.*u..
00000030: C7 00 00 00 00 5F E9 70  0F FF FF FF FF 10 00 00  ....._.p........
00000040: 00 01 01 00 00 01 8F 3F  D4 A6 94 7D CE CC 1F 14  .......?...}....
00000050: E9 CE C4 16 E0 75 8F D9  3B 9D 15 A4 56 5A 66 31  .....u..;...VZf1
00000060: A2 5A 6F 0F DD EC A9 69  6B 18 23 D3 28 1F 29 E9  .Zo....ik.#.(.).
00000070: EA EF 1A 6C 29 8E 7B 08  08 6A C2 CF C8 F9 64 FD  ...l).{..j....d.
00000080: 41 3D 1F F2 3B FA CD F4  C9 23 39 3F B5 E9 C7 F7  A=..;....#9?....
00000090: 85 33 C5 1F 47 05 22 42  17 BF 7E D6 D5 BB CC 67  .3..G."B..~....g
000000A0: 6C 98 DB 2E C8 CD 99 17  03 79 F6 C2 35 3C C1 E8  l........y..5<..
000000B0: E0 15 6B EC 15 B3 2A 3B  46 27 68 C5 BB 8C 81 9F  ..k...*;F'h.....
000000C0: 25 40 43 01 29 D8                                 %@C.).

We will now mine it until the first 4 hex digits are 0


The block finished mining at nonce: 297697
The new hash is: 0000e1fc6dd254cfc0e6d2224047c015437d672537239f263104fde6bddb2356
Saving keys, keys made for blocks are automatically saved.
```
