"""A module with SQLAlchemy models which describe requests history."""

from typing import Dict

from sqlalchemy import Column, Date, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config_data.config import DEFAULT_COMMANDS

engine = create_engine("sqlite:///database/requests_history.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
commands: Dict[str, str] = {
    command[0]: command[1] for command in DEFAULT_COMMANDS
}


class Requests(Base):
    """A model describes the table with history of requests."""

    __tablename__ = "requests"

    request_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    request_datetime = Column(DateTime, nullable=False)
    command = Column(String, nullable=False)
    city = Column(String, nullable=False)
    checkin_date = Column(Date, nullable=False)
    checkout_date = Column(Date, nullable=False)
    min_price = Column(Integer, default=None)
    max_price = Column(Integer, default=None)
    guests_qty = Column(Integer, nullable=False)
    results_qty = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        """The text presentation of the data."""

        return (
            f"\nДата и время: {self.request_datetime.strftime('%d-%m-%Y %H:%M:%S')}"
            f"\nКоманда: '{commands[self.command]}'"
            f"\nВыбранный город: {self.city}"
            f"\nДата заселения: {self.checkin_date.strftime('%d-%m-%Y')}"
            f"\nДата выселения: {self.checkout_date.strftime('%d-%m-%Y')}"
            f"\nМин. стоимость: {self.min_price}$"
            f"\nМакс. стоимость: {self.max_price}$"
            f"\nКоличество гостей: {self.guests_qty} чел."
            f"\nРезультатов к показу: {self.results_qty}\n"
        )
