from datetime import date
from typing import Optional

from pydantic import BaseModel


class StatisticsUploadRequest(BaseModel):
    """
    Реквест модель
    """
    stat_date: date
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[float] = None
