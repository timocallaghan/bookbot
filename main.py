import sys
from stats import word_count, letter_count, dict_sort

def main(filepath):
    text = get_book_text(filepath)
    count = word_count(text)
    letters = letter_count(text)
    sorted_dict = dict_sort(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for d in sorted_dict:
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

if len(sys.argv) != 2 :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])