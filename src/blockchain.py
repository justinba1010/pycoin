# Copyright 2020 Justin Baum
# Pycoin
# 6 January 2020
# blockchain.py

from block import Block

class Blockchain:
    def __init__(self):
        self.tx = {}
        self.blocks = []
    def add_block(self, block : Block):
        self.blocks.append(block)
        # Validate
        if block.prevhash != self.blocks[-1].hash and len(self.blocks) != 0:
            raise Exception("Illegal block")
        for tx in block.tx:
            self.tx[tx.get_unsigned_hash()] = tx
            # Verify tx signatures and address match
    
