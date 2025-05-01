def get_word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_char_list(char_counts):
    sorted_chars = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "num": count})

    # Sort the list in place based on the 'num' value in descending order
    sorted_chars.sort(key=lambda item: item['num'], reverse=True)
    return sorted_chars