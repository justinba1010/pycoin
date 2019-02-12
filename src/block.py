# Copyright 2019 Justin Baum
# Pycoin
# 11 February 2019
# block.py

import time
import hashlib
from tools import tobytes, getbytes

class Block:
  def __init__(self, data = None, prevhash = None):
    self.blockNo = 0
    self.data = data
    self.next = None
    self.hash = None
    self.nonce = 0
    self.prevhash = prevhash
    self.timestamp = int(time.time())
    self.tx = []
  def serialize(self):
    serial = tobytes(0,0)
    # Add Block Header
    serial += tobytes(self.blockno, 4)
    serial += tobytes(self.nonce, 4)
    serial += tobytes(self.prevhash, 8)
    serial += tobytes(self.timestamp, 4)
    serial += tobytes(len(self.tx), 4)
    for tx in self.tx:
      serial += tx.serialize()
    return serial

