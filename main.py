# A main script of the project.

import logging

from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands

logger = logging.getLogger("main")


if __name__ == "__main__":
    logging.basicConfig(
        filename="logs.log",
        filemode="a",
        format="%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )
    logger.info("==================THE SERVER IS LAUNCHED==================")
    set_default_commands(bot)
    bot.infinity_polling()
