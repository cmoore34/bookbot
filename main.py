from stats import words_in_string, num_of_chars_in_string, sort_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_name=sys.argv[1]
    word_count = words_in_string(get_book_text(file_name))
    letter_count = num_of_chars_in_string(get_book_text(file_name))
    letters_sorted = sort_list(letter_count)
    print_report(file_name, word_count, letters_sorted)

main()