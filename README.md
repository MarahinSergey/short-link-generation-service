# short-link-generation-service
Creating a short url. Deleting a url. Getting a full URL.

## Виртуальное окружение:
#### Создать
```python -m venv venv``` или ```python3 -m venv venv```
#### Активировать
- Windows: ```venv\Scripts\activate.bat```
- Linux и MacOS: ```source venv/bin/activate```
#### Деактивировать ```deactivate```
#### Удалить
- Windows: ```venv.destroy()```
- Linux и MacOS: ```rm -r venv/```
### poetry
#### Установка ```pip install poetry```
#### Установка пакетов ```poetry install```
#### Обновление пакетов ```poetry update```
#### Добавить пакет ```poetry add {package_name}```

## alembic
alembic init alembic

## RUN IN DOCKER
```cd docker```
```docker compose up --build -d```

## Migrations
- make migration `alembic revision --autogenerate -m "create account table"`
- migrate last `alembic upgrade head`


## app run ```http://0.0.0.0:8000/api/docs/```