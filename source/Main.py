from API.TelegramAPI import TelegramAPI
from dotenv import load_dotenv
from Scheduler import read_from_wishlist

def main():
    load_dotenv() #Só pra garantir...
    read_from_wishlist("Wishlist")
    telebot = TelegramAPI()
    
    telebot.start()
    while True:
        continue #Deixa o bot ligado sempre (a ideia é usar esse looping posteriormente pra um scheduler talvez.)

        # A ideia principal é talvez usar esse while loop como um scheduler.

if __name__ == "__main__":
    main()
