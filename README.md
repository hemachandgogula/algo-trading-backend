# Algo Trading Platform - Backend

A FastAPI-based backend for an algorithmic trading platform with PostgreSQL, Redis, and Celery integration.

## Features

- **FastAPI** - Modern, fast web framework for building APIs
- **PostgreSQL** - Async database with SQLAlchemy ORM
- **Redis** - Caching and message broker
- **Celery** - Background task processing
- **Alembic** - Database migrations
- **Docker** - Containerized development and deployment
- **Poetry** - Dependency management

## Project Structure

```
.
├── app/
│   ├── api/            # API endpoints
│   │   ├── health.py   # Health check endpoints
│   │   └── __init__.py
│   ├── core/           # Core functionality
│   │   ├── cache.py    # Redis client setup
│   │   ├── config.py   # Settings and configuration
│   │   └── __init__.py
│   ├── db/             # Database configuration
│   │   ├── base.py     # SQLAlchemy base
│   │   ├── session.py  # Database session management
│   │   └── __init__.py
│   ├── models/         # Database models
│   │   ├── user.py     # User model
│   │   └── __init__.py
│   ├── services/       # Business logic services
│   │   └── __init__.py
│   └── main.py         # FastAPI application entry point
├── alembic/            # Database migrations
│   ├── versions/       # Migration files
│   └── env.py          # Alembic configuration
├── tests/              # Test suite
│   ├── conftest.py     # Test fixtures
│   └── test_health.py  # Health check tests
├── docker-compose.yml  # Docker services configuration
├── Dockerfile          # Application container
├── pyproject.toml      # Poetry dependencies
├── alembic.ini         # Alembic configuration
└── .env.example        # Environment variables template
```

## Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Poetry (for local development)

## Quick Start with Docker

1. **Clone the repository and navigate to the project directory**

2. **Copy the environment file**
   ```bash
   cp .env.example .env
   ```

3. **Start all services**
   ```bash
   docker-compose up --build
   ```

   This will:
   - Start PostgreSQL database
   - Start Redis cache
   - Run database migrations
   - Start the FastAPI application

4. **Access the application**
   - API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

## Local Development Setup

### 1. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. Install Dependencies

```bash
poetry install
```

### 3. Set up Environment Variables

```bash
cp .env.example .env
# Edit .env with your local configuration
```

### 4. Start Required Services

Start PostgreSQL and Redis using Docker:

```bash
docker-compose up postgres redis
```

### 5. Run Database Migrations

```bash
poetry run alembic upgrade head
```

### 6. Start the Development Server

```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Environment Variables

Key environment variables (see `.env.example` for full list):

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql+asyncpg://postgres:postgres@localhost:5432/algotrading` |
| `REDIS_URL` | Redis connection string | `redis://localhost:6379/0` |
| `SECRET_KEY` | Secret key for JWT tokens | `your-secret-key-change-in-production` |
| `DEBUG` | Enable debug mode | `false` |
| `TRADING_API_KEY` | Trading platform API key | - |
| `TRADING_API_SECRET` | Trading platform API secret | - |

## Database Migrations

### Create a new migration

```bash
poetry run alembic revision --autogenerate -m "description of changes"
```

### Apply migrations

```bash
poetry run alembic upgrade head
```

### Rollback migrations

```bash
poetry run alembic downgrade -1
```

## Testing

### Run all tests

```bash
poetry run pytest
```

### Run with coverage

```bash
poetry run pytest --cov=app --cov-report=html
```

### Run specific test file

```bash
poetry run pytest tests/test_health.py
```

## Code Quality

### Format code with Black

```bash
poetry run black app tests
```

### Lint with Ruff

```bash
poetry run ruff check app tests
```

### Type check with MyPy

```bash
poetry run mypy app
```

## API Documentation

Once the application is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## Health Check

The `/health` endpoint provides status information about the application and its dependencies:

```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "ok",
  "services": {
    "database": "up",
    "cache": "up"
  }
}
```

## Docker Commands

### Build and start all services

```bash
docker-compose up --build
```

### Start services in background

```bash
docker-compose up -d
```

### Stop services

```bash
docker-compose down
```

### View logs

```bash
docker-compose logs -f api
```

### Restart a specific service

```bash
docker-compose restart api
```

## Project Development

### Adding New Models

1. Create model in `app/models/`
2. Import in `app/models/__init__.py`
3. Import in `alembic/env.py`
4. Generate migration: `alembic revision --autogenerate -m "add new model"`
5. Apply migration: `alembic upgrade head`

### Adding New API Endpoints

1. Create router in `app/api/`
2. Define endpoints with appropriate dependencies
3. Include router in `app/api/__init__.py`

### Adding Background Tasks

Configure Celery tasks in `app/services/` and use the Celery broker configuration from settings.

## Troubleshooting

### Database connection issues

- Ensure PostgreSQL is running: `docker-compose ps postgres`
- Check database logs: `docker-compose logs postgres`
- Verify `DATABASE_URL` in `.env`

### Redis connection issues

- Ensure Redis is running: `docker-compose ps redis`
- Check Redis logs: `docker-compose logs redis`
- Verify `REDIS_URL` in `.env`

### Migration issues

- Check Alembic logs for errors
- Verify database connection
- Try: `alembic downgrade -1` then `alembic upgrade head`

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## License

MIT License
