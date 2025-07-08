def get_num_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def count_char(text):
    lowered = text.lower()
    dict = {}
    for character in lowered:
        if character not in dict:
            dict[character] = 1
        else:
            dict[character] += 1
    return dict

def sort_on(item):
    return item["num"]

def get_new_list(dict):
    new_list = []
    for character, count in dict.items():
        new_dict = {"char": character, "num": count}
        if new_dict["char"].isalpha():
            new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list
