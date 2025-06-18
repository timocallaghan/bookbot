def main():
    from stats import word_count, letter_count, dict_sort
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    letters = letter_count(text)
    sorted_dict = dict_sort(letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for d in sorted_dict:
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

main()