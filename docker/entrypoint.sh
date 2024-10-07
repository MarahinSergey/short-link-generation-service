#!/bin/sh

alembic upgrade head
if [ $DEBUG = 'True' ]; then
    echo 'Service start in debug mode'
    python -m debugpy --listen 0.0.0.0:5678 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
else
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
fi
