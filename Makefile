install:
	poetry install

diff:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --гыук dist/*.whl

make lint:
	poetry run flake8 brain_games