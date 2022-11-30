from datetime import date
from typing import Optional
from pydantic import parse_obj_as

from app.models import Statistics
from app.payload import StatisticsUploadResponse


class StatisticsCRUD:

    @staticmethod
    async def save(db, stat_date: date, views: Optional[int] = None, clicks: Optional[int] = None,
                   cost: Optional[float] = None) -> StatisticsUploadResponse:
        """
        Сохранение статистики
        """
        statistics = Statistics(stat_date=stat_date,
                                views=views,
                                clicks=clicks,
                                cost=cost)
        db.add(statistics)
        db.flush()
        return parse_obj_as(StatisticsUploadResponse, statistics)

    @staticmethod
    async def show_in_time(db, start: date, end: date, filter_by: Optional[str]) -> list[StatisticsUploadResponse]:
        """
        Показ статистики
        """
        if not filter_by:
            filter_by = 'stat_date'
        statistics = db.query(Statistics). \
            filter(Statistics.stat_date >= start, Statistics.stat_date <= end). \
            order_by(filter_by).all()

        return parse_obj_as(list[StatisticsUploadResponse], statistics)

    @staticmethod
    async def delete(db) -> None:
        """
        Удаление статистики
        """
        statistics = db.query(Statistics).all()
        db.delete(statistics)
        db.flush()
