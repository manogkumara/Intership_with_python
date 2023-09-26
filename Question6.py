class PowerCalculator:
    def my_pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result

# Example usage:
power_calculator = PowerCalculator()
x = 2.0
n = 10
result = power_calculator.my_pow(x, n)
print(result)  # Output: 1024.0
