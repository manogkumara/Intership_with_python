# Input length and breadth from the user
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Check if it's a square or a rectangle
if length == breadth:
    print("It's a square.")
else:
    print("It's a rectangle.")
