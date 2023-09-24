def reverse(input_string):
 
    if len(input_string) % 4 == 0:
       
        reversed_string = input_string[::-1]
        return reversed_string
    else:
        return input_string  

input_str = "abcdefgh"
result = reverse(input_str)
print(result)  

input_str = "abcde"
result = reverseinput_str)
print(result) 
