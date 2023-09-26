# A module for retrieving detailed information of specified hotel.

from typing import Tuple


def get_hotel_info(src_hotel: dict) -> Tuple[str, str, str]:
    """
    A function retrieves detailed information of specified hotel.
    :param src_hotel: the dictionary with data of specified hotel
    :returns: the tuple with hotel name, price and URL to the site
    for getting more information and order
    """

    name = src_hotel["name"]
    price = src_hotel["mapMarker"]["label"]
    property_id = src_hotel["id"]
    site_url = f"https://www.expedia.com/.h{property_id}.Hotel-Information"

    return name, price, site_url
