install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

generate_diff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

coverage:
	  poetry run pytest --cov=gendiff --cov-report xml
