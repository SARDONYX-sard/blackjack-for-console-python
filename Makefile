exec:
		poetry run py -3 -m src

i:
		make install

install:
		poetry install --no-interaction

build: clean
		poetry run pyinstaller main.py --onefile -n blackjack

lint:
		# stop the build if there are Python syntax errors or undefined names
		poetry run flake8 ./src ./tests --count --select=E9,F63,F7,F82 --show-source --statistics
    # exit-zero はすべてのエラーを警告として扱う。 GitHub エディタの幅は 127 文字
		poetry run flake8 ./src ./tests  --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test:
		poetry run python -m unittest

clean:
		rm -rf  **/__pycache__ **/**/__pycache__ uild dist *.spec


.PHONY: clean test
