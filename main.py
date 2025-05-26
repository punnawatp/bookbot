
from stats import get_num_words
from stats import get_dictionary
from stats import new_dict

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main(path):
    text = get_book_text(path)
    print(text)

#main("./books/frankenstein.txt")

frakenstein_text = get_book_text("./books/frankenstein.txt")

#print(get_num_words(frakenstein_text))

#print(get_dictionary(frakenstein_text))

print(new_dict(get_dictionary(frakenstein_text)))