# News Showcase Monorepo

This is a monorepository for the News Showcase project, a dynamic news platform with a web-based showcase, native ads, and adaptive design for desktop and mobile devices. The project includes a FastAPI-based web module, with plans for future services like ranking, RTB, analytics, and monitoring.

## Structure
- `config/`: Shared configuration files (categories, ads, settings).
- `shared/`: Shared resources (models, schemas, migrations, utilities).
- `web/`: Web showcase module (FastAPI, frontend, database logic).
- `other_services/`: Placeholder for future services (ranking, RTB, etc.).

## Setup
1. Install Poetry: `pip install poetry`
2. Install dependencies: `cd web && poetry install`
3. Set up PostgreSQL and update `config/settings.py` with database URL.
4. Run migrations: `alembic upgrade head`
5. Start the server: `poetry run uvicorn web.app.main:app --reload`

## Requirements
- Python 3.11+
- PostgreSQL 15+
- Poetry 1.8+
- Docker (optional, for containerization)

## Development
- Use `docker-compose.yml` for local development.
- Add new migrations in `shared/migrations/`.
- Update models in `shared/models/` and schemas in `shared/schemas/`.
- Run tests: `poetry run pytest`

## Notes
- TODO: Include poetry.lock in VCS once dependencies stabilize.
