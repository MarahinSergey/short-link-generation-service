FROM python:3.12.6

ENV IN_DOCKER=1

WORKDIR /code
ENV PYTHONPATH /code

# Copy alembic
COPY ./alembic.ini /code/alembic.ini
# Copy poetry files
COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock
# Copy all entrypoint files
COPY ./docker/*.sh /
# Copy folder with code
COPY ./app /code/app
# Find all files with sh extention and change chmod
RUN  find / -name "*.sh" | xargs chmod 777
# Instal updates
RUN apt-get update -y
RUN pip install --upgrade pip
# Install poetry
RUN pip install poetry
# Disable venvs (use container default venv)
RUN poetry config virtualenvs.create false
# Install all dependencies (exclude dev)
RUN poetry install --no-root
