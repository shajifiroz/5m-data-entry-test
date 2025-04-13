def check_divisibility(num, divisor):
    """
    Check if the number (num) is divisible by another number (divisor).
    Both num and divisor must be numeric.
    Return True if num is divisible by divisor, False otherwise.
    """
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        raise ValueError("Both num and divisor must be numeric.")
    
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    
    return num % divisor == 0


# Task 2
# Function definition
def check_divisibility(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed."
    if num1 % num2 == 0:
        return f"{num1} is divisible by {num2}."
    else:
        return f"{num1} is not divisible by {num2}."

# Task 2: Invoke the function with the given scenarios
# Scenario 1: 10, 2
result1 = check_divisibility(10, 2)
print(result1)

# Scenario 2: 7, 3
result2 = check_divisibility(7, 3)
print(result2)
