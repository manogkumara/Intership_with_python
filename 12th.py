def convert(input_string):

    upper_count = sum(1 for char in input_string[:4] if char.isupper())
    if upper_count >= 2:
      
        return input_string.upper()
    else:
        return input_string 

input_str = "AbCde"
result = convert(input_str)
print(result) 

input_str = "aBCde"
result = convert(input_str)
print(result) 

input_str = "ABcde"
result = convert(input_str)
print(result)  

input_str = "abcde"
result = convert(input_str)
print(result) 
