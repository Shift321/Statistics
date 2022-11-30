# Statistics

Тестовое задание для компании CiPlay
## Техническое задание
Нужно разработать микросервис для счетчиков статистики. Сервис должен уметь взаимодействовать с клиентом при помощи REST API. Также нужно реализовать валидацию входных данных.

API методы:
Метод сохранения статистики
Метод показа статистики
Метод сброса статистики
Метод сохранения статистики.
Принимает на вход:

date - дата события
views - количество показов
clicks - количество кликов
cost - стоимость кликов (в рублях с точностью до копеек)
Поля views, clicks и cost - опциональные. Статистика агрегируется по дате.

Метод показа статистики
Принимает на вход:

from - дата начала периода (включительно)
to - дата окончания периода (включительно)
Отвечает статистикой, отсортированной по дате. В ответе должны быть поля:

date - дата события
views - количество показов
clicks - количество кликов
cost - стоимость кликов
cpc = cost/clicks (средняя стоимость клика)
cpm = cost/views * 1000 (средняя стоимость 1000 показов)
Метод сброса статистики
Удаляет всю сохраненную статистику.

Критерии приемки:
язык программирования: Python/ Fast Api
можно использовать любое хранилище(PostgreSQL, MySQl, Redis и т.д.) или обойтись без него (in-memory). При использовании СУБД нужен файл с запросами на создание - - всех необходимых таблиц.
формат даты YYYY-MM-DD.
стоимость указывается в рублях с точностью до копеек.
в методе показа статистики можно выбрать сортировку по любому из полей ответа.
простая инструкция для запуска (в идеале — с возможностью запустить в docker).
Усложнения:
покрытие unit-тестами.
документация (достаточно структурированного описания методов, примеров их вызова в README.md).
## Установка и запуск приложения


```bash
Скачать репозиторий
После чего использовать команду
docker-compose up
```

## CRUD

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
## Controllers
Получение статистики за определенный промежуток времени
```python
async def get(starts: date, ends: date, filter_by: Optional[str] = None, db: Session = Depends(get_db)):

    statistics = await StatisticsCRUD.show_in_time(starts=starts, ends=ends, filter_by=filter_by, db=db)
    if len(statistics) == 0:
        raise HTTPException(status_code=404,
                            detail=ErrorMessagesUtil.no_statitstics_between_date(starts=starts, ends=ends))
    return response(data=statistics)
```
Сохранение статистики
```python
async def save(stat_date: date, views: Optional[int] = None, clicks: Optional[int] = None,
               cost: Optional[float] = None,
               db: Session = Depends(get_db)):

    statistics = await StatisticsCRUD.save(stat_date=stat_date, views=views,
                                           clicks=clicks, cost=cost, db=db)
    db.commit()
    return response(data=statistics)
```
Удаление всей статистики
```python
async def delete(db: Session = Depends(get_db)):

    statistics = await StatisticsCRUD.delete(db=db)
    db.commit()
    return response()
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