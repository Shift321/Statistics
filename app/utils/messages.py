from datetime import date


class ErrorMessagesUtil:

    @staticmethod
    def no_statitstics_between_date(start: date, end: date):
        return f"с {start} по {end} cтатистики не обнаружено"
