from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

Base = declarative_base()

# Загружаем переменные окружения
load_dotenv()

DB_USER = os.getenv("DB_USER", "finance_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "people4people")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "finance")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, connect_args={"options": "-csearch_path=public"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


