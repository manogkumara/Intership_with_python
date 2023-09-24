input_string = input("Enter a string: ")
if len(input_string) < 2:
    result_string = input_string  
else:
    first_char = input_string[0]
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    result_string = modified_string
print("Result:", result_string)
