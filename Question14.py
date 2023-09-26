# Define the numbers for which you want to print the multiplication tables
numbers = [24, 50, 29]

# Define the range for the multiplication tables (e.g., 1 to 10)
start = 1
end = 10

# Loop through each number and print its multiplication table
for num in numbers:
    print(f"Multiplication table of {num}:")
    for i in range(start, end + 1):
        product = num * i
        print(f"{num} x {i} = {product}")
    print()  # Print a blank line to separate tables
