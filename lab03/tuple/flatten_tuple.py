
test_tuple = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
res=[]
for i in test_tuple:
	res.extend(i)
res=tuple(res)
# printing result
print("The flattened tuple : " + str(res))
