exec:
		python main.py

setup:
		conda env create -f conda_requirements.yaml

build: clean
		pyinstaller main.py --onefile -n blackjack

test:
		Python -m unittest discover __test__

clean:
		rm -rf  **/__pycache__ **/**/__pycache__ uild dist *.spec


.PHONY: clean test
