
total = 0
count = 0

while True:
    num = int(input("Enter an integer (0 to finish): "))
    
    # Check if the user wants to finish
    if num == 0:
        break
    
    # Add the number to the total and increment the count
    total += num
    count += 1

# Check if at least one number was entered
if count > 0:
    average = total / count
    print(f"Sum: {total}")
    print(f"Average: {average}")
else:
    print("No numbers were entered.")
