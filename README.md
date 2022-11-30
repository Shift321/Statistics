# Statistics

Тестовое задание для компании CiPlay

## Установка и запуск приложения


```bash
Скачать репозиторий
После чего использовать команду
docker-compose up
```

## Основные круды

Сохранение статистики в базу данных
```python
async def save(db,
               stat_date: date,
               views: Optional[int] = None,
               clicks: Optional[int] = None,
               cost: Optional[float] = None) -> StatisticsUploadResponse:

        statistics = Statistics(stat_date=stat_date,
                                views=views,
                                clicks=clicks,
                                cost=cost)
        db.add(statistics)
        db.flush()
        return parse_obj_as(StatisticsUploadResponse, statistics)
```
Показ статистики в определенном временном промежутке
```python
async def show_in_time(db, starts: date, ends: date, filter_by: str) -> list[StatisticsUploadResponse]:
    if not filter_by:
        filter_by = 'stat_date'
    statistics = db.query(Statistics). \
        filter(Statistics.stat_date >= starts, Statistics.stat_date <= ends). \
        order_by(filter_by).all()

    return parse_obj_as(list[StatisticsUploadResponse], statistics)
```
Удаление Статистики из базы данных
```python
async def delete(db) -> None:
    statistics = db.query(Statistics).all()
    for statistic in statistics:
        db.delete(statistic)
    db.flush()
```
## База данных
В качестве базы данных была использованна SQLite так как для данного задания ее достаточно
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./app/database/statistics.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
```
## Тесты
Для тестов был использован Pytest тесты находятся в директории tests.
Запуск тестов находясь в директории app
```bash
pytest
```

## Стак технологий

<a href="https://fastapi.tiangolo.com/">
    <img src="https://img.shields.io/badge/FastAPI-0.75.0-57b3b8?style=flat&logo=fastapi&logoColor=white" alt="FastAPI Badge"/>
    <img src="https://img.shields.io/badge/sqlite3-db-green" alt="SQLite Badge"/>
    <img src="https://img.shields.io/badge/PyTest-tests-red" alt="Pytest Badge"/>
    <img src="https://img.shields.io/badge/Docker-3.8-blue" alt="Docker Badge"/>
    <img src="https://img.shields.io/badge/SqlAlchemy-1.4.44-yellowgreen" alt="Sqlalch Badge"/>
</a>