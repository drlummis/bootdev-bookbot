def main():
    book = "books/frankenstein.txt"
    text = get_file_text(book)
    word_count = get_word_count(text)
    chars = get_character_counts(text)
    print(word_count)
    print(chars)

def get_file_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

main()
