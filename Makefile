
all: lint test validate

setup: setup_npm setup_python


setup_npm:
	npm install

lint:lint_markdown lint_python

lint_markdown:
	find *.md | grep '\.md$$' \
		| xargs npx markdownlint --config ./.markdownlint.json

POETRY_NO_ROOT:= --no-root
setup_python:
	poetry install $(POETRY_OPTION)

lint_python: pyright black flake8 isort yamllint jsonlint pydocstyle

pyright:
	npx pyright

black:
	find ./src tests | grep py$$ | xargs black --diff | diff /dev/null -

flake8:
	find ./src tests | grep py$$ | xargs flake8

isort:
	find ./src tests | grep py$$ | xargs isort --diff | diff /dev/null -

yamllint:
	find . -name '*.yml' -type f | grep -v node_modules | xargs yamllint --no-warnings

jsonlint:
	python3 -c "import sys,json;print(json.dumps(\
	    json.loads(sys.stdin.read()),\
	    indent=4,ensure_ascii=False,sort_keys=True))" \
	< ./.markdownlint.json  | diff -q - ./.markdownlint.json

pydocstyle:
	pydocstyle ./src tests --ignore=D100,D101,D102,D103,D104,D105,D107,D203,D212,D400,D415

test_python:
	coverage run -m unittest discover tests

_test_format_vanilla:
	python -m asdc.check.format -t vanilla -i ./data/vanilla
test_format: _test_format_vanilla
test: test_python test_format

validate: validate_example

validate_example:
	python -m asdc.check.format --type example -i ./data/scud/hotel --prefix "quasi_japanese_reviwes.hotel." --ref ./data/vanilla/hotel --all_correct
	python -m asdc.check.format --type example -i ./data/scud/spot --prefix "quasi_japanese_reviwes.spot." --ref ./data/vanilla/spot --all_correct
