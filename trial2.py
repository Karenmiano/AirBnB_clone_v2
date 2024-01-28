my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_to_check = ['a', 'b', 'd']

# Using a generator expression
result = all(key in my_dict for key in keys_to_check)

# Alternatively, using a list comprehension
# result = all([key in my_dict for key in keys_to_check])

print(result)  # Output: True if all keys are present, False otherwise
