# Original list of numbers
original_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# Create a lambda function to check if a number is divisible by nineteen or thirteen
is_divisible = lambda x: x % 19 == 0 or x % 13 == 0

# Initialize an empty list to store divisible numbers
divisible_numbers = []

# Iterate through the original list and add divisible numbers to the result list
for num in original_list:
    if is_divisible(num):
        divisible_numbers.append(num)

# Print the result
print("Numbers of the above list divisible by nineteen or thirteen:", divisible_numbers)
