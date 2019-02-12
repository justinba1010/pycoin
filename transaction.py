# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# transaction.py

from hashlib import sha256

class Transaction:
  def __init__(self, origins = [], destinations = []):
    #  origins are tuples of (tx hashes, and addresses)
    #  destinations are tuples of (address, and amounts)
    self.origins = origins
    self.destinations = destinations
    self.signatures = []
    self.hash = None
  def serialize_unhashed(self):
    #  start a byte sequence
    serial = tobytes(0,0)
    for origin in self.origins:
      #  16 bytes for each input
      serial += tobytes(origin[0], 8)
      serial += tobytes(origin[1], 8)
    for destination in self.destinations:
      #  16 bytes for each output
      serial += tobytes(destination[0], 8)
      serial += tobytes(destination[1], 8)
    return serial

def tobytes(int, padding):
  return (int).to_bytes(padding, byteorder="big")

tx = Transaction([(10,20),(15,30)],[(10,30)])
print(tx.serialize_unhashed())