from typing import Dict

import requests


def _make_response(
    method: str,
    url: str,
    headers: Dict,
    params: Dict,
    timeout: int,
    success=200,
):
    """TODO"""

    response = requests.request(
        method=method,
        url=url,
        headers=headers,
        params=params,
        timeout=timeout,
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code


def _get_date_fact(
    method: str,
    url: str,
    headers: Dict,
    params: Dict,
    date_day: str,
    date_month: str,
    timeout: int,
    func=_make_response,
):
    """TODO"""

    url = "{0}/{1}/{2}/date".format(
        url,
        date_month,
        date_day,
    )

    response = func(
        method=method,
        url=url,
        headers=headers,
        params=params,
        timeout=timeout,
    )

    return response


def _get_math_fact(
    method: str,
    url: str,
    headers: Dict,
    params: Dict,
    number: int,
    timeout: int,
    func=_make_response,
):
    """TODO"""

    url = "{0}/{1}/math".format(
        url,
        number,
    )

    response = func(
        method=method,
        url=url,
        headers=headers,
        params=params,
        timeout=timeout,
    )

    return response


class SiteApiInterface:
    """TODO"""

    @staticmethod
    def get_date_fact():
        """TODO"""
        return _get_date_fact

    @staticmethod
    def get_math_fact():
        """TODO"""
        return _get_math_fact


if __name__ == "__main__":
    _make_response()
    _get_date_fact()
    _get_math_fact()

    SiteApiInterface()
