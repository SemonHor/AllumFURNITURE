

all: RunAPI

.PHONY: req
req:
	poetry install --no-root

.PHONY: flake8
flake8: req
	poetry run flake8

.PHONY: QA
QA: flake8

.PHONY: Docker_start
Docker:
	./start_postgres_docker.sh
	poetry run alembic upgrade head

RunAPI: flake8
	poetry run uvicorn src.main:app