def main():
    from stats import word_count, letter_count, dict_sort
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    letters = letter_count(text)
    sorted_dict = dict_sort(letters)
    print(f"{count} words found in the document")
    print(sorted_dict)

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

main()