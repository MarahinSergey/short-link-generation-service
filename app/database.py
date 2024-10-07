from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from app.utils.settings import settings

engine = create_engine(settings.DATABASE_URI, pool_size=10, max_overflow=2, pool_recycle=300, pool_use_lifo=True)
if not database_exists(engine.url):
    create_database(settings.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
autocommit_engine = engine.execution_options(autocommit=True)
connection = autocommit_engine.connect()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
