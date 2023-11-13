from datetime import datetime


class DateHelper:

    @staticmethod
    def convert_default(date: str):

        # Convertendo para o formato datetime
        date_time = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")

        return date_time.strftime("%d%m%Y")

