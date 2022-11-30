from datetime import date


class ErrorMessagesUtil:

    @staticmethod
    def no_statitstics_between_date(starts: date, ends: date):
        return f"с {starts} по {ends} cтатистики не обнаружено"
