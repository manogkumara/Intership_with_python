
num = int(input("Enter an integer: "))
reversed_num = 0
while num != 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print(f"The reversed number is: {reversed_num}")

