# A module for retrieving data with available hotels by specified filters.

from datetime import datetime
from typing import List, Union

import requests
from requests.exceptions import JSONDecodeError

from config_data.config import RAPID_API_KEY
from main import logger


def get_offers(
    city_id: str,
    checkin_date: datetime.date,
    checkout_date: datetime.date,
    guests_amount: int,
    results_amount: int,
    min_price: int,
    max_price: int,
    sort_type: str,
) -> Union[List[dict], str]:
    """
    A function retrieves data with available hotels by specified filters.
    :param city_id: the city ID
    :param checkin_date: the check-in date
    :param checkout_date: the check-out date
    :param guests_amount: the amount of the guests
    :param results_amount: the amount of the results to show
    :param min_price: the minimum price of the room per day
    :param max_price: the maximum price of the room per day
    :param sort_type: the type of sorting results
    :returns: the list with properties or the error message
    """

    url = "https://hotels4.p.rapidapi.com/properties/v2/list"

    payload = {
        "currency": "USD",
        "siteId": 300000001,
        "destination": {"regionId": city_id},
        "checkInDate": {
            "day": checkin_date.day,
            "month": checkin_date.month,
            "year": checkin_date.year,
        },
        "checkOutDate": {
            "day": checkout_date.day,
            "month": checkout_date.month,
            "year": checkout_date.year,
        },
        "rooms": [{"adults": guests_amount, "children": []}],
        "resultsStartingIndex": 0,
        "resultsSize": results_amount,
        "sort": sort_type,
        "filters": {"price": {"max": max_price, "min": min_price}},
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
    }

    response = requests.post(url, json=payload, headers=headers)
    logger.info(f"Offers retrieving response status code: {response.status_code}")

    # Check status code:
    if response.status_code != 200:
        return "Что-то пошло не так... Пожалуйста, повторите запрос:"

    try:
        response_json = response.json()
        return response_json["data"]["propertySearch"]["properties"]

    except (TypeError, JSONDecodeError):
        return "По Вашему запросу не найдено ни одного варианта"
