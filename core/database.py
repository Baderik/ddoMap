from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from core.settings import DB_URL

__all__ = ["engine", "Base", "SessionLocal"]

if "sqlite" in DB_URL:
    engine = create_engine(DB_URL)
else:
    engine = create_engine(DB_URL, pool_size=20, max_overflow=0)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
