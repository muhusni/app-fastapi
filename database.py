from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"mysql+pymysql://{os.getenv('DATABASE_USER', 'root')}:{os.getenv('DATABASE_PASSWORD', '')}@{os.getenv('DATABASE_CONNECTION', 'localhost')}:{os.getenv('DATABASE_PORT', '3306')}/{os.getenv('DATABASE', 'dbapp')}"
DATABASE_URL_SSO = f"mysql+pymysql://{os.getenv('DATABASE_USER_SSO')}:{os.getenv('DATABASE_PASSWORD_SSO', '')}@{os.getenv('DATABASE_CONNECTION_SSO')}:{os.getenv('DATABASE_PORT_SSO')}/{os.getenv('DATABASE_SSO')}"
DATABASE_URL_TICKET = f"mysql+pymysql://{os.getenv('DATABASE_USER_SSO')}:{os.getenv('DATABASE_PASSWORD_SSO', '')}@{os.getenv('DATABASE_CONNECTION_SSO')}:{os.getenv('DATABASE_PORT_SSO')}/{os.getenv('DATABASE_TICKET')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine_sso = create_engine(DATABASE_URL_SSO)
SessionLocalSso = sessionmaker(autocommit=False, autoflush=False, bind=engine_sso)

engine_ticket = create_engine(DATABASE_URL_TICKET)
SessionLocalTicket = sessionmaker(autocommit=False, autoflush=False, bind=engine_ticket)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db_sso():
    db = SessionLocalSso()
    try:
        yield db
    finally:
        db.close()


def get_db_tiket():
    db = SessionLocalTicket()
    try:
        yield db
    finally:
        db.close()

