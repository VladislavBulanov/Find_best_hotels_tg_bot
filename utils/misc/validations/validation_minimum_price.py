# A module with function for validation the minimum price of the room.


def validate_minimum_price(amount_value: str) -> str:
    """
    A function validates inputted value of
    the minimum price of the room per day.
    :param amount_value: the inputted by user value of the minimum price
    :returns: the status of validation: 'OK' or the error message
    """

    try:
        min_price = int(amount_value)

    except ValueError:
        return (
            "Некорректное значение. "
            "Пожалуйста, введите минимальную стоимость номера (в долларах):"
        )

    if min_price <= 0:
        return (
            "Значение должно быть положительным числом. "
            "Пожалуйста, введите минимальную стоимость номера (в долларах):"
        )

    return "OK"
