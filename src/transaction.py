# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# transaction.py

from hashlib import sha256
from tools import tobytes, getbytes

class Transaction:
  def __init__(self, origins = [], destinations = []):
    # origins are tuples of (tx hashes, and addresses)
    # destinations are tuples of (address, and amounts)
    self.origins = origins
    self.destinations = destinations
    # Signatures are (public x, public y, r, q)
    self.signatures = []
    self.hash = None
  def serialize_unsigned(self):
    # start a byte sequence
    serial = tobytes(0,0)
    serial += tobytes(len(self.origins), 1)
    serial += tobytes(len(self.destinations), 1)
    for origin in self.origins:
      # 64 bytes for each input
      serial += tobytes(origin[0], 32)  # tx hash of origin
      serial += tobytes(origin[1], 32)  # public x of origin
    for destination in self.destinations:
      # 64 bytes for each output
      serial += tobytes(destination[0], 32)  # public x of destination
      serial += tobytes(destination[1], 32)  # amount in units
    return serial
  def serialize(self):
    serial = self.serialize_unsigned()
    # 1 bytes for num of signatures
    serial += tobytes(len(self.signatures),1)
    for signature in self.signatures:
      serial += tobytes(signature[0], 32)  # Public x
      serial += tobytes(signature[1], 32)  # Public y
      # Signatures part
      serial += tobytes(signature[2], 32)  # r
      serial += tobytes(signature[3], 32)  # q
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
    (nSignatures, message) = getbytes(1, message)
    for i in range(nSignatures):
      (px, message) = getbytes(4, message)
      (py, message) = getbytes(4, message)
      (r, message)  = getbytes(4, message)
      (q, message)  = getbytes(4, message)
      self.signatures((px, py, r, q))
    # Signatures
  def get_unsigned_hash(self):
    m = self.serialize_unsigned()
    hash = sha256()
    hash.update(m)
    
