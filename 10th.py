def unique_sorted_words(input_str):
    words = input_str.split(',')

    unique_words = set(word.strip() for word in words)

    sorted_words = sorted(unique_words)

    result_str = ', '.join(sorted_words)

    return result_str

input_sequence = "red, white, black, red, green, black"
sorted_unique_words = unique_sorted_words(input_sequence)
print("Unique words in sorted form:", sorted_unique_words)
