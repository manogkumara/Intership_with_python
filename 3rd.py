
input_string = input("Enter a string: ")

if len(input_string) < 2:
    result_string = ""  
else:
    result_string = input_string[:2] + input_string[-2:]

# Display the result
print("Result:", result_string)
