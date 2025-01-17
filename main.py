def main():
    book = "books/frankenstein.txt"
    text = get_file_text(book)
    word_count = get_word_count(text)
    print(word_count)

def get_file_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def get_word_count(text):
    words = text.split()
    return len(words)

main()
