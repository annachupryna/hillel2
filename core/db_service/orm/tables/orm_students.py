from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Базовий клас для визначення моделей даних
Base = declarative_base()


# Визначення моделі даних (таблиці) за допомогою класу
class ORMStudent(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
