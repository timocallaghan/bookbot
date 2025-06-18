def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(word_count(text))

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    words = text.split()
    return len(words)


main()