def main():
    book = "books/frankenstein.txt"
    text = get_file_text(book)
    print(text)

def get_file_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

main()
