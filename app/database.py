from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = "mysql+pymysql://root:Dnam14012006!@localhost:3306/SS24_IT215_BTTH1"

Engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=Engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
