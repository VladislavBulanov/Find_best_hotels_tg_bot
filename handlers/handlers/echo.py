# A module describing '/echo' command working.

from telebot.types import Message

from loader import bot
from main import logger


@bot.message_handler(func=lambda message: True)
def run_command_echo(message: Message) -> None:
    """A function launches a '/echo' command."""

    logger.info(f"The function 'echo' is called by {message.from_user.full_name}")
    bot.reply_to(
        message,
        "Простите, я не понял Вас. "
        "Чтобы узнать, что я умею, выберите "
        "в меню пункт 'Вывести справку' или напишите /help",
    )
