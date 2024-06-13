from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Підключення до бази даних (замініть на свої дані підключення)
DATABASE_URL = "postgresql+psycopg2://yakimov:1029nRiEg3847@localhost/db_lab3_"

# Створення підключення
engine = create_engine(DATABASE_URL)

# Базовий клас для декларативних моделей
Base = declarative_base()

# Створення сесії для взаємодії з базою даних
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
