# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# tools.py

import base58
from hashlib import sha256

ENDIANNESS = "big"

# We will not use underscores for these, they should be explicit enough

# tobytes(x : int, padding : int) => bytes
def tobytes(x, padding):
  if x == None:
    x = 0
  return (x).to_bytes(padding, byteorder=ENDIANNESS)

# getbytes(nbytes : int, message : bytes) => (int(of first nbytes), bytes(rest of message))
def getbytes(nbytes: int, message: bytes):
  byte_list = list(message)
  return (int.from_bytes(byte_list[:nbytes], byteorder=ENDIANNESS), byte_list[nbytes:])
# hextoint(hex : string) => int
def hextoint(hex):
  return int(hex, 16)

def tob58(b, padding = 32):
  if type(b) == int:
    return base58.b58encode_check(tobytes(b, padding))
  return base58.b58encode_check(b)

fromb58 = lambda string: base58.b58decode_check(string)

def gethash(message):
  hash = sha256()
  hash.update(message)
  return hash.digest()

def gethashhex(message):
  hash = sha256()
  hash.update(message)
  return hash.hexdigest()

def gethashint(message):
  hash = sha256()
  hash.update(message)
  return hextoint(hash.hexdigest())