from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot

from main import logger


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    logger.info(f"The command '/help' is called by {message.from_user.full_name}")
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))
