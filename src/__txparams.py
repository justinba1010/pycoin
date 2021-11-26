# Copyright 2019 Justin Baum
# Pycoin
# 21 March 2019
# __txparams.py
"""
This details the length of each field in the transaction.
"""

# Currents
Version = 1

# Lengths
lversion = 1
lnumin = 1
lprevtxhash = 32
ltxoutindex = 1
lnumout = 1
lvalue = 8
lpublicaddress = 32
#s ignatures
lsigx = 32
lsigy = 32
lsigr = 32
lsigq = 32
lnumsig = 1
