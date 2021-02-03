# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# keys.py

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256
import os

from tools import getbytes, tobytes, tob58

KEYFOLDER = "../keys/"

class Keys:
  def __init__(self, importation = True):
    self.keys = []
    if importation:
      self.importKeys()
  def saveToFile(self, folder = ""):
    for (key, pub) in self.keys:
      s = tobytes(key, 32)
      hashy = sha256()
      hashy.update(s)
      filename = hashy.hexdigest()[:8]
      filename = KEYFOLDER + folder + filename + ".key"
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
    # Return addresses as b58(public key x coord)
    return list(map(lambda x: (tob58(x[1].x)), self.keys))
  def signTX(self, trans, nkey = 0):
    m = trans.serialize_unsigned()
    # Get currect keys to sign...
    (r,s) = ecdsa.sign(m, self.keys[nkey][0], curve=curve.secp256k1, hashfunc=sha256)
    trans.signatures.append((self.keys[nkey][1].x, self.keys[nkey][1].y, r,s))
  #def verify(self, publickey, )
