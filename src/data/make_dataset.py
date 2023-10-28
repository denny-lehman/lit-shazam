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
        