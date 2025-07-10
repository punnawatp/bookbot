from stats import get_num_words
from stats import count_char
from stats import get_new_list
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
        num_words = get_num_words(text)
        print(f"Found {num_words} total words")
        dict = count_char(text)
        new_list = get_new_list(dict)
        for word in new_list:
            print(word["char"] + ":", word["num"])
    
main()