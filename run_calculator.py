from calculator import Calculator

# Example Usage:
calculator = Calculator()

# Addition
result_add = calculator.add(10, 5)
print("10 + 5 =", result_add)

# Subtraction
result_sub = calculator.subtract(10, 5)
print("10 - 5 =", result_sub)

# Multiplication
result_mul = calculator.multiply(10, 5)
print("10 * 5 =", result_mul)

# Division
try:
    result_div = calculator.divide(10, 0)  # Division by zero error
except ZeroDivisionError as e:
    print("Error:", e)

result_div = calculator.divide(10, 5)
print("10 / 5 =", result_div)
