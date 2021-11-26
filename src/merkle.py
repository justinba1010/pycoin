# Copyright 2019 Justin Baum
# Pycoin
# 10 March 2019
# merkle.py

from hashlib import sha256
from tools import tobytes, getbytes, hextoint


class MerkleTree:

  def __init__(self, txs=None):
    self.txhashs = []
    if isinstance(txs, list):
      self.addtxs(txs)
    elif txs == None:
      return
    else:
      self.addtx(txs)

  @staticmethod
  def left(n):
    return (n << 1) + 1

  @staticmethod
  def right(n):
    return (n << 1) + 2

  @staticmethod
  def up(n):
    return (n - 1) >> 1

  def addtxs(self, txshashes):
    self.txhashs += txshashes

  def addtx(self, txhash):
    self.txhashs.append(txhash)

  def merkleroot(self):
    return sha256(self.merkleroot_(0, len(self.txhashs) - 1)).digest()

  def merkleroot_(self, n, x):
    left = MerkleTree.left(n)
    right = MerkleTree.right(n)
    if x < left:
      if x < n:
        return sha256().digest()
      return self.txhashs[n]
    hashy = sha256((self.merkleroot_(left, x) + self.merkleroot_(right, x)))
    return hashy.digest()
