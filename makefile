PIP = pip3.9
PYTHON = python3.9

init:
	mkdir ./keys || true
	mkdir ./keys/blockkeys || true
	bash ./scripts/gen_address.sh

clean-keys:
	echo "This is a really bad idea if this were real."
	bash ./scripts/kindadangerous.sh

install:
	$(PIP) install fastecdsa base58 hexdump --user
	# If this doesn't work you may need to find where fastecdsa is installed on your system
	# This was patched upstream

test:
	pushd ./src/; $(PYTHON) ./test.py; popd

newkey:
	pushd ./src/; $(PYTHON) -c "from keys import Keys; a = Keys(); a.genkey(); a.saveToFile(); print(\"Generated key\")"; popd
