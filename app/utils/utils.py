import json
from typing import Any


def response(data: Any = None, status: str = 'ok') -> json:
    """
    Темплейт респонса для контроллеров
    """
    if data is None:
        data = {}
    return {'data': data, 'status': status}

