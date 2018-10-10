install:
	pip3 install -r requeriments.txt
	pip3 install pytest

test:
	cd ./src/ && python3 test_Status.py
