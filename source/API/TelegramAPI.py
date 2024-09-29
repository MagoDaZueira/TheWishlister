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

        @self.bot.message_handler(commands=["add"])
        def add_jogo(message):
            if not self.check_initialized(message):
                return

            # Extract the game name from the message
            try:
                game_name = message.text.split(" ", 1)[1]  # Split by space and get the second part (game name)
                already_released = BotCommands.AddJogo(game_name)
                
                if already_released:
                    self.bot.reply_to(message, f'Esse jogo já foi lançado!\nUse /review caso queira que eu te dê informações sobre ele.')
                else:
                    self.bot.reply_to(message, f"Adicionando {game_name} à sua wishlist.")

            except IndexError:
                self.bot.reply_to(message, "Por favor, insira o nome do jogo após o comando /add.")

        @self.bot.message_handler(commands=["remove"])    
        def remover_jogo(message):
            if not self.check_initialized(message):
                return

            # Extract the game name from the message
            try:
                game_name = message.text.split(" ", 1)[1]  # Split by space and get the second part (game name)
                self.bot.reply_to(message, f"Removendo {game_name} da sua wishlist.")
                BotCommands.RemoverJogo(game_name)

            except IndexError:
                self.bot.reply_to(message, "Por favor, insira o nome do jogo após o comando /remove.")
            except KeyError:
                self.bot.reply_to(message, f"{game_name} não está na sua wishlist.")

        @self.bot.message_handler(commands=["removeAll"])    
        def remover_tudo(message):
            if not self.check_initialized(message):
                return

            self.bot.reply_to(message, f"Removendo todos os jogos da sua wishlist.")
            BotCommands.RemoverTudo()

        @self.bot.message_handler(commands=["removeAll"])    
        def remover_tudo(message):
            if not self.check_initialized(message):
                return

            self.bot.reply_to(message, f"Removendo todos os jogos da sua wishlist.")
            BotCommands.RemoverTudo()

        @self.bot.message_handler(commands=["list"])    
        def listar_jogos(message):
            if not self.check_initialized(message):
                return

            listagem = BotCommands.ListarJogos()
            self.bot.reply_to(message, listagem)


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
