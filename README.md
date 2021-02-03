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
pushd ./src/; python3.9 ./test.py; popd
~/pycoin/src ~/pycoin
Private key: 92083257871373550863232481981772659260566714762705859235696551129935809984169
Public x: 101802235501780075571292264576948691644382705623020414330618483533993126186766
Public y: 93667983299543472015735375988454216325563932416913182489759216698519760269052
Wallet Address 0: b'wt1do7Lt3di8PYUXvqr7CFXkDTX7BQ9TnVMnr6WjAcQskjWcw'
Wallet Address 1: b'TCNRTdvQLVZbYBbvEjmirFVHxZ5maCCJpc4JohmzuX6mibCgc'
Wallet Address 2: b'hHh4qrnSJYRcZFXV4ev6P81BU7FUQdjUgZhnBEoFUNmfcfxrJ'
Wallet Address 3: b'7V7ZJ9zin2VX6Cv2wTCFgZY4yDN64xAPnCQPGrhVHGy1dWz8j'
Wallet Address 4: b'SdHj9y9Nszx6tuwVApr5jsafMkm2AX47hBtfXKqZhionSzdZA'
Wallet Address 5: b'2i883MgTPCd4XyuTKGqzw4Wjf4vKjicrydto6UdTndcQGHC9it'
Transaction has no origins:
Transaction has output to b'wt1do7Lt3di8PYUXvqr7CFXkDTX7BQ9TnVMnr6WjAcQskjWcw' with amount 1
Transaction has output to b'hHh4qrnSJYRcZFXV4ev6P81BU7FUQdjUgZhnBEoFUNmfcfxrJ' with amount 2
This is our signed transaction:

00000000: 01 02 77 74 31 64 6F 37  4C 74 33 64 69 38 50 59  ..wt1do7Lt3di8PY
00000010: 55 58 76 71 72 37 43 46  58 6B 44 54 58 37 42 51  UXvqr7CFXkDTX7BQ
00000020: 39 54 6E 56 4D 6E 72 36  57 6A 41 63 51 73 6B 6A  9TnVMnr6WjAcQskj
00000030: 57 63 77 01 54 43 4E 52  54 64 76 51 4C 56 5A 62  Wcw.TCNRTdvQLVZb
00000040: 59 42 62 76 45 6A 6D 69  72 46 56 48 78 5A 35 6D  YBbvEjmirFVHxZ5m
00000050: 61 43 43 4A 70 63 34 4A  6F 68 6D 7A 75 58 36 6D  aCCJpc4JohmzuX6m
00000060: 69 62 43 67 63 02 00 01  E1 12 05 FC C4 F2 2C 2F  ibCgc.........,/
00000070: 3E 59 58 99 9A D8 32 4A  C5 33 45 12 0F 0E D2 7B  >YX...2J.3E....{
00000080: 94 8C EA E6 28 C4 CF 0E  CF 16 33 25 C5 83 32 0D  ....(.....3%..2.
00000090: 62 93 13 01 97 74 C1 9B  90 C8 76 10 8B 65 8E 6E  b....t....v..e.n
000000A0: 9B B7 53 AB 3C C5 EE FC  FD 3C 9F 66 5F AF 90 11  ..S.<....<.f_...
000000B0: 99 47 3F 8B E2 DF FA 45  F6 A5 A6 BD 80 4D F9 08  .G?....E.....M..
000000C0: A7 A3 4B 45 28 02 C4 BC  3D A3 FB FA 80 95 B7 11  ..KE(...=.......
000000D0: 86 D6 F4 EB 9A C9 04 01  2A 49 12 17 1D 05 E6 87  ........*I......
000000E0: BA D5 6D BF 6F C7 26 39                           ..m.o.&9

The new TX hash is: 
df370208187233682b543c470675617a567c2402b832347f31407301355e2afe
We will make a block: bc947127313031542333c3f4beb586ce6a60c7eb9838faadd6800dbd06556faa
We will add the tx: 144418c02eb1108c08d886929cf7ef756e6705e5132193fae6bad1341868fea3

This is the block contents 
00000000: FA DE FA DE 01 00 00 00  00 00 00 00 00 00 00 00  ................
00000010: 00 61 3A 5A E1 71 46 82  00 12 62 B5 9B E7 0D 1B  .a:Z.qF...b.....
00000020: 4F A5 25 31 65 73 C7 00  52 DB 1D 4B 6A A0 3D 5D  O.%1es..R..Kj.=]
00000030: 1C 00 00 00 00 60 1A 1B  48 FF FF FF FF 10 00 00  .....`..H.......
00000040: 00 01 01 02 77 74 31 64  6F 37 4C 74 33 64 69 38  ....wt1do7Lt3di8
00000050: 50 59 55 58 76 71 72 37  43 46 58 6B 44 54 58 37  PYUXvqr7CFXkDTX7
00000060: 42 51 39 54 6E 56 4D 6E  72 36 57 6A 41 63 51 73  BQ9TnVMnr6WjAcQs
00000070: 6B 6A 57 63 77 01 54 43  4E 52 54 64 76 51 4C 56  kjWcw.TCNRTdvQLV
00000080: 5A 62 59 42 62 76 45 6A  6D 69 72 46 56 48 78 5A  ZbYBbvEjmirFVHxZ
00000090: 35 6D 61 43 43 4A 70 63  34 4A 6F 68 6D 7A 75 58  5maCCJpc4JohmzuX
000000A0: 36 6D 69 62 43 67 63 02  00 01 E1 12 05 FC C4 F2  6mibCgc.........
000000B0: 2C 2F 3E 59 58 99 9A D8  32 4A C5 33 45 12 0F 0E  ,/>YX...2J.3E...
000000C0: D2 7B 94 8C EA E6 28 C4  CF 0E CF 16 33 25 C5 83  .{....(.....3%..
000000D0: 32 0D 62 93 13 01 97 74  C1 9B 90 C8 76 10 8B 65  2.b....t....v..e
000000E0: 8E 6E 9B B7 53 AB 3C C5  EE FC FD 3C 9F 66 5F AF  .n..S.<....<.f_.
000000F0: 90 11 99 47 3F 8B E2 DF  FA 45 F6 A5 A6 BD 80 4D  ...G?....E.....M
00000100: F9 08 A7 A3 4B 45 28 02  C4 BC 3D A3 FB FA 80 95  ....KE(...=.....
00000110: B7 11 86 D6 F4 EB 9A C9  04 01 2A 49 12 17 1D 05  ..........*I....
00000120: E6 87 BA D5 6D BF 6F C7  26 39                    ....m.o.&9

We will now mine it until the first 4 hex digits are 0
The block finished mining at nonce: 82126
The new hash is: 0000687cafa2a4cdbd4cd1794509588767988a53112c07bcb8b1680547919e07
This is the block contents 
00000000: FA DE FA DE 01 00 00 00  00 00 01 40 CE 00 00 00  ...........@....
00000010: 00 61 3A 5A E1 71 46 82  00 12 62 B5 9B E7 0D 1B  .a:Z.qF...b.....
00000020: 4F A5 25 31 65 73 C7 00  52 DB 1D 4B 6A A0 3D 5D  O.%1es..R..Kj.=]
00000030: 1C 00 00 00 00 60 1A 1B  48 FF FF FF FF 10 00 00  .....`..H.......
00000040: 00 01 01 02 77 74 31 64  6F 37 4C 74 33 64 69 38  ....wt1do7Lt3di8
00000050: 50 59 55 58 76 71 72 37  43 46 58 6B 44 54 58 37  PYUXvqr7CFXkDTX7
00000060: 42 51 39 54 6E 56 4D 6E  72 36 57 6A 41 63 51 73  BQ9TnVMnr6WjAcQs
00000070: 6B 6A 57 63 77 01 54 43  4E 52 54 64 76 51 4C 56  kjWcw.TCNRTdvQLV
00000080: 5A 62 59 42 62 76 45 6A  6D 69 72 46 56 48 78 5A  ZbYBbvEjmirFVHxZ
00000090: 35 6D 61 43 43 4A 70 63  34 4A 6F 68 6D 7A 75 58  5maCCJpc4JohmzuX
000000A0: 36 6D 69 62 43 67 63 02  00 01 E1 12 05 FC C4 F2  6mibCgc.........
000000B0: 2C 2F 3E 59 58 99 9A D8  32 4A C5 33 45 12 0F 0E  ,/>YX...2J.3E...
000000C0: D2 7B 94 8C EA E6 28 C4  CF 0E CF 16 33 25 C5 83  .{....(.....3%..
000000D0: 32 0D 62 93 13 01 97 74  C1 9B 90 C8 76 10 8B 65  2.b....t....v..e
000000E0: 8E 6E 9B B7 53 AB 3C C5  EE FC FD 3C 9F 66 5F AF  .n..S.<....<.f_.
000000F0: 90 11 99 47 3F 8B E2 DF  FA 45 F6 A5 A6 BD 80 4D  ...G?....E.....M
00000100: F9 08 A7 A3 4B 45 28 02  C4 BC 3D A3 FB FA 80 95  ....KE(...=.....
00000110: B7 11 86 D6 F4 EB 9A C9  04 01 2A 49 12 17 1D 05  ..........*I....
00000120: E6 87 BA D5 6D BF 6F C7  26 39                    ....m.o.&9
Saving keys, keys made for blocks are automatically saved.
~/pycoin

```
