# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# transaction.py

from fastecdsa import point, curve, ecdsa
from hashlib import sha256

import __txparams as txparams
import tools


class Transaction:

  def __init__(self, origins=[], destinations=[]):
    # origins are tuples of (tx hashes, index)
    # destinations are tuples of (address, and amounts)
    self.origins = origins
    self.destinations = destinations
    # Signatures are (public x, public y, r, q)
    self.signatures = []
    self.hash = None
    self.version = txparams.Version

  def serialize_unsigned(self):
    # start a byte sequence
    serial = tools.tobytes(0, 0)
    serial += tools.tobytes(txparams.Version, txparams.lversion)
    serial += tools.tobytes(len(self.origins), txparams.lnumin)
    for origin in self.origins:
      # 64 bytes for each input
      serial += tools.tobytes(origin[0],
                              txparams.lprevtxhash)  # tx hash of origin
      serial += tools.tobytes(origin[1], txparams.ltxoutindex)  # tx index
    serial += tools.tobytes(len(self.destinations), txparams.lnumout)
    for destination in self.destinations:
      # 64 bytes for each output
      serial += tools.tobytes(
          destination[0], txparams.lpublicaddress)  # public x of destination
      serial += tools.tobytes(destination[1],
                              txparams.lvalue)  # amount in units
    return serial

  def serialize(self):
    serial = self.serialize_unsigned()
    # 1 bytes for num of signatures
    serial += tools.tobytes(len(self.signatures), txparams.lnumsig)
    for signature in self.signatures:
      serial += tools.tobytes(signature[0], txparams.lsigx)  # Public x
      serial += tools.tobytes(signature[1], txparams.lsigy)  # Public y
      # Signatures part
      serial += tools.tobytes(signature[2], 32)  # r
      serial += tools.tobytes(signature[3], 32)  # q
    return serial

  def from_serial(self, message):
    (self.version, message) = tools.getbytes(txparams.lversion, message)
    (nInputs, message) = tools.getbytes(txparams.lnumin, message)
    self.origins = []
    for i in range(nInputs):
      (txid, message) = tools.getbytes(txparams.lprevtxhash, message)
      (index, message) = tools.getbytes(txparams.ltxoutindex, message)
      self.origins.append((txid, index))
    (nOutputs, message) = tools.getbytes(txparams.lnumout, message)
    self.destinations = []
    for i in range(nOutputs):
      (address, message) = tools.getbytes(txparams.lpublicaddress, message)
      (value, message) = tools.getbytes(txparams.lvalue, message)
      self.destinations.append((address, value))
    (nSignatures, message) = tools.getbytes(txparams.lnumsig, message)
    self.signatures = []
    for i in range(nSignatures):
      (px, message) = tools.getbytes(txparams.lsigx, message)
      (py, message) = tools.getbytes(txparams.lsigy, message)
      (r, message) = tools.getbytes(txparams.lsigr, message)
      (q, message) = tools.getbytes(txparams.lsigq, message)
      self.signatures.append((px, py, r, q))
    return message

  def get_unsigned_hash(self):
    return tools.gethash(self.serialize())

  def get_unsigned_hex_hash(self):
    return tools.gethashhex(self.serialize())

  def verify(self, blockchain):
    """
    """

    def check_signature(px, py, r, q):
      msg = self.serialize_unsigned()
      try:
        Q = point.Point(px, py, curve.secp256k1)
      except ecdsa.EcdsaError:
        return False
      except ValueError:
        return False
      return ecdsa.verify(
          sig=(r, q),  # signature
          msg=msg,
          Q=Q,
          hashfunc=sha256,
          curve=curve.secp256k1)

    origin_spend = 0
    for origin, signature in zip(self.origins, self.signatures):
      (txid, index) = origin
      (px, py, r, q) = signature
      # TODO: Find tranasction
      tx = blockchain.tx.get(txid)
      # Check if tx exists and the output exists
      if not tx or index >= len(tx.destinations):
        return False
      destination = tx.destinations[index]

      # TODO: Keep track if inputs > outputs
      # TODO: Check to make sure tx not spent
      if not check_signature(px, py, r, q):
        return False
    return True

  def __copy__(self):
    copy = transaction.Transaction()
    copy.origins = self.origins[:]
    copy.destinations = self.destinations[:]
    return copy
