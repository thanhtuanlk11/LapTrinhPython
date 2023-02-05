test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))

# printing original tuple
print("The original tuple : " + str(test_tuple))

# initializing Keys
keys = ['key', 'value', 'id']

# Convert Nested Tuple to Custom Key Dictionary
# Using zip() + list comprehension
res = [{key: val for key, val in zip(keys, sub)}
						for sub in test_tuple]

# printing result
print("The converted dictionary : " + str(res))
