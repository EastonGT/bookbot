import sys
from stats import get_word_count, get_char_counts, get_sorted_char_list

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    if book_text:
        word_count = get_word_count(book_text)
        char_counts = get_char_counts(book_text)
        sorted_char_list = get_sorted_char_list(char_counts)

        print("=" * 20 + " BOOKBOT " + "=" * 20)
        print(f"Analyzing book found at {filepath}...")
        print("-" * 15 + " Word Count " + "-" * 15)
        print(f"Found {word_count} total words")
        print("-" * 15 + " Character Count " + "-" * 15)
        for item in sorted_char_list:
            print(f"{item['char']}: {item['num']}")
        print("=" * 20 + " END " + "=" * 20)

if __name__ == "__main__":
    main()