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