from sqlalchemy.orm import Session

from core.database import *


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)  # TODO: Migrations
