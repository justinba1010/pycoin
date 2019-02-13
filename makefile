
init:
	mkdir ./keys || true
	bash ./scripts/gen_address.sh

clean-keys:
	echo "This is a really bad idea if this were real."
	bash ./scripts/kindadangerous.sh

install:
	pip install fastecdsa
	cp ./patch/ecdsa.py /usr/local/lib/python3.7/site-packages/fastecdsa/ecdsa.py
	cp ./patch/util.py /usr/local/lib/python3.7/site-packages/fastecdsa/util.py

test:
	pushd ./src/; python3 ./test.py; popd
