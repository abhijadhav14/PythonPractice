import math
from scientific_calculator import ScientificCalculator

# Example Usage:
scientific_calculator = ScientificCalculator()

# Using basic arithmetic operations from the Calculator class
result_add = scientific_calculator.add(10, 5)
print("10 + 5 =", result_add)

result_sub = scientific_calculator.subtract(10, 5)
print("10 - 5 =", result_sub)

result_mul = scientific_calculator.multiply(10, 5)
print("10 * 5 =", result_mul)

try:
    result_div = scientific_calculator.divide(10, 0)  # Division by zero error
except ZeroDivisionError as e:
    print("Error:", e)

result_div = scientific_calculator.divide(10, 5)
print("10 / 5 =", result_div)

# Using trigonometric functions from the ScientificCalculator class
angle_rad = math.radians(45)  # Convert 45 degrees to radians
result_sin = scientific_calculator.sin(angle_rad)
print("sin(45 degrees) =", result_sin)

result_cos = scientific_calculator.cos(angle_rad)
print("cos(45 degrees) =", result_cos)

result_tan = scientific_calculator.tan(angle_rad)
print("tan(45 degrees) =", result_tan)
