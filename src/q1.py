def swap(x, y):
    """
    Swaps the values of x and y if both are numeric.
    Returns -1 if either x or y is not numeric.
    """
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap values using arithmetic operations (no additional variables)
    x = x + y
    y = x - y
    x = x - y
    
    # Print swapped values
    print(f"Swapped values: x = {x}, y = {y}")

# Scenario 1: "Apple", 10
result1 = swap("Apple", 10)
print(result1)  # Expected output: -1 because "Apple" is not numeric

# Scenario 2: 9, 17
result2 = swap(9, 17)
# Expected output:
# Swapped values: x = 17, y = 9
