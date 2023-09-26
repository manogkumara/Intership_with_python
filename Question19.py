
mixed_list = [1, 'apple', 3.14, 42, 'banana', 2.718, 'cherry', 7]

# Initialize empty lists to store integers, strings, and floats
int_list = []
str_list = []
float_list = []

# Iterate through the mixed list and categorize elements into the appropriate lists
for item in mixed_list:
    if isinstance(item, int):
        int_list.append(item)
    elif isinstance(item, float):
        float_list.append(item)
    elif isinstance(item, str):
        str_list.append(item)

# Print the separate lists
print("Integers:", int_list)
print("Floats:", float_list)
print("Strings:", str_list)
