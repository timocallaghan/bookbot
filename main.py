def main():
    from stats import word_count, letter_count
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    print(f"{count} words found in the document")
    print(letter_count(text))

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

main()