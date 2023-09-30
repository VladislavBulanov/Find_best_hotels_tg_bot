from telebot.types import Message

from loader import bot
from main import logger


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    logger.info(f"The command '/start' is called by {message.from_user.full_name}")
    bot.reply_to(
        message,
        f"Привет, {message.from_user.full_name}!\n"
        "Я бот, который поможет Вам найти лучший "
        "отель в указанном городе за лучшую цену. "
        "Чтобы узнать, что я умею, выберите в меню пункт 'Вывести справку' "
        "или напишите /help",
    )
