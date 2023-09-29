# A module with function for validate the amount of guests.


def validate_guests_amount(amount_value: str) -> str:
    """
    A function validates inputted value of amount of guests.
    :param amount_value: the inputted by user value of amount of guests
    :returns: the status of validation: 'OK' or the error message
    """

    try:
        guests_amount = int(amount_value)

    except ValueError:
        return "Некорректное значение. " "Пожалуйста, введите количество гостей:"

    if guests_amount <= 0:
        return (
            "Значение должно быть положительным числом. "
            "Пожалуйста, введите количество гостей:"
        )

    if guests_amount > 5:
        return (
            "Значение не должно превышать пять человек. "
            "Пожалуйста, введите количество гостей:"
        )

    return "OK"
