# A module for retrieving data of the city.

from typing import List

import requests
from requests.exceptions import JSONDecodeError

from config_data.config import RAPID_API_KEY
from main import logger


def get_city_info(src_city: str) -> str:
    """
    A function makes HTTP request and retrieve
    information of the specified city.
    :param src_city: the source city
    :returns: the city ID or the error message
    """

    url = "https://hotels4.p.rapidapi.com/locations/v3/search"

    querystring = {"q": src_city}

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    logger.info(f"City info response status code: {response.status_code}")

    # Check status code:
    if response.status_code != 200:
        return "Что-то пошло не так... Пожалуйста, повторите запрос:"

    try:
        response_json = response.json()
        regions: List[dict] = response_json["sr"]

        # If the inputted city not found:
        if not regions:
            return "Введённый город не найден. Пожалуйста, повторите запрос:"

        # If the inputted city exists:
        for region in regions:
            city_id = region.get("cityId", "")
            if city_id != "":
                return f"OK{city_id}"

        for region in regions:
            city_id = region.get("gaiaId", "")
            if city_id != "":
                return f"OK{city_id}"

    except (TypeError, JSONDecodeError):
        return "Введённый город не найден. Пожалуйста, повторите запрос:"
