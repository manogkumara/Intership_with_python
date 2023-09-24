
def starts_with(input_string, specified_chars):
    return input_string.startswith(specified_chars)

input_str = "Hello, World!"
specified_chars = "Hello"
if starts_with(input_str, specified_chars):
        print(f"The string does not start with '{specified_chars}'.")
