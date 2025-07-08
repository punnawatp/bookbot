from stats import get_num_words
from stats import count_char
from stats import get_new_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    dict = count_char(text)
    print(get_new_list(dict))
    
main()