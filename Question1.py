class RomanConverter:
    def __init__(self):
        self.roman_numerals = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

    def int_to_roman(self, num):
        if not 1 <= num <= 3999:
            return "Invalid input. Please enter an integer between 1 and 3999."

        result = ""
        for symbol, value in self.roman_numerals.items():
            while num >= value:
                result += symbol
                num -= value

        return result

    def roman_to_int(self, roman):
        result = 0
        i = 0

        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i + 2] in self.roman_numerals:
                result += self.roman_numerals[roman[i:i + 2]]
                i += 2
            else:
                result += self.roman_numerals[roman[i]]
                i += 1

        return result
converter = RomanConverter()

# Convert integer to Roman numeral
roman_numeral = converter.int_to_roman(1987)
print(f"Integer 1987 as Roman numeral: {roman_numeral}")

# Convert Roman numeral to integer
integer_value = converter.roman_to_int("MCMLXXXVII")
print(f"Roman numeral 'MCMLXXXVII' as integer: {integer_value}")
