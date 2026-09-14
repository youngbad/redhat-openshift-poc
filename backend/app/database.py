import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Read the database URL from the environment, falling back to a local SQLite
# file so the app can run without a PostgreSQL instance during local tests.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local.db")

# SQLite requires this extra connect arg when used with multiple threads (e.g. FastAPI's TestClient).
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
