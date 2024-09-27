import telebot
from telebot.apihelper import get_chat

from API.Keys import Keys
from Chat import Chat, StandardAnswers, BotCommands


class TelegramAPI:

    def __init__(self):
        self.bot = telebot.TeleBot(Keys.getTelegramKey()) # F keys...
        self.set_handlers()

    def set_handlers(self):
        @self.bot.message_handler(commands=["start"])
        def bem_vindo(message): #Isso aqui não é uma cópia direta do JP, confia.
            novo_chat = Chat(message.chat.id, message.chat.username)

            self.bot.reply_to(
            message, "Ola! Eu sou o TheWishlister, um bot que irá te ajudar a saber quando seus jogos favorítos são lançados, buscar reviews de jogos e dar recomendações baseado nos jogos que você gosta.\n\n"
                     "Veja tudo o que posso fazer com /comandos"
        )

        @self.bot.message_handler(commands=["comandos"])
        def comandos(message):
            if not self.check_initialized(message):
                return
            self.bot.reply_to(message, StandardAnswers.ListCommands())

        @self.bot.message_handler(commands=["addJogo"])
        def add_jogo(message):
            if not self.check_initialized(message):
                return
            self.bot.reply_to(message, StandardAnswers.addJogo())
            BotCommands.AddJogo()

    def check_initialized(self, message):
        try:
            chat = self.bot.get_chat(message.chat.id)

            if chat is None:
                self.bot.reply_to(
                    message, "Você não iniciou o chat comigo. Digite /start para começar."
                )
                return False

        except telebot.apihelper.ApiException as e:
            self.bot.reply_to(
                message, "Ocorreu um erro ao tentar acessar o chat. Digite /start para iniciar."
            )
            return False

        return True


    def send_message(self, message, chat_id):
        self.bot.send_message(chat_id, message)

    def start(self):
        self.bot.polling()
