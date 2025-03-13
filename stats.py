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
