# A module describing '/custom' command working.

from telebot.types import Message

from loader import bot
from utils.misc.steps.steps import run_command


@bot.message_handler(commands=["custom"])
def run_command_custom(message: Message) -> None:
    """A function launches a '/custom' command."""

    run_command(
        command_name="custom",
        src_message=message,
    )
