
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    number = int(input("Enter a number: "))
    result = factorial(number)
    print(f"Factorial of {number} is: {result}")
except ValueError:
    print("Please enter a valid integer.")
