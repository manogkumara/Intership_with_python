# Initialize variables to store the sum, count, and product
total = 0
count = 0
product = 1

# Continue taking inputs until 'q' is pressed
while True:
    user_input = input("Enter an integer (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if user_input == 'q':
        break
    
    try:
        # Try to convert the user input to an integer
        num = int(user_input)
        
        # Update sum, count, and product
        total += num
        count += 1
        product *= num
    except ValueError:
        print("Invalid input. Please enter an integer or 'q' to quit.")

# Calculate the average
if count > 0:
    average = total / count
    print(f"Average: {average}")
else:
    print("No valid numbers were entered.")

# Print the product
print(f"Product: {product}")
