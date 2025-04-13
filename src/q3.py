def update_dictionary(dct, key, value):
    """
    Updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Returns the updated dictionary.
    """
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    dct[key] = value
    return dct

# Task 2: Invoke the function using the given scenarios

# Scenario 1: Empty dictionary, adding "name": "Alice"
result1 = update_dictionary({}, "name", "Alice")
print("Updated Dictionary (Scenario 1):", result1)

# Scenario 2: Dictionary with "age": 25, updating "age" to 26
result2 = update_dictionary({"age": 25}, "age", 26)
print("Updated Dictionary (Scenario 2):", result2)
