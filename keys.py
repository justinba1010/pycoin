# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# keys.py

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256
import os

KEYFOLDER = "keys/"

class Keys:
  def __init__(self):
    self.keys = []
    self.importKeys()
  def saveToFile(self):
    for (key, pub) in self.keys:
      s = key.to_bytes(256, byteorder="big")
      hash = sha256()
      hash.update(s)
      filename = hash.hexdigest()[:8]
      filename = KEYFOLDER + filename + ".key"
      keys.export_key(key, curve=curve.secp256k1, filepath=filename)
  def genkey(self):
    d, Q = keys.gen_keypair(curve.secp256k1)
    self.keys.append((d,Q))
  def importKeys(self):
    for file in os.listdir(KEYFOLDER):
      if file.endswith(".key"):
        d, Q = keys.import_key(KEYFOLDER+file)
        self.keys.append((d,Q))
  def getaddresses(self):
    # Return addresses as hex(public key x coord)
    return list(map(lambda x: hex(x[1].x), self.keys))
