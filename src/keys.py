# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# keys.py

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256
import os
from tools import getbytes, tobytes

KEYFOLDER = "keys/"

class Keys:
  def __init__(self):
    self.keys = []
    self.importKeys()
  def saveToFile(self):
    for (key, pub) in self.keys:
      s = tobytes(key,16)
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
  def signTX(self, trans):
    m = trans.serialize_unhashed().decode()
    # Get currect keys to sign...
    (r,s) = ecdsa.sign(m, self.keys[0][0], curve=curve.secp256k1, hashfunc=sha256)
    trans.signatures.append((r,s))
  #def verify(self, publickey, )

key = Keys()
print(key.keys)
print(key.getaddresses())
