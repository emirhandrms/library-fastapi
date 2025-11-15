from fastapi import Depends
from sqlalchemy import create_engine
from app.utils.db_parser import parse_connection_string
from app.core.settings import settings
from sqlalchemy.orm import sessionmaker

con_str = parse_connection_string(settings.SQL_CONNECTION_STRING)
engine = create_engine(con_str)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)