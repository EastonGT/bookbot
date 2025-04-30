def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import get_word_count
from stats import get_char_count

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")

    char_counts = get_char_count(book_text)
    print("Character counts:")
    print(char_counts)

if __name__ == "__main__":
    main()