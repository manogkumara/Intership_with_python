class StringReverser:
    def reverse_words(self, input_string):
        words = input_string.split()  # Split the input string into words
        reversed_string = ' '.join(reversed(words))  # Reverse the words and join them

        return reversed_string

# Example usage:
string_reverser = StringReverser()
input_string = 'hello .py'
result = string_reverser.reverse_words(input_string)
print(result)  # Output: '.py hello'
