# A module with function for validate check-in date.

from datetime import datetime
from typing import Union


def validate_checkin_date(src_date: str) -> Union[datetime.date, str]:
    """
    A function validates inputted value of check-in date
    by user and tries to convert it in 'datetime.date' object.
    :param src_date: the inputted by user check-in date
    :returns: 'datetime.date' object if date is valid,
    error message if it isn't
    """

    try:
        checkin_date = datetime.strptime(src_date, "%d.%m.%y").date()

        if checkin_date < datetime.now().date():
            return (
                "Дата приходится на прошлое. "
                "Пожалуйста, введите дату в формате ДД.ММ.ГГ:"
            )

        return checkin_date

    except ValueError:
        return (
            "Некорректный формат даты. " "Пожалуйста, введите дату в формате ДД.ММ.ГГ:"
        )
