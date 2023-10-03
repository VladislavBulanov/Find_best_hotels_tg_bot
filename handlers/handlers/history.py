# A module describing '/history' command working.

from sqlalchemy import desc
from telebot.types import Message

from database.models import Requests, session
from loader import bot
from main import logger


@bot.message_handler(commands=["history"])
def run_command_history(message: Message) -> None:
    """A function launches a '/history' command."""

    user_name = message.from_user.full_name
    logger.info(f"The command '/history' is launched by {user_name}")

    # Try to get requests history of user:
    try:
        requests: list = (
            session.query(Requests)
            .filter_by(user_name=user_name)
            .order_by(desc(Requests.request_datetime))
            .limit(10)
            .all()
        )

        # If user did at least one request:
        if requests:
            result_message = f"История Ваших запросов (последние десять):\n"
            for request in requests:
                result_message += str(request)
            bot.send_message(message.chat.id, result_message)
            logger.info("The history is successfully shown")

        # If user didn't any request:
        else:
            bot.send_message(
                message.chat.id,
                "Вы ещё не сделали ни одного запроса",
            )
            logger.info("The history is clear")

    except BaseException as exc:
        bot.send_message(
            message.chat.id,
            "Ошибка на сервере. Пожалуйста, повторите запрос",
        )
        logger.error(f"Error: {exc}")

    finally:
        logger.info(f"The command '/history' is completed")
