x = 5
def add():
    """
    Adds 5 to a local variable 'x' and prints its value.
    """
    x = 3
    x = x + 5  # Same as x = x + 5
    print(x)

# Call the add function
add()

# Print the global variable 'x' (unchanged because of function scope)
print(x)
