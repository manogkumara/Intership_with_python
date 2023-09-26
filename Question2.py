class BracketValidator:
    def is_valid(self, s):
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack.pop() != brackets[char]:
                    return False

        return len(stack) == 0


# Example usage:
validator = BracketValidator()

# Test cases
print(validator.is_valid("()"))            # Valid
print(validator.is_valid("()[]{}"))        # Valid
print(validator.is_valid("[)"))            # Invalid
print(validator.is_valid("({[)]"))        # Invalid
print(validator.is_valid("{{{"))            # Invalid
