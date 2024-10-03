import WishlistManager as wm
from Metacritic import retrieve_info
from Maritaca import maritalk_review

class Chat:
    def __init__(self, chat_id, userName):
        self.chat_id  = chat_id
        self.userName = userName
        global usersDataBase


class StandardAnswers():
    _COMANDOS = {
        "/add": "Adiciona um jogo na sua wishlist.",
        "/review": "Gera um resumo das informações disponíveis no Metacritic do jogo.",
        "/remove": "Remove um jogo da wishlist.",
        "/removeAll": "Remove todos os jogos da wishlist.",
        "/list": "List todos os jogos da wishlist."

    }
    @staticmethod
    def ListCommands():
        answer = ""
        for key in StandardAnswers._COMANDOS.keys():
            answer += f"{key}:\n{StandardAnswers._COMANDOS[key]}\n\n"
        return answer


#TODO: Comando VerReviews, depende da parte do Arthur.
class BotCommands():
    @staticmethod
    def AddJogo(gameName):
        info = retrieve_info(gameName)
        if info:
            return 1
        return 0

    @staticmethod
    def RemoverJogo(gameName):
        wm.delete_from_wishlist(wm.wishlist_file, gameName)

    @staticmethod
    def RemoverTudo():
        wm.delete_all(wm.wishlist_file)

    @staticmethod
    def VerReviews(gameName):
        return maritalk_review(gameName)

    @staticmethod
    def ListarJogos():
        answer = f'Aqui estão os jogos da sua wishlist:\n\n'
        answer += wm.list_all(wm.wishlist_file)
        return answer
