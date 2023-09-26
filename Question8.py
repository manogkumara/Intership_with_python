class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Enter a string: ")

    def print_string(self):
        print("Reversed string:", self.input_string[::-1])

# Example usage:
string_manipulator = StringManipulator()
string_manipulator.get_string()
string_manipulator.print_string()
