# A module for the checking result of validation and the choosing next step.

from datetime import datetime
from logging import Logger
from typing import Callable, Union

from telebot import TeleBot


def check_validation_result_and_register_next_step(
    chat_id: int,
    validation_result_object: Union[datetime.date, str],
    type_of_validation: str,  # "city", "date" or "integer"
    src_logger: Logger,
    src_bot: TeleBot,
    not_success_function: Callable,
    success_function: Callable = None,
    success_message: str = None,
) -> Union[str, datetime.date, None]:
    """
    A function receives the object which was returned by validating function.
    If validation is not good the current step will be repeated (not_success_function
    will be called), function returns None. If validation is good the next step is
    registered (success_function will be called), function returns the data to
    record in user state object.
    :param chat_id: the ID of the chat with current user
    :param validation_result_object: the object which was returned by validating function
    :param type_of_validation: the type of validation (str): "city", "date" or "integer"
    :param src_logger: the source logger
    :param src_bot: the source Telegram bot object
    :param not_success_function: the function which will be called if validation is not good
    :param success_function: the function which will be called if validation is good
    :param success_message: the message which will be sent to user if validation is good
    :return: None if validation is not good, else string or 'datetime' object
    """

    if type_of_validation == "city":
        # Validation is good:
        if validation_result_object[:2] == "OK":
            data_to_record = validation_result_object[2:]
            msg = src_bot.send_message(chat_id, success_message)
            src_bot.register_next_step_handler(msg, success_function)
            return data_to_record

        # Validation is not good:
        else:
            msg = src_bot.send_message(chat_id, validation_result_object)
            src_logger.error(f"Error: {validation_result_object}")
            src_bot.register_next_step_handler(msg, not_success_function)
            return

    elif type_of_validation == "date":
        # Validation is not good:
        if isinstance(validation_result_object, str):
            msg = src_bot.send_message(chat_id, validation_result_object)
            src_logger.error(f"Error: {validation_result_object}")
            src_bot.register_next_step_handler(msg, not_success_function)
            return

        # Validation is good:
        else:
            msg = src_bot.send_message(chat_id, success_message)
            src_bot.register_next_step_handler(msg, success_function)
            return validation_result_object

    elif type_of_validation == "integer":
        # Validation is not good:
        if validation_result_object != "OK":
            msg = src_bot.send_message(chat_id, validation_result_object)
            src_logger.error(f"Error: {validation_result_object}")
            src_bot.register_next_step_handler(msg, not_success_function)
            return

        # Validation is good:
        else:
            if success_function:
                msg = src_bot.send_message(chat_id, success_message)
                src_bot.register_next_step_handler(msg, success_function)
            return validation_result_object
