import requests

def get_book(url:str):
    """Requests a book from project gutenberg and returns the string as text
    Args
        url - the website url, normally ending in .txt
    Returns
        book - the text of the book
    """
    
    assert type(url) == str and url, 'URL must be a string and cannot be empty'
    
    raw_str_url = r"{}".format(url) # make raw string, otherwise / will make escape character
    try:
        r = requests.get(raw_str_url)
    
        # do url handling here
        book = r.text
        return book
    except Exception as e:
        print(str(e))
        return None
        
# all books in project gutenberg end with 
# *** END OF THE PROJECT GUTENBERG EBOOK {Title} ***
# *** END OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***

import re
def remove_bookend(book:str)->str:
    """removes the extra end of the book in project gutenberg"""
    end_of_book_pattern = r'\*\*\* END OF THE PROJECT GUTENBERG EBOOK [\w\d\s]+ \*\*\*'
    match = re.search(end_of_book_pattern, book)
    if match is None:
        print('could not find project gutenberg ending')
        raise ValueError
    last_character = match.start()
    return book[:last_character]