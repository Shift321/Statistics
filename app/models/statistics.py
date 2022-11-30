from typing import Optional
from datetime import date
from sqlalchemy import Column, Integer, Date, Float

from app.database import Base


class Statistics(Base):
    __tablename__ = "statistics"

    id: int = Column(Integer, primary_key=True, index=True)
    stat_date: date = Column(Date)
    views: Optional[int] = Column(Integer)
    clicks: Optional[int] = Column(Integer)
    cost: Optional[float] = Column(Float)
