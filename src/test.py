from keys import Keys
from transaction import Transaction
from block import Block
from blockchain import Blockchain
import tools
from hexdump import hexdump

wallet = Keys()
#wallet.genkey()
ourkey = wallet.keys[-1]
ownerkey = wallet.keys[-2]
outputaddresses = wallet.getaddresses()

blockchain = Blockchain()

print("Private key: " + str(ourkey[0]))
print("Public x: " + str(ourkey[1].x))
print("Public y: " + str(ourkey[1].y))
for counter, address in enumerate(wallet.getaddresses()):
  print("Wallet Address " + str(counter) + ": " + str(address))

tx = Transaction(origins=[(outputaddresses[0], 1), (outputaddresses[1], 2)])
print("Transaction has no origins:")
print("Transaction has output to {} with amount {}".format(
    outputaddresses[0], 1))
print("Transaction has output to {} with amount {}".format(
    outputaddresses[2], 2))
wallet.signTX(tx, -1)
print("This is our signed transaction:")
print()
hexdump(tx.serialize())
print()

print("Verifying the transaction: ")
print(tx.verify(blockchain))

print("The new TX hash is: ")
print(tools.bytestohex(tx.get_unsigned_hash()))

block = Block(owner=ownerkey[1].x)
blockchain.add_block(block)

print("We will make a block: " + str(block.get_hash_hex()))
block.tx.append(tx)
print("We will add the tx: " + str(block.get_hash_hex()))

hexdigits = 4
block.difficulty = 0xFFFFFFFF
block.difficultyoffset = hexdigits * 4
block.gen_target()

print()
print("This is the block contents ")
hexdump(block.serialize())
print()

print("We will now mine it until the first " + str(hexdigits) +
      " hex digits are 0")

block.mine()
print("The block finished mining at nonce: " + str(block.nonce))
print("The new hash is: " + str(block.get_hash_hex()))

print("This is the block contents ")
hexdump(block.serialize())
print("Saving keys, keys made for blocks are automatically saved.")
wallet.saveToFile()
