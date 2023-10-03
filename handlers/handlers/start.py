# A module describing '/start' command working.

from telebot.types import Message

from loader import bot
from main import logger


@bot.message_handler(commands=["start"])
def run_command_start(message: Message) -> None:
    """A function launches a '/start' command."""

    logger.info(f"The command '/start' is called by {message.from_user.full_name}")
    bot.reply_to(
        message,
        f"Привет, {message.from_user.full_name}!\n"
        "Я бот, который поможет Вам найти "
        "лучший отель в указанном городе. "
        "Чтобы узнать, что я умею, выберите в меню пункт 'Вывести справку' "
        "или напишите /help",
    )
    logger.info(f"The command '/start' is completed")
