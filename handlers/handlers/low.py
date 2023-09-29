# A module describing '/low' command working.

from telebot.types import Message

from loader import bot
from utils.misc.steps.steps import run_command


@bot.message_handler(commands=["low"])
def run_command_low(message: Message) -> None:
    """A function launches a '/low' command."""

    run_command(
        command_name="low",
        src_message=message,
    )
