from itertools import chain, product

# initializing tuples
test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

# printing original tuples
print("The original tuple 1 : " + str(test_tuple1))
print("The original tuple 2 : " + str(test_tuple2))

# All pair combinations of 2 tuples
# Using chain() + product()
res = list(chain(product(test_tuple1, test_tuple2), product(test_tuple2, test_tuple1)))

# printing result
print("The filtered tuple : " + str(res))
