from keys import Keys
from transaction import Transaction
from block import Block

wallet = Keys()
wallet.genkey()
ourkey = wallet.keys[-1]
print("Private key: " + str(ourkey[0]))
print("Public x: " + str(ourkey[1].x))
print("Public y: " + str(ourkey[1].y))

tx = Transaction()
wallet.signTX(tx, -1)
print("Wallet signatures: ")
print(tx.signatures)

print("The new TX hash is: ")
print(tx.get_unsigned_hash())

block = Block()

print("We will make a block: " + str(block.get_hash()))
block.tx.append(tx)

print("We will add the tx: " + str(block.get_hash()))
print("We will now mine it until the first 4 hex digits are 0")
block.difficulty = 16
block.mine()
print("The block finished mining at nonce: " + str(block.nonce))
print("The new hash is: " + str(block.get_hash()))
