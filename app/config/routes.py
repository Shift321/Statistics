from fastapi import APIRouter

from app.controllers import StatisticsController

APIRouter.__enter__ = lambda self: self
APIRouter.__exit__ = lambda *args: ''

router = APIRouter()

with APIRouter(prefix="/api/v1") as api_v1:
    """
    Эндпоинты статистики
    """
    api_v1.post('/save-statistics')(StatisticsController.save)
    api_v1.get('/get-statistics')(StatisticsController.get)
    api_v1.delete('/delete-statistics')(StatisticsController.delete)

router.include_router(api_v1)
