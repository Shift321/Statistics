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
        if values['cost'] and values['clicks'] is not None:
            v = values['cost'] / values['clicks']
            return v

    @validator("cpm", always=True, pre=True)
    def cpm_count(cls, v, values):
        if values['cost'] and values['views'] is not None:
            v = values['cost'] / values['views'] * 1000
            return v
