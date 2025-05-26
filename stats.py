def get_num_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return f"{counter} words found in the document"

def get_dictionary(text):
    lower_case_text = text.lower()
    unique_letters = set()
    
    for char in lower_case_text:
        unique_letters.add(char)

    dictionary = {}

    for uni_char in unique_letters:
        counter = 0
        for char in lower_case_text:
            if char == uni_char:
                counter += 1
        dictionary[uni_char] = counter
    
    return dictionary


def new_dict(dict):
    result = []
    for c, n in dict.items():
        new_dict = {}
        new_dict["char"] = c
        new_dict["num"] = n
        result.append(new_dict)
    return result
