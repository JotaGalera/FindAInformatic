install:
	pip3 install -r requeriments.txt
	

test:
	cd ./src/ && pytest
