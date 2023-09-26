# Initialize an empty list
my_list = []

# Take inputs from the user to create the list
while True:
    user_input = input("Enter an element to add to the list (press Enter to stop): ")
    if user_input == "":
        break
    my_list.append(user_input)

# Display the current list
print("Current list:", my_list)

# Take an input from the user to search and delete an element
element_to_delete = input("Enter an element to search and delete: ")

# Check if the element exists in the list, and if found, remove it
if element_to_delete in my_list:
    my_list.remove(element_to_delete)
    print(f"{element_to_delete} has been deleted from the list.")

# Iterate over the updated list using a for loop
print("Updated list after deletion:")
for item in my_list:
    print(item)
