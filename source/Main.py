from API.TelegramAPI import TelegramAPI

def main():
    telebot = TelegramAPI()
    
    telebot.start()
    while True:
        continue #Deixa o bot ligado sempre (a ideia é usar esse looping posteriormente pra um scheduler talvez.)

        # A ideia principal é talvez usar esse while loop como um scheduler.

if __name__ == "__main__":
    main()
