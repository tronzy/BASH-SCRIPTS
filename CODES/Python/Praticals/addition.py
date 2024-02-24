def add_numbers(num1, num2):
    """Adds two numbers and returns the sum.

    Args:
        num1: The first number to add.
        num2: The second number to add.

    Returns:
        The sum of num1 and num2.
    """

    sum = num1 + num2
    return sum

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
result = add_numbers(num1, num2)

# Print the result
print("The sum of", num1, "and", num2, "is", result)