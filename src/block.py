# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# block.py

import time
from hashlib import sha256
from tools import tobytes, getbytes, hextoint

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
  # serialize() => bytes
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
  # get_hash() => int
  def get_hash(self):
    m = self.serialize()
    hash = sha256()
    hash.update(m)
    return hextoint(hash.hexdigest())

  # Utilities
  def from_serial(self, message):
    (self.blockNo, message) = getbytes(4, message)
    (self.blockNo, message) = getbytes(4, message)
    (self.blockNo, message) = getbytes(4, message)
    (self.blockNo, message) = getbytes(4, message)
    (self.blockNo, message) = getbytes(4, message)
    (self.blockNo, message) = getbytes(4, message)
    
  def mine(self):
    while self.get_hash() > 2**(256-self.difficulty):
      self.__incremement_nonce()

  # __get_generated() => int
  def __get_generated(self):
    return kFirstReward >> int(self.blockNo/kHalvingBlocks)

  # __get_block_reward() => int
  def __get_block_reward(self):
    # Add up unspent inputs
    unspent_inputs = self.__calculate_unspent()
    return 0

  def __incremement_nonce(self):
    self.nonce += 1
    if self.nonce == 2**32:
      print("This block cannot be mined.")
    self.nonce %= 2**32

  # __calculate_unspent() => int
  def __calculate_unspent(self):
    return 0
