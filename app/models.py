from sqlalchemy import Column, String

from app.database import Base


class UrlModel(Base):
    __tablename__ = 'urls'

    short_url = Column(String(50), primary_key=True)
    long_url = Column(String(5000), unique=True, nullable=False)
