
init:
	mkdir ./keys || true
	mkdir ./keys/blockkeys || true
	bash ./scripts/gen_address.sh

clean-keys:
	echo "This is a really bad idea if this were real."
	bash ./scripts/kindadangerous.sh

install:
	pip install fastecdsa base58
	# If this doesn't work you may need to find where fastecdsa is installed on your system
	cp ./patch/ecdsa.py /usr/local/lib/python3.7/site-packages/fastecdsa/ecdsa.py
	cp ./patch/util.py /usr/local/lib/python3.7/site-packages/fastecdsa/util.py

test:
	pushd ./src/; python3 ./test.py; popd
