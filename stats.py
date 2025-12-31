def count_words(text):
    return len(text.split()) # Split string into list of words, return length.

def count_chars(text):
    char_count = {}
    lower_text = str.lower(text)
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_dict_list(dict):
    char_list = []
    
    for key in dict:
        if key.isalpha():
            char_list.append({"char": key, "num": dict[key]})
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list

