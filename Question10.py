salary = float(input("Enter the employee's salary: "))
years_of_service = int(input("Enter the employee's years of service: "))

# Define the bonus rate (5% as 0.05)
bonus_rate = 0.05

# Check if the employee's years of service is more than 5
if years_of_service > 5:
    # Calculate the bonus amount
    bonus_amount = salary * bonus_rate
    print(f"Net bonus amount: ${bonus_amount:.2f}")
else:
    print("No bonus is applicable.")
