from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import datetime

DATABASE_URL = 'sqlite:///errors.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)

Base.query = db_session.query_property()
