from datetime import datetime
import csv
import shelve


def date_passed(date: dict) -> bool:
    """
    Receives a dictionary with keys:
    - Year
    - Month
    - Day
    And returns a bool, indicating whether
    we're equal/beyond that date
    """

    current_date = datetime.now()
    target_date = datetime(date["Year"], date["Month"], date["Day"])

    if target_date > current_date:
        return False
    
    return True



def write_to_wishlist(file_name: str, game: str, date: str) -> None:
    """
    Writes a game's name and its release date to a
    wishlist db file, using the shelve library.

    Receives three string inputs:
    - file_name: the file to write to (without .db at the end, only the prefix)
    - game: the game's name
    - date: the game's release date
    
    Returns nothing
    """

    with shelve.open(file_name) as db:
        db[game] = date


def delete_from_wishlist(file_name: str, game: str) -> None:
    """
    Deletes a game's entry from the wishlist shelve file.
    
    - file_name: the shelve file to modify (without .db at the end, only the prefix)
    - game: the game's name to delete
    
    Returns nothing
    """
    with shelve.open(file_name) as db:
        if game in db:
            del db[game]
            print(f"{game} has been removed from the wishlist.")
        else:
            print(f"{game} not found in the wishlist.")


def delete_all(file_name: str) -> None:
    """
    Deletes all the games in a wishlist shelve file.
    
    - file_name: the shelve file to clear (without .db at the end, only the prefix)
    
    Returns nothing
    """
    with shelve.open(file_name) as db:
        for key in db:
            delete_from_wishlist(file_name, key)