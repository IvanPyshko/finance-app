from fastapi import FastAPI
from database.db import engine, Base

app = FastAPI()

# Создаем таблицы в БД (позже заменим на Alembic)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Transaction Service is running"}
