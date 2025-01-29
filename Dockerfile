FROM python:3.10.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=2.0.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install "poetry==${POETRY_VERSION}"

RUN rm -f poetry.lock \
    && poetry lock \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --only main

# Copy only poetry files first
COPY pyproject.toml poetry.lock ./

# Generate a fresh lock file and install dependencies
RUN poetry lock --no-update \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --only main

# Copy project
COPY . .

# Create directory for static files
RUN mkdir -p /app/staticfiles

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser