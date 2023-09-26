# Input quantity from the user
quantity = int(input("Enter the quantity: "))

# Define the cost per unit
cost_per_unit = 100

# Calculate the total cost without discount
total_cost = quantity * cost_per_unit

# Check if the total cost is more than 1000 to apply the discount
if total_cost > 1000:
    discount = 0.10 * total_cost  # 10% discount
    total_cost -= discount

# Print the total cost
print(f"Total cost: {total_cost}")
