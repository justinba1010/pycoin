
init:
	mkdir ./keys || true
	python3 -c 'from keys import Keys; keys = Keys(); keys.genkey(); keys.saveToFile(); print("Generated: "+keys.getaddresses()[-1])'
