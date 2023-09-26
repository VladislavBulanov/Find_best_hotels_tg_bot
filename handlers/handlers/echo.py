from telebot.types import Message

from loader import bot


@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.reply_to(
        message,
        "Простите, я не понял Вас. "
        "Чтобы узнать, что я умею, выберите "
        "в меню пункт 'Вывести справку' или напишите /help",
    )
