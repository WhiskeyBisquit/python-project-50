install:
	poetry install

selfcheck:
	poetry check

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

# check: selfcheck test lint

# lint:
# 	poetry run flake8 gendiff

# build: check
# 	poetry build