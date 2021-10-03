exec:
		python main.py

setup:
		conda env create -f conda_requirements.yaml

build:
		pyinstaller main.py --onefile -n blackjack

test:
		Python -m unittest discover __test__ && make clean

clean:
		rm -rf  **/__pycache__ **/**/__pycache__

.PHONY: clean test
