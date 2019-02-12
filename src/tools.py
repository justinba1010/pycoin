# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# tools.py

ENDIANNESS = "big"

def tobytes(int, padding):
  return (int).to_bytes(padding, byteorder=ENDIANNESS)

def getbytes(nbytes, message):
  byte_list = list(message)
  return (int.from_bytes(byte_list[:nbytes], byteorder=ENDIANNESS), byte_list[nbytes:])
