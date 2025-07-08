def get_num_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return f"{counter} words found in the document"


