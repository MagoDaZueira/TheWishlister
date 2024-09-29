import os

class Keys:
    @staticmethod
    def getTelegramKey():
        telegram_key = os.getenv('TELEGRAM_API_KEY')
        if telegram_key is None:
            raise ValueError("A variável de ambiente 'TELEGRAM_API_KEY' não está definida.")
        return telegram_key

    @staticmethod
    def getMaritacaKey():
        maritaca_key = os.getenv('MARITACA_API_KEY')
        if maritaca_key is None:
            raise ValueError("A variável de ambiente 'MARITACA_API_KEY' não está definida.")
        return maritaca_key
