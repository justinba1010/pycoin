# Copyright 2020 Justin Baum
# Pycoin
# 11 February 2019
# block.py

import time
from hashlib import sha256
import tools
from merkle import MerkleList
import __blockparams as blockparams

# internals
from transaction import Transaction
from keys import Keys

class Block:
  def __init__(self, owner = None, prevhash = None):
    self.blockNo = 0
    self.next = None
    self.hash = None
    self.difficulty = 0
    self.difficultyoffset = 0
    self.nonce = 0
    self.prevhash = prevhash
    self.timestamp = int(time.time())
    self.keys = None
    self.target = tools.tobytes(0x0000FFFF * 2**208, 32)
    self.tx = []
    if not owner:
      # generate keys
      self.keys = Keys(False)
      self.keys.genkey()
      self.owner = self.keys.keys[0][1].x
      self.keys.saveToFile("blockkeys/")
    else:
      self.owner = owner

  def gen_last_tx(self):
    lastTx = Transaction([], [(self.owner, self.__get_block_reward())])
    self.keys.signTX(lastTx)
    return lastTx

  def genesis_block(self):
    return 0

  def gen_header(self):
    serial = tools.tobytes(0,0)
    # Add Block Header
    serial += tools.tobytes(blockparams.kMagicNum, blockparams.lmagicnum)
    serial += tools.tobytes(blockparams.kVersion, blockparams.lVersion)
    serial += tools.tobytes(self.blockNo, blockparams.lblockno)
    serial += tools.tobytes(self.nonce, blockparams.lnonce)
    serial += tools.tobytes(self.prevhash, blockparams.lprevhash)
    serial += tools.tobytes(self.get_merkle(), blockparams.lmerkle)
    serial += tools.tobytes(self.timestamp, blockparams.ltimestamp)
    serial += tools.tobytes(self.difficulty, blockparams.ldifficulty)
    serial += tools.tobytes(self.difficultyoffset, blockparams.ldifficultyoffset)
    serial += tools.tobytes(len(self.tx), blockparams.ltx)
    return serial

  def de_header(self, message):
    (kMagicNum, message) = tools.getbytes(blockparams.lmagicnum, message)
    (kVersion, message) = tools.getbytes(blockparams.lVersion)
    (self.blockNo, message) = tools.getbytes(blockparams.lblockno, message)
    (self.nonce, message) = tools.getbytes(blockparams.lnonce, message)
    (self.prevhash, message) = tools.getbytes(blockparams.lprevhash, message)
    (self.merkle, message) = tools.getbytes(blockparams.lmerkle, message)
    (self.timestamp, message) = tools.getbytes(blockparams.ltimestamp, message)
    (self.difficulty, message) = tools.getbytes(blockparams.ldifficulty, message)
    (self.difficultyoffset, message) = tools.getbytes(blockparams.ldifficultyoffset, message)
    (_, message) = tools.getbytes(blockparams.ltx, message)
    return message
  
  def gen_target(self):
    target = self.difficulty << (224-self.difficultyoffset)
    self.target = tools.tobytes(target, 32)

  # serialize() => bytes
  def serialize(self):
    serial = self.gen_header()
    for tx in self.tx:
      serial += tx.serialize()
    return serial

  # get_hash() => bytes (use merkleroot)
  def get_hash(self):
    m = self.gen_header()
    return tools.gethash(m)

  def get_hash_hex(self):
    m = self.gen_header()
    return tools.gethashhex(m)

  # Utilities
  def from_serial(self, message):
    message = self.de_header(message)
    while message:
      tx = Transaction()
      message = tx.from_serial(message)
      self.tx.append(tx)
    
  def mine(self):
    while self.get_hash() > self.target:
      self.nonce += 1

  def get_merkle(self):
    merklelist = MerkleList(list(map(lambda x: x.get_unsigned_hash(), self.tx)))
    return merklelist.merkleroot()

  # __get_generated() => int
  def __get_generated(self):
    return blockparams.kFirstReward >> int(self.blockNo/blockparams.kHalvingBlocks)

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
    for tx in self.tx:
      unspent += tx.get_unspent()
    return unspent
