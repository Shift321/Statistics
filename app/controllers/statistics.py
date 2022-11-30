from datetime import date
from typing import Optional

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import StatisticsCRUD
from app.utils import response
from app.utils import ErrorMessagesUtil


class StatisticsController:

    @staticmethod
    async def get(starts: date, ends: date, filter_by: Optional[str] = None, db: Session = Depends(get_db)):
        """
        Получение статистики за определенный промежуток времени
        """

        statistics = await StatisticsCRUD.show_in_time(starts=starts, ends=ends, filter_by=filter_by, db=db)
        if len(statistics) == 0:
            raise HTTPException(status_code=404,
                                detail=ErrorMessagesUtil.no_statitstics_between_date(starts=starts, ends=ends))
        return response(data=statistics)

    @staticmethod
    async def save(stat_date: date, views: Optional[int] = None, clicks: Optional[int] = None,
                   cost: Optional[float] = None,
                   db: Session = Depends(get_db)):
        """
        Сохранение статистики
        """
        statistics = await StatisticsCRUD.save(stat_date=stat_date, views=views,
                                               clicks=clicks, cost=cost, db=db)
        db.commit()
        return response(data=statistics)

    @staticmethod
    async def delete(db: Session = Depends(get_db)):
        """
        Удаление всей статистики
        """
        statistics = await StatisticsCRUD.delete(db=db)
        db.commit()
        return response()
