def find_longest_word(words):
    if not words:
        return 0  

    max_length = len(words[0])  

    for word in words:
        current_length = len(word)
        if current_length > max_length:
            max_length = current_length
    return max_length
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
longest_word_length = find_longest_word(word_list)
print("The length of the longest word is:", longest_word_length)
