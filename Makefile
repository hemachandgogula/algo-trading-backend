.PHONY: help install run test lint format clean docker-up docker-down migrate

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies with Poetry"
	@echo "  make run          - Run the FastAPI application"
	@echo "  make test         - Run tests with pytest"
	@echo "  make lint         - Run linting with ruff"
	@echo "  make format       - Format code with black"
	@echo "  make clean        - Remove cache and temporary files"
	@echo "  make docker-up    - Start all services with docker-compose"
	@echo "  make docker-down  - Stop all services"
	@echo "  make migrate      - Run database migrations"

install:
	poetry install --no-root

run:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	poetry run pytest -v

lint:
	poetry run ruff check app tests

format:
	poetry run black app tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

docker-up:
	docker-compose up --build

docker-down:
	docker-compose down

migrate:
	poetry run alembic upgrade head
