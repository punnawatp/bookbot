from stats import get_num_words
from stats import count_char

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print(count_char(text))

main()