
init:
	mkdir ./keys || true
	bash ./scripts/gen_address.sh

clean-keys:
	echo "This is a really bad idea if this were real."
	bash ./scripts/kindadangerous.sh
