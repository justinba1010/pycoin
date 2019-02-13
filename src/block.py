# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# block.py

import time
from hashlib import sha256
from tools import tobytes, getbytes

# internals
from transaction import Transaction
from keys import Keys

kFirstReward = 50000000
kHalvingBlocks = 210000

class Block:
  def __init__(self, owner = None, prevhash = None):
    self.blockNo = 0
    self.next = None
    self.hash = None
    self.difficulty = 0
    self.nonce = 0
    self.prevhash = prevhash
    self.timestamp = int(time.time())
    self.keys = None
    self.tx = []
    if not owner:
      # generate keys
      self.keys = Keys(False)
      self.keys.genkey()
      self.owner = self.keys.keys[0][1].x
      self.keys.saveToFile("blockkeys/")

  def gen_last_tx(self):
    lastTx = Transaction([], [(self.owner, self.__get_block_reward())])
    self.keys.signTX(lastTx)
    return lastTx
  def genesis_block(self):
    return 0
  def serialize(self):
    serial = tobytes(0,0)
    # Add Block Header
    serial += tobytes(self.blockNo, 4)
    serial += tobytes(self.nonce, 4)
    serial += tobytes(self.prevhash, 8)
    serial += tobytes(self.timestamp, 4)
    serial == tobytes(self.difficulty, 4)
    serial += tobytes(len(self.tx), 4)
    for tx in self.tx:
      serial += tx.serialize()
    return serial
  def get_hash(self):
    m = self.serialize()
    hash = sha256()
    hash.update(m)
    return hash.hexdigest()
  # Utilities
  def mine(self):
    while int(self.get_hash(), 16) > 2**(256-self.difficulty):
      self.__incremement_nonce()

  def __get_generated(self):
    return kFirstReward >> int(self.blockNo/kHalvingBlocks)
  def __get_block_reward():
    # Add up unspent inputs
    unspent_inputs = self.__calculate_unspent()
    return 0
  def __incremement_nonce(self):
    self.nonce += 1
    self.nonce %= 2**32
