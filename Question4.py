
x = float(input("Enter the length of side x: "))
y = float(input("Enter the length of side y: "))
z = float(input("Enter the length of side z: "))

if x + y > z and y + z > x and x + z > y:
    if x == y and y == z:
        print("Equilateral triangle")
    elif x != y and y != z and x != z:
        print("Scalene triangle")
    else:
        print("Isosceles triangle")
else:
    print("Invalid triangle")
