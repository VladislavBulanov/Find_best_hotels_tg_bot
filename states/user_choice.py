# A module describing class for record parameters chosen by user.

from datetime import datetime


class UserChoice:
    """A class for record parameters chosen by user."""

    def __init__(
        self,
        city_id: str = None,
        checkin_date: datetime.date = None,
        checkout_date: datetime.date = None,
        guests_amount: int = None,
        results_amount: int = None,
        min_price: int = 25,
        max_price: int = 10000,
    ) -> None:
        """
        The class constructor.
        :param city_id: the ID of chosen city
        :param checkin_date: the date of check-in at the hotel
        :param checkout_date: the date of check-out at the hotel
        :param guests_amount: the quantity of guests
        :param results_amount: the quantity of results to show
        :param min_price: the minimum price of the room per day
        :param max_price: the maximum price of the room per day
        """

        self.city_id = city_id
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.guests_amount = guests_amount
        self.results_amount = results_amount
        self.min_price = min_price
        self.max_price = max_price
