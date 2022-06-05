# installs virtual environment
setup:
	source ~/.msds434-gcp/bin/activate

# installs source code from a requirements file and updates pip to the current version
install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

# test the libraries and notebooks
test:
	python -m pytest -vv test_main.py
	#python -m pytest --nbval notebook.ipynb

format:
	black *.py

# disables false positives and keeps recommendation warnings but leaves errors
# linting library, command-line tool, and web application
lint:
	pylint --disable=R,C main.py

# run "make all" to have all commands run
all: setup install format lint test