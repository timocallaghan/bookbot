def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letters_total = text.lower()
    letters_dict = {}
    for letter in letters_total:
        if letter in letters_dict:
            letters_dict[letter] +=1
        else:
            letters_dict[letter] = 1
    return letters_dict

def sort_on(dict):
    return dict["num"]

def dict_sort(dictionary):
    dict_list =[]
    for key in dictionary:
        if key.isalpha():
            dict_list.append({"char": key, "num": dictionary[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
