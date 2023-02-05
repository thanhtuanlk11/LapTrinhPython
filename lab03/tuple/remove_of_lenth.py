# initializing list
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 1

# filter() filters non K length values and returns result
res = list(filter(lambda x : len(x) != K, test_list))

# printing result
print("Filtered list : " + str(res))
