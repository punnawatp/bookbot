from stats import get_num_words
from stats import get_dictionary
from stats import sort_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    get_num_words(frakenstein_text)
    print(f"{num_words} words found in the document")



