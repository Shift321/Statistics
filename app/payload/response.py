from datetime import date
from typing import Optional

from pydantic import BaseModel, validator


class StatisticsUploadResponse(BaseModel):
    """
    Респонс модель
    """
    stat_date: date
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[float]
    cpc: Optional[float] = None
    cpm: Optional[float] = None

    class Config:
        orm_mode = True

    """
    Подсчет полей cpc и cpm
    """

    @validator("cpc", always=True, pre=True)
    def cpc_count(cls, v, values):
        cost = values['cost']
        clicks = values['clicks']
        if cost and clicks is not None:
            v = cost / clicks
            return v

    @validator("cpm", always=True, pre=True)
    def cpm_count(cls, v, values):
        cost = values['cost']
        views = values['views']
        if cost and views is not None:
            v = cost / views * 1000
            return v
