# pycoin

## Installing

System is required to have Python 3.7 or greater to install.
Run `make install`.
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
Private key: 99473331271771304360940542609648978172890070577571071437978724864388892288125
Public x: 22151781544167531805362197475648940527442304364498437889252000541621913588574
Public y: 1069901238826807630779442081095277279141647573014111374758398847047356225644
Wallet Address 0: b'2Evqs1YT6GKaKGN9BULSvo8GMFzcUAkYCX1WmcgCDeueqxVQbb'
Wallet Address 1: b'qcJEj9CLMNyNBwkpmYRsAqmKN6xoCFcG797ymiHmDqcUTktFR'
Wallet Address 2: b'z3MU7ApG3kwQoHd2NAkpy8GFDNwkVfVVxz8iCnFpq1c726Fqe'
Wallet Address 3: b'22HSh98qMUccVygBCM9nmPYoFzgWT8WZZUaAGGSCA69LxKqQiY'
Wallet Address 4: b'DtGGDkCnG4o8sffQkrM11jH8i8ijdKA7bpkkGJnNgRGPnaRLg'
Wallet Address 5: b'6gV9BZ8g2XJUEHtPqhCqcaCTBrA63Soh9YV9YinCtUGwhG6Wn'
Wallet Address 6: b'1N2gFskHbUjqAQ5GsH2jbrUgkwCNEGHoeJsvkc3TA1TGDPJ1A'
Wallet Address 7: b'ykmnypJPwu7sSVpXg5h8kFZqfMg7yTcPr3rJG6WAZouYtzNgq'
Wallet Address 8: b'2sLUSMrdgXdqYLRjrBg154K5itGEV7NzdeNqpAPJD11bEj1BoS'
Wallet Address 9: b'2vGKcrQ69qBKKyVATPfuBiDmQYRjaqGLtRaxba2e3RgC5Jx6qb'
Wallet Address 10: b'2ZerPUduAcsKYEQRDvfzSZvMU1n96AESJ1GfCmFL2ZzvRmroDJ'
Wallet Address 11: b'wnqU2SBoC5N8EPrMNsRUSW8S67AsMqmYCEDzC84MoqGrXQ1rm'
Wallet Address 12: b'9sF1zam5dJuLb7V3pnxvqkVjDJpncR2WvspEF4bqyLqoS1asw'
Wallet Address 13: b'qpVrn3NKJiW6ji5JdKkyGotv4jkXS5LFSDAimLNRPZj7ge87y'
Wallet Address 14: b'2SH8uosiSEqDbGCmkMdPj3og9uKcqgxHmNxs8e9QjD47fQNgxN'
Wallet Address 15: b'uQmzHCgrEZU5rJuHuNcFCeuDzv54uPWfvbMqTJpnq3UJGFMFg'
Wallet Address 16: b'2ggNbprfEBswK3m36ZdrZu2YWa1SypHhaDqkowVBEEuxJ7WXkQ'
Wallet Address 17: b'q4Ao7znaqAJ2HvrcdcmPvqx7amT4Lao7AaCfL5RLpxfaq12C3'
Wallet Address 18: b'gXekr2d329onajFj3vrk2au29FeYPjiu8MZSx5CXw5rLEbBQQ'
Wallet Address 19: b'zRTqZjVRySjXanGF1TSWnMmYrAz6B6CEkGERRS25ux5jKyzcp'
Wallet Address 20: b'EZ2eeSF1RWpuuZMNZKic3CFKsuYSaEUoSpBVc5RK9EcjBZEKL'
Wallet Address 21: b'2oVbgAb9Qj43DKgurRBSTadvDztPhWmt6pjpNoxzYEnQmkYHkJ'
Wallet Address 22: b'xitFm9MMY2UypYPWm5TjhV2W3DQm58siCrajmxVUK6DfPDq11'
Wallet Address 23: b'Ucw2jp468AyTnbKwyYiJn3rNsPaL6khhjVitGEr5kEfQXCXZP'
Wallet Address 24: b'2neuRWamxv1eNLhXxjz5P5kwtusvgdS3Jiyw88xghFyvvvD4Qw'
Wallet Address 25: b'2qy1mWzVYhZsXPqswKrcyWjTbLvMwp4pNheZGzFpU8nTKpAo6g'
Wallet Address 26: b'NZzFXjDw2ges2655rcMStvzs74vRQQs56bnsHghWSckhdjSxT'
[(22151781544167531805362197475648940527442304364498437889252000541621913588574, 1069901238826807630779442081095277279141647573014111374758398847047356225644, 67320460532883555023238481053762436724580749494410504541767244204105513232348, 84076863073697876609867589501249037202651116685818981001699662048396354143555)]
The new TX hash is: 
96a296d224f285c67bee93c30f8a309157f0daa35dc5b87e410b78630a09cfc7
We will make a block: 60847445570070410738802376938106653157072150723525018818891746179803138494205
We will add the tx: 6586063297165613106614770038514184728305938698493428643620268641125787633752
We will now mine it until the first 5 hex digits are 0
The block finished mining at nonce: 2455128
The new hash is: 37263615672294996210139982791530471284557915942745053244530194507321219
Saving keys, keys made for blocks are automatically saved.
```
