# A module with function for validation the maximum price of the room.


def validate_maximum_price(
    amount_value: str,
    min_price: int,
) -> str:
    """
    A function validates inputted value of
    the maximum price of the room per day.
    :param amount_value: the inputted by user value of the maximum price
    :param min_price: the inputted by user value of the minimum price
    :returns: the status of validation: 'OK' or the error message
    """

    try:
        max_price = int(amount_value)

    except ValueError:
        return (
            "Некорректное значение. "
            "Пожалуйста, введите максимальную стоимость номера (в долларах):"
        )

    if max_price <= 0:
        return (
            "Значение должно быть положительным числом. "
            "Пожалуйста, введите максимальную стоимость номера (в долларах):"
        )

    if max_price < min_price:
        return (
            "Максимальная стоимость не может быть меньше минимальной. "
            "Пожалуйста, введите максимальную стоимость номера (в долларах):"
        )

    return "OK"
