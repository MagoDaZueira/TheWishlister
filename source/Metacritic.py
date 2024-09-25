import requests
from bs4 import BeautifulSoup
from DataConverter import name_prepare, date_prepare
from WishlistManager import date_passed, write_to_wishlist


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

wishlist_file = "Wishlist"

def retrieve_info(game: str) -> dict:
    """
    Receives the name of a game and gathers information about it on Metacritic.
    
    The input is a string.

    If it succeeds, the return value is a dictionary, with:
    - Name: a string, the game's name;
    - Score: an integer, the game's Metascore
    - Date: a dict(str, int), with:
    - - Year
    - - Month
    - - Day
    - Reviews: a list of dicts, with:
    - - Name: Critic's name
    - - Score: Review score
    - - Summary: Snippet of the review
    - - Link: Link to the full review (if available, else "N/A")

    If the game hasn't been released yet, it returns 0.
    """

    # Checks for url formatting
    game_name = name_prepare(game)
    url = f'https://www.metacritic.com/game/{game_name}/'

    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        html_content = page.text
        soup = BeautifulSoup(html_content, 'html.parser')
    else:
        # Game's not on Metacritic
        print(f"Failed to retrieve the webpage. Status code: {page.status_code}")
        write_to_wishlist(wishlist_file, game, "TBD")
        return 0

    # Find the relevant divs in the html
    release_date_div = soup.find('span', text='Released On: ')
    metascore_div = soup.find('div', attrs={'title': lambda x: x and 'Metascore' in x})
    reviews = soup.find_all('div', class_='c-siteReview')
    release_date = "TBD"

    # Return dictionary
    game_info = {}
    game_info["Name"] = game

    if metascore_div:
        metascore_text = metascore_div['title']
        metascore = metascore_text.split()[1]
        game_info["Score"] = metascore

    if release_date_div:
        release_date_span = release_date_div.find_next('span')
        release_date = release_date_span.text.strip()
        game_info["Date"] = date_prepare(release_date)
    else:
        game_info["Date"] = "TBD"

    
    # Game has not been released yet
    if (game_info["Date"] == "TBD"):
        write_to_wishlist(wishlist_file, game, "TBD")
        return 0
    elif (not date_passed(game_info["Date"])):
        write_to_wishlist(wishlist_file, game, release_date)
        return 0
    

    # Will append dictionaries with reviews to this
    review_list = []

    for review in reviews:
        this_review = {}

        score_div = review.find('div', class_='c-siteReviewScore')
        score = score_div.find('span').text.strip() if score_div and score_div.find('span') else "N/A"

        reviewer_name_div = review.find('div', class_='c-siteReviewHeader')
        reviewer_name = reviewer_name_div.find('a', class_='c-siteReviewHeader_publicationName').text.strip() if reviewer_name_div and reviewer_name_div.find('a', class_='c-siteReviewHeader_publicationName') else "N/A"

        summary_div = review.find('div', class_='c-siteReview_quote')
        summary = summary_div.find('span').text.strip() if summary_div and summary_div.find('span') else "N/A"

        full_review_link_div = review.find('a', class_='c-siteReview_externalLink')
        full_review_link = full_review_link_div['href'] if full_review_link_div else "N/A"
        
        # Filters out user reviews
        if reviewer_name != "N/A":
            this_review["Name"] = reviewer_name
            this_review["Score"] = score
            this_review["Summary"] = summary
            this_review["Link"] = full_review_link
            review_list.append(this_review)
    
    game_info["Reviews"] = review_list
    
    return game_info



# # Example
# info = retrieve_info("Sludge Life")

# if (info):
#     print(info["Name"])
#     print(info["Score"])
#     print(info["Date"])
#     print(info["Reviews"])