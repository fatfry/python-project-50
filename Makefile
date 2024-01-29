install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

diff:
	poetry run gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check


build:
	poetry build

#.PHONY: install test lint selfcheck check build package-install