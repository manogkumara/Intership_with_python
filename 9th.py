def remove_nth_character(input_string, n):
  
    if n < 0 or n >= len(input_string):
        return "Invalid index"

  
    result_string = input_string[:n] + input_string[n+1:]

    return result_string
input_string = "Hello, World!"
n = 5  # Remove the character at index 5 (which is ',')

result = remove_nth_character(input_string, n)
print("Original String:", input_string)
print("String after removing character at index", n, ":", result)
