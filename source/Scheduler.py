import WishlistManager as wm
import shelve
import Metacritic as mt
import os
from DataConverter import date_prepare


def read_from_wishlist(filename: str):
    with shelve.open(filename) as db:
        os.system("start cmd.exe /k echo Bot funcionando")
        for game in db:

            print(game)
            print(db[game])
            if (db[game] == "TBD"):
                mt.retrieve_info(game)
        
            date = date_prepare(db[game])
            if wm.date_passed(date):
                print("mandar review")
                wm.delete_from_wishlist(filename, game)
    

                

