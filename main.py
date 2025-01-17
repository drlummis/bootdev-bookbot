def main():
    book_path = "books/frankenstein.txt"
    text = get_file_text(book_path)
    word_count = get_word_count(text)
    chars_dict = get_character_counts(text)
    print_report(book_path, word_count, chars_dict)

def get_file_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    chars = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def print_report(book_path, word_count, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    print_character_counts(chars_dict)
    print("--- End report ---")

def print_character_counts(chars_dict):
    chars_list = convert_chars_dict_to_list(chars_dict)
    sort_chars_list(chars_list)
    for dic in chars_list:
        char = dic["letter"]
        count = dic["count"]
        print(f"The '{char}' character was found {count} times")

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
