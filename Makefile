repo = tidyball
codecov_token = 

.PHONY: check coverage format tests

check:
	black --check --line-length 100 ${repo}
	black --check --line-length 100 tests
	black --check --line-length 100 src
	flake8 --max-line-length 100 ${repo}
	flake8 --max-line-length 100 tests
	flake8 --max-line-length 100 src

clean:
	rm --force --recursive **/__pycache__
	rm --force --recursive __pycache__
	rm --force --recursive .pytest_cache
	rm --force --recursive results
	rm --force .mutmut-cache

coverage:
	mkdir --parents results
	pytest --cov=${repo} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

format:
	black --line-length=100 ${repo}
	black --line-length=100 tests

init: install tests

install:
	pip install --editable .

mutants: install
	mkdir --parents results
	mutmut run --paths-to-mutate ${repo}

tests:
	pytest --verbose