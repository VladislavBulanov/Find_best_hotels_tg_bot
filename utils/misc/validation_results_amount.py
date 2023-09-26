# A module with function for validate the amount of results.


def validate_results_amount(amount_value: str, limit: int) -> str:
    """
    A function validates inputted value of amount of results to show.
    :param amount_value: the inputted by user value of amount of results to show
    :param limit: the maximum amount of results to show
    :returns: the status of validation: 'OK' or the error message
    """

    try:
        results_to_show = int(amount_value)

    except ValueError:
        return (
            "Некорректное значение. "
            "Пожалуйста, введите количество результатов для показа "
            "(не больше десяти):"
        )

    if results_to_show > limit:
        return (
            "Значение превышает максимально допустимое. "
            "Пожалуйста, введите количество результатов для показа "
            "(не больше десяти):"
        )

    if results_to_show <= 0:
        return (
            "Значение должно быть положительным числом. "
            "Пожалуйста, введите количество результатов для показа "
            "(не больше десяти):"
        )

    return "OK"
