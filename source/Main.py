from API.TelegramAPI import TelegramAPI
from dotenv import load_dotenv
from Scheduler import read_from_wishlist

def main():
    load_dotenv()
    read_from_wishlist("Wishlist")
    telebot = TelegramAPI()
    
    telebot.start()
    while True:
        continue

if __name__ == "__main__":
    main()
