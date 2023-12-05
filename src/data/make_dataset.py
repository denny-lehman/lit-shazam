import requests
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer

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
        print(f'could not find project gutenberg ending of {book}')
        raise ValueError
    last_character = match.start()
    return book[:last_character]

def remove_book_start(book:str)->str:
    """removes the boiler plate beginning part of the book in project gutenberg"""
    start_of_book_pattern = r'\*\*\* START OF THE PROJECT GUTENBERG EBOOK [\w\d\s]+ \*\*\*'
    match = re.search(start_of_book_pattern, book)
    if match is None:
        print(f'could not find project gutenberg beginning of {book}')
        raise ValueError
    first_character = match.end()
    return book[first_character:]

def remove_new_line_tabs(book):
    """remmove unwanted newlines, tabs, etc from the text"""
    for char in ["\n", "\r", "\d", "\t", "\s"]:
        book = book.replace(char, " ")
    return book


def convert_to_sentences(book, sentences_per_example=3):
    """returns a list of (sentences_per_example, author) pairs """
    sentences = sent_tokenize(book)
    total_clusters = int(len(sentences)/sentences_per_example)
    data = []
    for i in range(total_clusters):
        sentence_cluster = sentences[i*sentences_per_example:(i+1)*sentences_per_example]
        data += [''.join(sentence_cluster)]
        
    return data

def sentence_to_bag_of_words(sentence):
    """Converts words in a sentence into stemmed tokens"""
    # 1. lower case
    # 2. remove punctuation
    # 3. tokenize
    # 4. stem
    # 5. TODO: lem
    # 6. combine back together with spaces
    
    result = sentence.lower()
    

    tokenizer = RegexpTokenizer(r'\w+')
    token_list = tokenizer.tokenize(result)
    
    
    porter = PorterStemmer()
    porter_tokens = [porter.stem(token) for token in token_list]
    
    bag_of_words = ' '.join(porter_tokens)
    
    return bag_of_words
