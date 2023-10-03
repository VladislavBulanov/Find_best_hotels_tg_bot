# A module with function for validate check-out date.

from datetime import datetime, timedelta
from typing import Union


def validate_checkout_date(
    src_checkout_date: str,
    src_checkin_date: datetime.date,
) -> Union[datetime.date, str]:
    """
    A function validates inputted value of check-out date
    by user and tries to convert it in 'datetime.date' object.
    :param src_checkout_date: the inputted by user check-out date
    :param src_checkin_date: the inputted by user check-in date
    :returns: 'datetime.date' object if date is valid,
    error message if it isn't
    """

    try:
        checkout_date = datetime.strptime(src_checkout_date, "%d.%m.%y").date()

        if checkout_date <= src_checkin_date:
            return (
                "Дата выселения меньше или совпадает с датой заселения. "
                "Пожалуйста, введите дату в формате ДД.ММ.ГГ:"
            )

        if checkout_date > datetime.now().date() + timedelta(days=366):
            return (
                "Бронирование отелей доступно в пределах "
                "календарного года от текущей даты. "
                "Пожалуйста, введите дату в формате ДД.ММ.ГГ:"
            )

        return checkout_date

    except ValueError:
        return (
            "Некорректный формат даты. " "Пожалуйста, введите дату в формате ДД.ММ.ГГ:"
        )
