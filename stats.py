def get_num_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return f"{counter} words found in the document"

def count_char(text):
    lowered = text.lower()
    dict = {}
    for c in lowered:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
    return dict
         

