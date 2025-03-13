import sys
from stats import get_word_count
from stats import get_character_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_file_text(book_path)
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    chars_dict = get_character_counts(text)
    print(chars_dict)
    print_report(book_path, word_count, chars_dict)

def get_file_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def print_report(book_path, word_count, chars_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_character_counts(chars_dict)
    print("============= END ===============")

def print_character_counts(chars_dict):
    chars_list = convert_chars_dict_to_list(chars_dict)
    sort_chars_list(chars_list)
    for dic in chars_list:
        char = dic["letter"]
        count = dic["count"]
        print(f"{char}: {count}")

def convert_chars_dict_to_list(chars_dict):
    chars_list = []
    for key in chars_dict:
        count = chars_dict[key]
        chars_list.append({ "letter" : key, "count" : count})
    return chars_list

def sort_chars_list(chars_list):
    chars_list.sort(reverse=True, key=sort_chars_list_key)

def sort_chars_list_key(chars_dict):
    return chars_dict["count"]

main()
