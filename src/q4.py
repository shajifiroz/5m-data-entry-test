def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return s[::-1]

# Task 2: Test cases
print(string_reverse("Hello World"))  # Output: "dlroW olleH"
print(string_reverse("Python"))       # Output: "nohtyP"
