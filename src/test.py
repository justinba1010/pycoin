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
