
import math

try:
    number = float(input("Enter a number: "))

    sqrt_val = math.sqrt(number)
    log_val = math.log(number)
    sin_val = math.sin(number)

    print(f"Square root: {sqrt_val}")
    print(f"Logarithm: {log_val}")
    print(f"Sine: {sin_val}")
except ValueError:
    print("Please enter a valid number greater than 0 for logarithmic and square root operations.")
