# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# tools.py

ENDIANNESS = "big"

# We will not use underscores for these, they should be explicit enough

# tobytes(x : int, padding : int) => bytes
def tobytes(x, padding):
  if x == None:
    x = 0
  return (x).to_bytes(padding, byteorder=ENDIANNESS)

# getbytes(nbytes : int, message : bytes) => (int(of first nbytes), bytes(rest of message))
def getbytes(nbytes, message):
  byte_list = list(message)
  return (int.from_bytes(byte_list[:nbytes], byteorder=ENDIANNESS), byte_list[nbytes:])
# hextoint(hex : string) => int
def hextoint(hex):
  return int(hex, 16)
