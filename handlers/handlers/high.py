# A module describing '/high' command working.

from telebot.types import Message

from loader import bot
from utils.misc.steps.steps import run_command


@bot.message_handler(commands=["high"])
def run_command_high(message: Message) -> None:
    """A function launches a '/high' command."""

    run_command(
        command_name="high",
        src_message=message,
    )
