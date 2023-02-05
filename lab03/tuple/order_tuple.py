
test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

# printing original list
print("The original list is : " + str(test_list))

# initializing order list
ord_list = ['Geeks', 'best', 'CS', 'Gfg']

# Order Tuples by List
# Using setdefault() + sorted() + lambda
temp = dict()
for key, ele in enumerate(ord_list):
	temp.setdefault(ele, []).append(key)	
res = sorted(test_list, key = lambda ele: temp[ele[0]].pop())

# printing result
print("The ordered tuple list : " + str(res))
