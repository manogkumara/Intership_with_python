string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if len(string1) >= 2 and len(string2) >= 2:
   result_string = string2[:2] + string1[2:] + ' ' + string1[:2] + string2[2:]
else:
    result_string = "Both strings must have at least two characters to perform the swap."
print("Result:", result_string)
