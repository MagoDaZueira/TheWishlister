import telebot
from keyring.backends.libsecret import available
from telebot.apihelper import get_chat

from source.API.Keys import Keys
from source.Chat import Chat, StandardAnswers, BotCommands


class TelegramAPI:

    def __init__(self):
        global bot
        bot = telebot.TeleBot(Keys.getTelegramAPIKey())

    def send_message(self, message, chat_id):
        self.bot.send_message(chat_id, message)

    @bot.message_handler(commands=["start"])
    def bem_vindo(self, message): #Isso aqui não é uma cópia direta do JP, confia.
        novo_chat = Chat(message.chat.id, message.chat.userName)

        bot.reply_to(
            message, "Ola! Eu sou o TheWishlister, um bot que irá te ajudar a saber quando seus jogos favorítos são lançados, buscar reviews de jogos e dar recomendações baseado nos jogos que você gosta.\n\n"
                     "Veja tudo o que posso fazer com /comandos"
        )

    @staticmethod
    def checkInitialized(message):
        chat = get_chat(message.chat.id)

        if chat is None:
            bot.reply_to(
                message, "Você não iniciou o chat comigo. Digite /start para começar.")
        return

    @bot.message_handler(commands=["comandos"])
    def comandos(self, message):
        checkInitialized(message)
        chat = get_chat(message.chat.id)
        bot.reply_to(message, StandardAnswers.ListCommands())

    @bot.message_handler(commands=["addJogo"])
    def addJogo(self, message):
        chat = get_chat(message.chat.id)
        bot.reply_to(message, StandardAnswers.addJogo())
        BotCommands.AddJogo()

    @bot.message_handler(commands=["delJogo"])
    def comandos(self, message):
        chat = get_chat(message.chat.id)
        bot.reply_to(message, StandardAnswers.ListCommands())

    @bot.message_handler(commands=["delTudo"])
    def comandos(self, message):
        chat = get_chat(message.chat.id)
        bot.reply_to(message, StandardAnswers.ListCommands())
