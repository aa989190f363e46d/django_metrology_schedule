MANAGE := poetry run python manage.py

run: 
	export DJANGO_DEBUG=True
	$(MANAGE) runserver

repl:
	$(MANAGE) shell_plus

test:

install:
	poetry install

test:
	

lint:
	poetry run flake8 django_metrology_schedule

selfcheck:
	poetry check

check: selfcheck lint test

build:
	poetry build

publish:
	 poetry publish -r pypi-test

.PHONY: repl tun publish install test lint selfcheck check build