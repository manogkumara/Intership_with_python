# Lambda function to check if a string meets the requirements
check_string = lambda s: all([
    any(c.isupper() for c in s),  # Contains at least one capital letter
    any(c.islower() for c in s),  # Contains at least one lowercase letter
    any(c.isdigit() for c in s),  # Contains at least one digit
    len(s) >= 10  # Meets the minimum length requirement
])

# Input string
input_string = "PaceWisd0m"

# Check if the input string is valid
if check_string(input_string):
    print("Valid string")
else:
    print("Invalid string")
