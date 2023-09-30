# A module with functions which describe the working of program at each step.

from typing import List, Union

from telebot.types import Message

from loader import bot
from main import logger
from states.user_choice import UserChoice
from utils.misc.city_info import get_city_info
from utils.misc.hotel_info import get_hotel_info
from utils.misc.offers import get_offers
from utils.misc.steps.next_step_registration import \
    check_validation_result_and_register_next_step
from utils.misc.validations.validation_checkin_date import \
    validate_checkin_date
from utils.misc.validations.validation_checkout_date import \
    validate_checkout_date
from utils.misc.validations.validation_guests_amount import \
    validate_guests_amount
from utils.misc.validations.validation_results_amount import \
    validate_results_amount

USER_CHOICE = UserChoice()  # A 'UserChoice' class instance,
# which consists of chosen parameters by user like city, dates, etc.
# for send request to get suitable proposal of hotels


def run_command(
    command_name: str,
    src_message: Message,
) -> None:
    """
    A function runs the sequence of steps
    corresponding to the specified command.
    :param command_name: the command name
    :param src_message: the source message
    """

    def request_city_and_country(message: Message) -> None:
        """A function requests the user for the city and the country."""

        logger.info(f"The command '/{command}' is launched by {message.from_user.full_name}")

        # Send message to user for request city and country:
        msg = bot.send_message(
            message.chat.id,
            "Введите город и страну через пробел (пример: Москва Россия):",
        )

        bot.register_next_step_handler(
            msg,
            validate_city_and_request_checkin_date,
        )

    def validate_city_and_request_checkin_date(message: Message) -> None:
        """A function validates a city inputted by user,
        requests it again if something is wrong and
        then requests the user for the check-in date."""

        logger.info(f"{message.from_user.full_name}'s message: {message.text}")

        city: str = get_city_info(message.text)

        result = check_validation_result_and_register_next_step(
            chat_id=message.chat.id,
            validation_result_object=city,
            type_of_validation="city",
            src_logger=logger,
            src_bot=bot,
            not_success_function=validate_city_and_request_checkin_date,
            success_function=validate_checkin_date_and_request_checkout_date,
            success_message="Введите желаемую дату заселения (в формате ДД.ММ.ГГ):",
        )

        if result:
            USER_CHOICE.city_id = result
            logger.info(f"City ID: {USER_CHOICE.city_id}")

    def validate_checkin_date_and_request_checkout_date(message: Message) -> None:
        """A function validates check-in date,
        records it if date is valid or requests date again,
        and requests checkout date."""

        logger.info(f"{message.from_user.full_name}'s message: {message.text}")

        # Validate check-in date:
        checkin_date = validate_checkin_date(src_date=message.text)

        result = check_validation_result_and_register_next_step(
            chat_id=message.chat.id,
            validation_result_object=checkin_date,
            type_of_validation="date",
            src_logger=logger,
            src_bot=bot,
            not_success_function=validate_checkin_date_and_request_checkout_date,
            success_function=validate_checkout_date_and_request_guests_amount,
            success_message="Введите желаемую дату выселения (в формате ДД.ММ.ГГ):",
        )

        if result:
            USER_CHOICE.checkin_date = result
            logger.info(f"Check-in date: {USER_CHOICE.checkin_date}")

    def validate_checkout_date_and_request_guests_amount(message: Message) -> None:
        """A function validates check-out date,
        records it if date is valid or requests date again,
        and requests the amount of guests."""

        logger.info(f"{message.from_user.full_name}'s message: {message.text}")

        # Validate check-out date:
        checkout_date = validate_checkout_date(
            src_checkout_date=message.text,
            src_checkin_date=USER_CHOICE.checkin_date,
        )

        result = check_validation_result_and_register_next_step(
            chat_id=message.chat.id,
            validation_result_object=checkout_date,
            type_of_validation="date",
            src_logger=logger,
            src_bot=bot,
            not_success_function=validate_checkout_date_and_request_guests_amount,
            success_function=validate_guests_amount_and_request_results_amount,
            success_message="Введите количество гостей:",
        )

        if result:
            USER_CHOICE.checkout_date = result
            logger.info(f"Check-out date: {USER_CHOICE.checkout_date}")

    def validate_guests_amount_and_request_results_amount(message: Message) -> None:
        """A function validates the amount of guests,
        records it if amount is valid or requests amount again,
        and requests the amount of results to show."""

        logger.info(f"{message.from_user.full_name}'s message: {message.text}")

        # Validate amount of guests:
        guests_amount = message.text
        validation_result = validate_guests_amount(amount_value=guests_amount)

        result = check_validation_result_and_register_next_step(
            chat_id=message.chat.id,
            validation_result_object=validation_result,
            type_of_validation="integer",
            src_logger=logger,
            src_bot=bot,
            not_success_function=validate_guests_amount_and_request_results_amount,
            success_function=validate_results_amount_and_get_results,
            success_message="Введите количество результатов для показа (не больше десяти):",
        )

        if result:
            USER_CHOICE.guests_amount = int(guests_amount)
            logger.info(f"Guests amount: {USER_CHOICE.guests_amount}")

    def validate_results_amount_and_get_results(message: Message) -> None:
        """A function validates the amount of results,
        records it if amount is valid or requests amount again,
        and make HTTP request to get results."""

        logger.info(f"{message.from_user.full_name}'s message: {message.text}")

        # Validate amount of results:
        results_amount = message.text
        validation_result = validate_results_amount(
            amount_value=results_amount,
            limit=10,
        )

        result = check_validation_result_and_register_next_step(
            chat_id=message.chat.id,
            validation_result_object=validation_result,
            type_of_validation="integer",
            src_logger=logger,
            src_bot=bot,
            not_success_function=validate_results_amount_and_get_results,
        )

        if result:
            USER_CHOICE.results_amount = int(results_amount)
            logger.info(f"Results amount: {USER_CHOICE.results_amount}")

            # Make HTTP request and retrieve data with results:
            data: Union[List[dict], str] = get_offers(
                city_id=USER_CHOICE.city_id,
                checkin_date=USER_CHOICE.checkin_date,
                checkout_date=USER_CHOICE.checkout_date,
                guests_amount=USER_CHOICE.guests_amount,
                results_amount=USER_CHOICE.results_amount,
                min_price=USER_CHOICE.min_price,
                max_price=USER_CHOICE.max_price,
                sort_type="PRICE_LOW_TO_HIGH" if command == "low" else "PRICE_RELEVANT",
            )

            # Show the results or the error message:
            if isinstance(data, List):
                if data:
                    qty = 0
                    for hotel in data:
                        name, price, site_url = get_hotel_info(hotel)
                        bot.send_message(
                            message.chat.id,
                            f"{name}\n"
                            f"Цена за сутки: {price}\n"
                            f"Узнать подробности:\n{site_url}",
                        )
                        qty += 1
                    logger.info(f"The {qty} results are shown")
                    logger.info(f"The command '/{command}' is completed")
                else:
                    bot.send_message(
                        message.chat.id,
                        "По Вашему запросу не найдено ни одного варианта",
                    )
                    logger.info("No matches")
                    logger.info(f"The command '/{command}' is completed")

            # Show error message:
            else:
                bot.send_message(
                    message.chat.id,
                    data,
                )
                logger.error(f"Error: {data}")
                logger.info(f"The command '/{command}' is completed")

    command = command_name
    request_city_and_country(src_message)
