# Copyright 2019 Justin Baum
# Pycoin
# 10 March 2019
# merkle.py

# Eventually wil be a merkle tree

from hashlib import sha256
from tools import tobytes, getbytes, hextoint

class MerkleList:
  def __init__(self, txs = None):
    self.txhashs = []
    if isinstance(txs, list):
      self.addtxs(txs)
    elif txs == None:
      return
    else:
      self.addtx(txs)

  def addtxs(self, txshashes):
    self.txhashs += txshashes

  def addtx(self, txhash):
    self.txhashs.append(txhash)
  
  def merkleroot(self):
    hash = sha256()
    for txhash in self.txhashs:
      hash.update(txhash)
    return hash.digest()

