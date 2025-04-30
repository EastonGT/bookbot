def get_word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_char_count(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts