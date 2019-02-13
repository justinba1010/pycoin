# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# transaction.py

from hashlib import sha256
from tools import tobytes, getbytes

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
    serial += tobytes(len(self.origins), 1)
    serial += tobytes(len(self.destinations), 1)
    for origin in self.origins:
      #  64 bytes for each input
      serial += tobytes(origin[0], 32)
      serial += tobytes(origin[1], 32)
    for destination in self.destinations:
      #  16 bytes for each output
      serial += tobytes(destination[0], 32)
      serial += tobytes(destination[1], 32)
    return serial
  def serialize(self):
    serial = self.serialize_unhashed()
    for signature in self.signatures:
      serial += tobytes(signature[0], 32)
      serial += tobytes(signature[1], 32)
    return serial
  def from_serial(self, message):
    (nInputs, message) = getbytes(1, message)
    (nOutputs, message) = getbytes(1, message)
    for i in range(nInputs):
      (txid, message) = getbytes(32, message)
      (address, message) = getbytes(32, message)
      self.origins.append((txid, address))
    for i in range(nOutputs):
      (address, message) = getbytes(32, message)
      (value, message) = getbytes(32, message)
      self.destinations.append((address, value))
    # Signatures
