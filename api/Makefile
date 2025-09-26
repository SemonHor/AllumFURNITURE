

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
Docker_start:
	./start_postgres_docker.sh
	sleep 4
	poetry run alembic upgrade head

.PHONY: alebmic_autogen
alebmic_autogen:
	poetry run alembic upgrade head
	poetry run alembic revision --autogenerate -m ""

RunAPI: flake8
	poetry run uvicorn src.main:app --reload