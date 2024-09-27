import pandas as pd


class Chat:
    def __init__(self, chat_id, userName):
        self.chat_id  = chat_id
        self.userName = userName
        global usersDataBase


#TODO: Add os outros comandos e funcionalidades do bot
class StandardAnswers():
    _COMANDOS = {
        "/add": "Adiciona um jogo na sua Wishlist.",
        "/review": "Gera um resumo de todas as Reviews disponíveis no MetaCritic do jogo.",
        "/remove": "Remove um jogo da wishlist.",
        "/removeAll": "Remove todos os jogos da wishlist.",
        "/list": "List todos os jogos da wishlist."

    }
    @staticmethod
    def ListCommands():
        answer = ""
        for key in StandardAnswers._COMANDOS.keys():
            answer += f"/{key}:\n{StandardAnswers._COMANDOS[key]}\n\n"
        return answer
    
    #TODO: Terminar a parte de listagem de todos os jogos, mas pra isso, precisa definir como eles serão guardados.
    @staticmethod
    def ListGames():
        answer = ""


#TODO: Implementar os comandos do bot aqui.
class BotCommands():
    @staticmethod
    def AddJogo():
        pass

    def RemoverJogo(gameName):
        pass

    def RemoverTudo():
        pass

    def ResumirReview(gameName):
        pass

    @staticmethod
    def VerReviews():
        pass

