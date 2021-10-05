exec:
		poetry run py -3 -m src/run.py

i:
		make install

install:
		poetry install --no-interaction

build: clean
		poetry run pyinstaller ./src/run.py --clean --onefile --name blackjack --distpath ../dist

lint:
		# stop the build if there are Python syntax errors or undefined names
		poetry run flake8 ./src ./tests --count --select=E9,F63,F7,F82 --show-source --statistics
    # exit-zero はすべてのエラーを警告として扱う。 GitHub エディタの幅は 127 文字
		poetry run flake8 ./src ./tests  --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test:
		poetry run python -m unittest

exetest:
		make build
		cd ./dist && ./blackjack.exe
clean:
		rm -rf  **/__pycache__ **/**/__pycache__


.PHONY: clean test
