FROM python:3.11-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy Poetry configuration
COPY web/pyproject.toml web/poetry.lock* ./

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy project files
COPY . .

CMD ["uvicorn", "web.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
